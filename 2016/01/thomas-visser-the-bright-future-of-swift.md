Conference: dotswift-2016
Tags: swift
Filmed: 2016-01-29
Author: thomasvisser
Image: https://farm2.staticflickr.com/1479/24125155124_ae76314602_k_d.jpg
Title: The Bright Future of Swift
Curator: dimsumthinking, sylvinus
Category: Frontend
Summary: With Swift in the open, we can see what is coming for the language. Better built-in support for asynchronous programming is not one of them, yet. Thomas explains how Futures can help you write better asynchronous code now and what Futures could look like if they would be added to the language.
Slides: http://speakerdeck.com/player/d1f4b5a1ec7a483ca686566186acf4e1
Video: https://www.youtube.com/watch?v=vjGvsJv4Wos
Template: talk
Date: 2016-02-17 18:04:32
Status: draft


Now Swift is Open Source, we are able to look further in the future of Swift than ever before. This allows us to see what's coming, the cool things that will allow us to write better code, in Swift 3 and beyond, but also what won’t be coming any time soon. Improvements in support for asynchronous programming is an example of the latter. It is out of scope for Swift 3.

Asynchronous programming is a topic I care about a lot. Enough so that I've written my own implementation of Futures for Swift: [BrightFutures](https://github.com/Thomvis/BrightFutures). Futures provide a powerful alternative to the completionHandler-based APIs we all know. By leveraging the flexibility of Swift, we can make them feel right at home in the language, but built-in support - we can (and will) only speculate about what that will look like - trumps all.

Within the documents that became public when Swift was Open Sourced we can find a proposal showing what it would take to add something like Futures to the language. That is the first step towards a future version of Swift with improved asynchronous programming capabilities. Until then, a third-party Future library will do.

Further reading:
- [http://www.thomasvisser.me/2015/11/26/async-swift/](http://www.thomasvisser.me/2015/11/26/async-swift/)
- [http://www.thomasvisser.me/2015/12/06/async-swift-open-source/](http://www.thomasvisser.me/2015/12/06/async-swift-open-source/)