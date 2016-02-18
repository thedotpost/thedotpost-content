Conference: dotswift-2016
Tags: swift
Filmed: 2016-01-29
Author: chriseidhof
Image: https://farm2.staticflickr.com/1523/24635121582_2502465b89_k_d.jpg
Title: Tiny Networking in Swift
Curator: dimsumthinking, sylvinus
Category: Frontend
Summary: Chris looks at how we can take standard networking code, and use Swift's features to make it generic and simple. While live-coding, he factors out common parts into a struct, so that the resulting code is easy to test and highly reusable.
Video: https://www.youtube.com/watch?v=ewk-XNzXzAA
Template: talk
Date: 2016-02-17 10:12:27
Status: draft

Chris' comments:

I try to make the the case for creating a simple wrapper around networking code. Rather than having a lot of asynchronous code (which is hard to test), I try to minimize the asynchronous part and instead use generics and structs to make it simpler and more testable.

I took this code from an existing app we wrote in production, and wrote a blog post about it in 2014: [http://chris.eidhof.nl/posts/tiny-networking-in-swift.html](http://chris.eidhof.nl/posts/tiny-networking-in-swift.html). In my recent book [Advanced Swift](https://www.objc.io/books/advanced-swift/), we go into more detail explaining these techniques. Over the last years, a number of companies have used a variant of this library in production, and are quite happy with it.

After watching the talk, you'll see that there are a number of things that can be improved: how to parse other things than JSON? How can you make it asynchronous? How can you handle POST requests? I hope that you take these challenges, and see if you can add these features. It'll be lots of fun!