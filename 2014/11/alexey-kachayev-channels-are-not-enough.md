Title: Channels Are Not Enough
SubTitle: ... or Why Pipelining Is Not That Easy
Author: kachayev
Date: 2014-11-01
Summary: [Golang](https://talks.golang.org/2012/concurrency.slide#1) [Concurrency](http://blog.golang.org/advanced-go-concurrency-patterns) [Patterns](http://blog.golang.org/pipelines) for brave and smart.
Category: Theory
Tags: golang

## Intro

Go was designed for building concurrency applications easily so it has goroutines for running independent computations and channels to communicate with each other. We've all heard this story before. All examples and tutorials look just fine: we can create a new channel, we can send to a channel, we can read from a channel, we even have the nifty, elegant select statement (__btw, why do we still have statements in 21th century?__), blocking reads and buffers…

![channels](https://pbs.twimg.com/media/BvBSJJQCAAAWH8e.jpg)

Keynote: **99% of time I don't really care if the response is delivered with a channel or a magical unicorn brought it on its horn.**

It’s so cool to find yourself writing tutorial for beginners! And it's a bit painful when you are trying to implement big and sophisticated system(s). Channels are [primitives](https://golang.org/doc/). They are low-level building blocks and I highly doubt you want to work with them on daily basis.

Look at ["advanced patterns"](http://blog.golang.org/advanced-go-concurrency-patterns) and ["pipeline"](http://blog.golang.org/pipelines). Not that simple right? Too many things to keep in mind and constantly memorize: when and how to close channels, how to propagate errors, how to free resources. I'm complaining about this not because I've tried implementing something and failed. But because I work with stuff like this every single day.

You can say that it's not necessary for beginner to understand all of the details of the whole picture. But... are described patterns really "advanced"? Unfortunately, the answer is *NO*. They're basic and common.

Take a closer look to pipeline problem. Is it really a pipeline? No… "...for each path from directory calculate `MD5` checksum and collect result to a single `map[string]string`...". It’s just a `pmap` (parallel map). Or `pmap` with `pool of executors` in case of bounded parallelism. And `pmap` should not require that I enter so [many][scala-pmap] [lines][clojure-pmap] of code. Wanna look at the real pipelining problem - I will describe one at the end of the article (see "Building Twitter Analyzer" paragraph).

## So What About Patterns?

To develop real-world applications fast enough we should be able to distil higher level abstractions than primitive channels. They are only a transport layer. We need application level abstractions to write programs (compare to [OSI](http://en.wikipedia.org/wiki/OSI_model)), otherwise you will find yourself in constantly digging through low-level details of your channels network trying to find why it doesn’t work. Only on production machine. From time to time. Without any reasonable steps to reproduce. Check [Erlang OTP](http://learnyousomeerlang.com/what-is-otp) that aims to solve the same problem: to protect you from low-level message passing code.

What is the problem with low-level code? There is a great article ["Edward C++Hands"](http://bartoszmilewski.com/2013/09/19/edward-chands/):

> Having scissors for hands in not all that bad. Edward has many talents: he can, for instance, create stunning dog hairdos. Don’t get me wrong — there were many stunning dog hairdos on display (I mean C++ code that was elegant and simple) but the bulk of the conference was about how to avoid mutilation and how to deliver first aid in case of accidental amputation.

At [Kyiv Go Meetup][go-meetup] I experienced the same situation: 20 lines of clean and readable code on a single slide. One non-trivial race condition and one possible runtime panic. Was it obvious for all listeners? No. Not even for half of them.

## Any Reason for Panic?

Ok. Let’s try to collect such patterns. From work experience, from books, from other languages (yeah, guys, I know that it's hard to believe but there are several other languages also designed for concurrency).

Rob Pike [talks][rob-pike] about Fan-in, Fan-out. It’s useful in many ways, but still about the network of channels. Not about your application. In any case, let's check (shamelessly stolen from [here](http://blog.golang.org/pipelines)).

```go
func merge(cs ...<-chan int) <-chan int {
    var wg sync.WaitGroup
    out := make(chan int)

    // Start an output goroutine for each input channel in cs.  output
    // copies values from c to out until c is closed, then calls wg.Done.
    output := func(c <-chan int) {
        for n := range c {
            out <- n
        }
        wg.Done()
    }
    wg.Add(len(cs))
    for _, c := range cs {
        go output(c)
    }

    // Start a goroutine to close out once all the output goroutines are
    // done.  This must start after the wg.Add call.
    go func() {
        wg.Wait()
        close(out)
    }()
    return out
}
```

Hm... `<-chan int`. Not that abstract to reuse in my own application (i.e. move to library)... And not that obvious to reimplement each time when I need it. How to make it reusable? `<-chan interface{}`? Welcome to the land of types casting and runtime panics. If you want to implement high level fan-in (merge) you’re losing type safety. The same (unfortunately) goes for all other patterns.

What I really want here is:

```go
func merge[T](cs ...<-chan T) <-chan T
```

Yeah, I know that Go [doesn't have generics](http://golang.org/doc/faq#generics) because who ever need them?

## What is the Weather Now?

Return to patterns. Let’s analyse hypothetical project that’s really close to practical experience in server-side development. We need a server that accepts request about weather for a given USA state and respond with info collected from [OpenWeatherMap](http://openweathermap.org/api). In such a way:

```shell
$ http localhost:4912/weather?q=CA
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Type: application/json; charset=utf-8
```

```json
[{
    "clouds": {
        "all": 40
    },
    "id": 5391959,
    "main": {
        "temp": 288.89,
        "temp_max": 291.48,
        "temp_min": 286.15
    },
    "name": "San Francisco",
    "weather": [
        {
            "description": "mist",
            "icon": "50d",
            "id": 701,
            "main": "Mist"
        }
    ]
}, {
    "clouds": {
        "all": 90
    },
    "id": 5368361,
    "main": {
        "temp": 292.83,
        "temp_max": 296.15,
        "temp_min": 289.15
    },
    "name": "Los Angeles",
    "weather": [
        {
            "description": "mist",
            "icon": "50d",
            "id": 701,
            "main": "Mist"
        }
    ]
}]
```

### Pmap

Let's start from something that we already know. So, we've got the request `?q=CA`. I don't want to specify where we're going to find list of relative cities. We can use for this database, in-memory cache or whatever reasonable. Assume that we have magical `findCities(state)` function that returns `chan City` (as most universal `go` representation for lazy sequence). Next? For each city we have to call OpenWeatherMap API and collect results into single `map[City]Weather`. We've talked about such pattern already. It's `pmap`. And I want my code to look like

```go
chanCities := findCities(state)
resolver := func(name City) Weather { return openWeatherMap.AskFor(name) }
weather := chanCities.Par.Map(resolver)
```

or in case of bounded parallelism

```go
chanCities := findCities(state)
pool := NewWorkers(20)
resolver := func(w Worker, name City) Weather { return w.AskFor(name) }
weather := chanCities.Par.BoundedMap(pool, resolver)
```

That's it. I want all this `<-done` synchronizations and `select` sacramentals to be entire hidden.

### Futures & Promises

It can take a long time to get current weather, i.e. when you have long list of cities for concrete state. Off course you don't want to duplicate API calls so you should manage simultaneous requests somehow:

```go
func collect(state string) Weather {
  calc, ok := calculations.get(state) // check if it's in progress
  if !ok {
      calc = calculations.run(state) // run otherwise
  }
  return calc.Wait() // wait until done
}
```

This is so called [future/promise](http://en.wikipedia.org/wiki/Futures_and_promises). From Wiki:

> They describe an object that acts as a proxy for a result that is initially unknown, usually because the computation of its value is yet incomplete.

I've heard from a number of people that `go` `future` is a simple:

```go
f := make(chan int, 1)
```

Which is wrong because all waiters should get result. And this version is also wrong:

```go
f := make(chan int, 1)
v <- f
f <- v
// use v here
```

Because it's impossible to manage resources this way. And I wish you luck finding a bug if somebody missed the `f <- v` part in his code.

It's not that hard though to implement `promise` directly storing all waiters (I'm not sure that this code is really bugs free):

```go
type PromiseDelivery chan interface{}
type Promise struct {
  sync.RWMutex
  value interface{}
  waiters []PromiseDelivery
}

func (p *Promise) Deliver(value interface{}) {
  p.Lock()
  defer p.Unlock()
  p.value = value
  for _, w := range p.waiters {
    locW := w
    go func(){
      locW <- value
    }()
  }
}

func (p *Promise) Value() interface{} {
  if p.value != nil {
    return p.value
  }

  delivery := make(PromiseDelivery)
  p.waiters = append(p.waiters, delivery)
  return <-delivery
}

func NewPromise() *Promise {
  return &Promise{
    value: nil,
    waiters: []PromiseDelivery{},
  }
}
```

How to use it?

```go
p := NewPromise()
go func(){
  p.Deliver(42)
}()
p.Value().(int) // blocks and returns interface{} when ready
```

But `interface{}` and type casting are already here. What do I really want?

```go
// .. somewhere in well-tested library or even in stdlib
type PromiseDelivery[T] chan T
type Promise[T] struct {
  sync.RWMutex
  value T
  waiters []PromiseDelivery[T]
}
func (p *Promise[T]) Deliver(value T)
func (p *Promise[T]) Value() T
func NewPromise[T]() *Promise[T]

// in my code:
v := NewPromise[int]()
go func(){
  v.Deliver("woooow!") // compilation error
  v.Deliver(42)
}()
v.Value() // blocks and returns 42, not interface{}
```

No, sure, nobody needs generics. What the hell am I talking about?

You can also avoid `p.Lock()` using `select` to listen to `deliver` and `wait` operations in a single goroutine. You can also introduce special `.ValueWithTimeout` method which will be really helpful for end users. And there're lots of other "you can...". Despite the fact that we're talking about 20 lines of code (that probably will grow each time you discover more details of futures/promises interactions). Do I really need to know (or even think) about channels that delivered me the value? No.

### Pub/sub

Assume that we want to build real-time service. So now our client can open websocket connection with a `q=CA` request and get instant updates about weather changes in California. It would look something like:

```go
// deliverer
calculation.WhenDone(func(state string, w Weather) {
  broker.Publish("CA", w)
})

// client
ch := broker.Subscribe("CA")
for update := range ch {
  w.Write(update.Serialize())
}
```

It's a typical pub/sub. You can learn about it from [Advanced Go Patterns](http://blog.golang.org/advanced-go-concurrency-patterns) talk and even find ready-to-use [implementations](https://github.com/tuxychandru/pubsub). The problems is that [they](https://github.com/tuxychandru/pubsub/blob/master/pubsub.go#L34) [are](https://github.com/tuxychandru/pubsub/blob/master/pubsub.go#L48) [all](https://github.com/tuxychandru/pubsub/blob/master/pubsub.go#L54) [about](https://github.com/tuxychandru/pubsub/blob/master/pubsub.go#L58) interfaces.

Is it possible to implement:

```go
broker := NewBroker[String, Weather]()
// so that
broker.Subs(42) // compilation failure
// and
broker.Subs("CA") // returns (chan Weather) not (chan interface{})
```

Sure! If you're brave enough to copy-paste code from project to project with small fixes here and there.

### Map/filter

Assume that we want to give our users more flexibility and we're introducing new query params: `show` which can be equal to `all|temp|wind|icon`.

Probably you'll start from simples:

```go
ch := broker.Subscribe("CA")
for update := range ch {
  temps := []Temp
  for _, t := update.Temp {
    temps = append(temps, t)
  }

  w.Write(temps)
}
```

But after 10 such methods you'll realize that it's not composable and even boring. Maybe you need

```go
ch := broker.Subscribe("CA").Map(func(w Weather) Temp { return w.Temp })
for update := range ch {
  w.Write(update)
}
```

Wait, did I just say that channel is a [functor](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)? As well as Future/Promise.

```go
p := NewPromise().Map(func(w Weather) Temp { return w.Temp })
go func(){
  p.Deliver(Weather{Temp{42}})
}()
p.Value().(Temp) // Temp, not Weather
```

Which means that I can reuse the same code for channels and futures. You may also end up with something like [transducers](http://blog.cognitect.com/blog/2014/8/6/transducers-are-coming). I frequently use in ClojureScript code tricks like

```clojure
(->> (send url) ;; returns chan, put single value to it {:status 200 :result 42} when ready
     (async/filter< #(= 200 (:status %))) ;; check that :status is 200
     (async/map< :result)) ;; expose only 42 to end user
;; note, that it will close all channels (including implicit intermediate one) properly
```

Do I really have to worry if `x` is a channel or a future if I can simply do `x.Map(transformation)` and get back value of the same type? Probably not. In this case why am I allowed to do `make(chan int)` and not `make(Future int)`?

### Request/Reply

Assume that our users like our service and use it actively. So we decided to introduce a simple API limitation: number of requests for each IP, per day. It's simply to collect the number of calls into single `map[string]int`. Go docs [says](http://blog.golang.org/share-memory-by-communicating) "Do not communicate by sharing memory; instead, share memory by communicating". Ok, sounds like a nice idea.

So for the first we need the goroutine that will be responsible for collecting number of requests.

```go
req := make(chan string)
go func() { // wow, look here - it's an actor!
  m := map[string]int{}
  for r := range req {
    if v, ok := m[r]; !ok {
      m[r] = 1
    } else {
      m[r] = v + 1
    }
  }
}()

go func() {
  req <- "127.0.0.2"
}()

go func() {
  req <- "127.0.0.1"
}()
```

It's easy. Now can calculate number of requests for each IP. Not that much... We also have to be able to ask permission to execute request.

```go
type Req struct {
  ip string
  resp chan int
}

func NewRequest(ip string) *Req {
  return &Req{ip, make(chan int)}
}

requests := make(chan *Req)

go func() {
  m := map[string]int{}
  for r := range requests {
    if v, ok := m[r.ip]; !ok {
      m[r.ip] = 1
    } else {
      m[r.ip] = v + 1
    }
    r.resp <- m[r.ip]
  }
}()

go func() {
  r := NewRequest("127.0.0.2")
  requests <- r
  fmt.Println(<- r.resp)
}()

go func() {
  r := NewRequest("127.0.0.1")
  requests <- r
  fmt.Println(<- r.resp)
}()
```

I won't even try to ask you about generic solution (without hardcoded strings and ints). I ask you instead, to check if everything is right with this code? Is it that simple?

Are you sure, that `r.resp <- m[r.ip]` is a good solution? No. Definitely not. I don't want anybody to wait for slow clients. Yes? And what if I have too many slow clients? Maybe I have to handle this somehow.

Is this part `requests <- r` that simple? What if my actor (server) is too busy to reply now? Maybe I need to handle timeouts here...

And from time to time I need to specify initialization process.. And cleanup... Both with timeouts. And the ability to hold requests until initialization is finished.

What about priority of calls? I.e. when I need to implement `Dump` procedure for my analytic system but I don't want to pause all users until analytics data is collected.

And... Looks like `gen_server` in [Erlang](http://www.erlang.org/doc/man/gen_server.html). For sure I want it to be implemented once and shipped with well-documented library with high test coverage rate. 98% of time I don't want to see this `resp: make(chan int, ?)` and I really don't want to think what should I put instead of `?`.

**99% of time I don't really care if the response is delivered with a channel or a magical unicorn brought it on its horn.**

### And counting

There are many other common concurrency situations. I think you've already gotten the idea.

## The Pain

You can tell me, that described patterns are not common. But.. I have to implement almost all of them in all my projects. Every. Single. Time. Maybe I’m just out of luck and your projects are as simple as tutorial for beginners.

I know that most of you will say "world is too hard and programming is too painful". I continue to upset you: there are at least a few examples of languages that solved this problem at least partially. Or at least working on solving it. Haskell and Scala type systems give you ability to build strong [high-level abstractions][haskell-book] or even custom [control flows][oz-style] to [deal](https://github.com/scala/async) with concurrency. An opposite Clojure is dynamically typed that encourage you to distil and share [high level][clojure-async] [abstraction][clojure-trans]. Rust has [channels](http://doc.rust-lang.org/std/comm/) and [generics](http://doc.rust-lang.org/rust.html#generic-functions).

Make it work -> Make it beautiful -> Make it reusable.

Now that the first step is done. What's next? Don't get me wrong, `go` is a perspective language: channels and goroutines are way much better than i.e. `pthread`, but should we really stop here?


## P.S. Building Twitter Analyzer

About real-world pipelining.

Probably you've already seen [Twitter Analytics](https://analytics.twitter.com/) which is really great. Assume for the time being, that it's not introduced yet and we have to run our own analysis: for a given username calculate how many unique users saw (at least theoretically) each of his own tweets. How we can do this? Not that hard really: read user's timeline, filter away all retweets and replies, for all other tweets ask for all retweeters, for each retweeter ask for a list of followers, merge all retweeters' followers together and add own user's followers. What I want to have as a result of these steps: `map[TweetId][]Username` (retweeters) and `map[Username][]Username`. It would be enough to build a fancy table to show to the requester.

Few technical details that you should be aware of:

- Twitter API requires OAuth for each call and sets strong limitations (450 calls per 15 minutes per each user). To deal with such a limitation, we're going to use a predefined list of OAuth tokens (i.e. 50) organized into a pool of workers where each worker is able to suspend himself before facing problems with limits.

- Most Twitter API calls use pagination for results with `since_id` or `max_id` continuations. So you can't rely on the fact that single call to worker will give you full result.

[Example of rough implementation](https://gist.github.com/kachayev/50d89615101444cd62ad). Note, that there is no need for you to understand everything in this file. Just the opposite. If you can't understand it after quick screening then we're on the right path.

So what do we have here?

1. Few stages of computations: `TimelineReader` -> `RetweetersReader` -> `FollowersReader` -> `FinalReducer`.

2. Self-stage messaging. All stages are a recursive cause of pagination. It means that each stage emits messages both to the next stage and to itself. It's much harder to deal with cancellations in this case. Or even find out when everything is done on a single stage.

3. Early propagation. There are at least 2 cases here: for the first in order to collect mapping from `TweetId` to `[]Username` we need to send collected info directly from `RetweetersReader` to `FinalReducer`; for the second we know from the very beginning that we need to fetch followers for the initial user, so his username should be emitted to `RetweetersReader` bypassing `TimelineReader` stage.

4. Middleware reducers. `FollowersReader` is not only a pipe. It's a reducer for usernames that we've already seen (cause you don't want to duplicate your work).

5. Long running workers. You can't just wait for workers shutdown in many cases, i.e. when you're implementing a server that should respond to many clients simultaneously.

[scala-pmap]: http://docs.scala-lang.org/overviews/parallel-collections/overview.html

[clojure-pmap]: http://clojuredocs.org/clojure_core/clojure.core/pmap

[haskell-book]: http://www.amazon.com/Parallel-Concurrent-Programming-Haskell-Multithreaded/dp/1449335942

[oz-style]: http://doc.akka.io/docs/akka/2.0.1/scala/dataflow.html

[clojure-async]: https://github.com/clojure/core.async

[go-meetup]: http://www.meetup.com/uagolang/events/188657172/

[rob-pike]: http://talks.golang.org/2012/concurrency.slide#1

[clojure-trans]: http://blog.cognitect.com/blog/2014/8/6/transducers-are-coming