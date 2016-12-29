Conference: dotjs-2016
Tags: JavaScript
Filmed: 2016-12-05
Author: thomasbelin
Image: https://farm6.staticflickr.com/5496/31115229670_a18b4951da_k_d.jpg
Title: User Interfaces as Pure Functions of Time
Curator: sylvinus
Category: Backend
Summary: Thomas explains how Cycle.js and Functional Reactive Programming can help us define User Interfaces as Pure Functions of Time by trying to model a Lightning Talk.
Slides: http://blog.thomasbelin.fr/talks/dotjs-ui-as-pure-functions-of-time/
Video: https://www.youtube.com/watch?v=9BG0Y3C6WqM
Template: talk
Date: 2016-12-27 14:54:22

To learn more, check out [Cycle.js](https://cycle.js.org/)

### Full transcript:

Let's take a minute to think about what is happening here, at this very moment in this very room.
And because we are developers and we love to model reality, let's try to model a Lightning talk.
To do that, we'll have to forget we are humans for a moment and consider we are programs.
I am a program, you are programs and we are supposed to work together.

Now I, as a speaker, am a function of time.
Depending on time, I produce audio and video.
The audio is, of course, the words I say and the video is the moves I make.

You are functions too.
You are not functions of time directly but rather functions of what I produce.
You are "subscribing" to what I say and "observing" what I do.
So here I am, on stage, emitting sounds, that form words that end up forming sentences and here you are receiving (or not at all) this raw data.

But what exactly is this entity called "you"? How are "you" receiving what I am sending?
Well actually, you are composed of many other functions.
Their job is to convert raw data into another type of data.
Your ears and eyes, for example, are receiving waves and light from me and transforming them into electrical impulses that go right to your brain.
They are independent, functional parts of a bigger function that defines "you".

In this metaphor, I am the user and you are the interface.
If I product a joke for instance, I expect you to laugh.
Just like when your user clicks, he expects the interface to change.
You depend on what I do ... but not only.

You are also receiving a lot of data that comes from all directions: the slides I am showing, the person speaking next to you, your cellphone ringing ... And so on

Just like you, user interfaces do not only depend on what the user is doing.
They also react to server responses, websocket events, timers ending, hardware messages...
And that's the challenge we, as front-end developers, have to face when we build a web interface: handling streams of data that come from multiple sources.
And that's also exactly the problem that Functional Reactive Programming is addressing.

If you pay close attention to the nature of the signals your program receives, there is one common denominator between them: Time.
Time is a key component of our modern web apps.
Time rules everything.
Without time, I produce nothing and you receive nothing either.
Without time, a server does not receive any request from a client.
Without time, an interface does not receive any event from a user.

Functional Reactive Programming adds time as a fundamental input of computer programs. And this changes everything!
You don't need to worry anymore about which parts of your code are asynchronous which parts are not.
You just need to declare a data flow that will convert any input signal into pieces of virtual-dom, http requests, hardware queries... In a word: Side effects.
Now, with that in mind, and probably a little help from Cycle.js, you can start building interfaces as Pure Functions of Time.
