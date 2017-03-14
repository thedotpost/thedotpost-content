Conference: dotswift-2017
Tags: Swift
Filmed: 2017-01-27
Author: lorentey
Image: https://farm1.staticflickr.com/720/32665458185_86af48f3bb_k_d.jpg
Title: Optimizing Swift Collections
Curator: dimsumthinking, sylvinus
Category: Frontend
Summary: In this talk, Karoly describes several ways to implement the same simple ordered set protocol in Swift, demonstrating how the language supports a number of surprisingly different approaches to programming. At every step, we trade extra complexity for improved runtime performance, ending on an implementation that is ludicrously fast but also quite difficult to handle.
Slides: https://speakerdeck.com/player/92b3584fe5a24da78acc000411883c04
Video: https://www.youtube.com/watch?v=UdZP6JeTCkM
Template: talk
Date: 2017-03-14 11:06:37

The full source code behind the talk is available as a GitHub repository:

[https://github.com/lorentey/OptimizingCollections](https://github.com/lorentey/OptimizingCollections)

The repository includes an Xcode playground with all the data structures presented in the talk. The playground also explains how we can conform all implementations to the Collection protocol—which is something Károly conveniently skipped.

As an extra bonus, Károly included the fun Mac app that he wrote to run benchmarks and to generate the colorful performance plots used in their slides. The app also contains super-secret experimental enhancements to the BTree struct.

For a production-quality implementation of ordered sets (and other ordered collection types), check out my BTree package:

[https://github.com/lorentey/BTree](https://github.com/lorentey/BTree)

Some of the optimizations benchmarked are not yet implemented in this package. If you have time to spare, help him implement them!