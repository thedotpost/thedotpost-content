Conference: dotgo-2016
Tags: golang
Filmed: 2016-10-10
Author: jcinnamond
Image: https://farm9.staticflickr.com/8132/30161637702_8aa93a7355_k_d.jpg
Title: A Look at the Criticism of Go
Curator: sylvinus
Category: backend
Summary: The past decade has seen an explosion of new programming languages, many of them bringing exciting ideas from the research community into the world of mainstream programming. And then there is Go. John looks at why Go is so frequently criticised by the programming languages community, why that might not matter, and how we can all learn from this.
Slides: https://speakerdeck.com/player/66bbc87b98e344889f3fff0b3fd5f697
Video: https://www.youtube.com/watch?v=gHCtEjzZ-rY
Template: talk
Date: 2016-10-25 11:04:29
Status: draft

Full Transcript:


This is an exciting time to be a developer. The last 15 years or so has seen a real explosion in the number of new programming languages. You’re probably all familiar with Go which was announced to the world in 2009; but there have also been a whole host of new functional languages, of new systems languages, of languages to replace things like javascript or php, and other exciting languages. Now for me personally this has been a really exciting time because it’s rekindled my love of the Theory of Programming Languages. In fact I got so excited I started looking around at some postgraduate courses. A lot of Computer Science departments will have a research group which focusses on the Theory of Programming Languages, or something related to that. But when I started looking into it I was really shocked at how much things had changed since my undergraduate days. I kind of assumed that these research groups would look at things such as type theory, or computability, or formal verification. But in fact the main focus of research these days seems to be going onto Hacker News, or Reddit, or social media, and complaining about how terrible Go is. Or at least I presume that’s what these people are doing because that’s what I see a lot of today.


Now, if you look into these complaints they seem to fall into one of two categories. People complain about the simple type system in Go, or they complain about the fact that it reminds them of writing C and they didn’t like doing that. But if you look behind that and look at the actual details of these complains that I think what you’ll find… well actually I think what you’ll find is that these complaints are generally largely valid. Go has got a number of flaws and it could be improved in a number of different ways. But I think if you stop there, and just criticise Go, then you’re missing out on a real opportunity. I think there’s a lot we can learn from Go, and there are a couple of properties in particular that I want to look at today.


The first of these is that Go is really popular. Now, I’m not suggesting that being popular means that it’s a good language - I mean there are some other counterexamples for that. But don’t misunderstand me. I have a lot of respect for Javascript programmers. People build amazing things in Javascript. It’s just that in my opinion they do it in spite of the language, not because of it. I think that Javascript is popular not because the language is great but because for many years it was the only of targeting the browser. Now there’s no such reason for using Go. You don’t have to use Go for anything. In fact the only reason that people seem to use Go is because they like using Go. But that can’t be right, can it? I mean Go has all these of flaws which mean it’s more difficult to develop in. So why are people enjoying using it?


I think that’s an interesting question but there’s [also] another aspect of Go that I think is interesting, and that is that Go is pretty good at writing programs that work. Now I’m not suggesting that every Go program is error free. But in general, compared to other languages, it’s pretty good about producing reliable code. But that can’t be right either, can it? I mean Go’s got all of these flaws which are going to lead to unreliable code. So what’s going on here?


I think this is quite interesting, and more generally I think you could say that in theory Go should really suck, but in practice it doesn’t. And that’s quite interesting. I think there’s an awful learn we can learn about that by looking at Go’s successes. So I think this is an opportunity to learn and this is what I mean when I say that “Complaining about Go is a wasted opportunity.”


But there’s a flip side to this. I think there’s an awful lot the Go community can learn from these criticisms. But this is a difficult thing to do because the people making these criticisms are talking these funny languages like Haskell and Agda and it’s hard to understand what they’re saying. And when you do understand what they’re saying it turns out that they’re just criticism what we do, and that’s hard to deal with. But if we can get beyond that, if we can listen to what they’re saying I think there’s a lot we can learn from that and we can use it to improve Go. And we can do that without losing what’s important to us - what we like about the Go language.


But this is very difficult to do because this is about being more diverse and diversity is hard. But it’s also really important. So I think maybe what we can do is we can try and learn how to listen to other people and hear what they’re saying, and use that to improve what we do. I guess what I’m really trying to say is that we should make an effort to have conversations with people who aren’t like us, and we’ll all be better of for it.


Thanks for listening.