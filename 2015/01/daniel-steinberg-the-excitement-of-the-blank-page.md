Title: The excitement of the blank page
Status: draft
Template: article
Date: 2015-01-20
Author: dimsumthinking
Category: Humans
Summary: Daniel explains how Swift makes 2015 a tremendously exciting year to be writing iOS and OS X apps.
Image: https://farm4.staticflickr.com/3017/2926876465_3d658d5ac9_b_d.jpg
ImageCredit: https://www.flickr.com/photos/lyre/2926876465

Nearly twenty years ago Java was the new language the cool kids were playing with.

Kind of hard to picture, isn't it.

Then again, I suppose there was a time in the early sixties when the cool kids were kicking the tires on COBOL.

Anyway, back to Java. There's a wonderful <a href="http://www.artima.com/intv/gosling1P.html">interview</a> that Bill Venners did with James Gosling. Gosling is known as the father of Java.

Venners asks Gosling why he created Java. "When," he asks, does it make "sense for developers to develop a tool to solve a general case, as opposed to solving the specific problem in front of them?"

Gosling eventually replies, "Programming languages are a really dubious thing to create. I've done a lot of them, and they can be really good solutions to all kinds of problems. But they come with a learning curve infrastructure problem that can make them pretty difficult. And, actually, in the Green project I wasn't real happy about going off and doing a new language. It started out with me not trying to do a new language, but trying to fix some underlying issues in C++ that were not so much C++ the language, but C++ the compiler."

It wasn't tough to learn Java the language. Learning the libraries, the design patterns, and the best practices was something else entirely.

In addition, we didn't have nice IDEs for Java in those days. We wrote code in a text editor and compiled code from the terminal using javac. I know that that's not exactly submitting a stack of punch cards to be run, but we had to wait minutes for our code to compile.

Java was a language written by geeks for geeks.

My favorite feature was that when the garbage collector ran, an animation appeared of a bulldozer pushing dirt into a pile. That's right, end users could see when the garbage collector was being run. It wasn't much of a secret as our program screeched to a halt while the collector ran.

Swift is also a language written by geeks for geeks.

These are the folks that worked on LLVM and the Clang. And yet it feels different. It feels as if the people who created and are growing Swift understand that we have to ship software today while helping to transition us to the platform on which we'll ship software for years to come.

"But," you say, "Swift doesn't do everything I want the way I want it to."

No it doesn't. It's still early days.

This weekend I read a <a href="http://www.phoefsutton.com/bertram-millhauser/">blog post</a> by Phoef Sutton. He writes movies for a living and he was arguing that movie writers are way underappreciated.

"Everyone," he wrote, "from the actor to the director to the set designer has something to work from, a script. Even if it’s a truly rotten script. But the writer? He has nothing but his imagination and time."

Whether I'm struggling to write code or prose, it's always a good idea to just get something written. Then I can fix it. Once we have code written down we can improve it. When there's no code, there's nothing to work with.

I'm really looking forward to this year. I'm expecting some changes in the language and some changes in the library.

Imagine the people in charge of creating and growing the Swift Standard Library. They are running smack into the limitations of the language. And those of use writing code in Swift are running head first into the limitations of the library.

These experiences will help inform each other. Our limitations are pointing to the things we need - or think we need - from the standard libraries. I'm expecting a rethinking of Foundation. Does NSDate really need to be a class? Can't this small immutable wrapper around a Unix time stamp be reimplemented as a struct?

The people in charge of the Swift library can't do everything they want to because of the limitations of the language.

The language architects and implementers need to wade through this river of requests and decide which enhancements will take the language in the right direction and which will open a door that can never be closed.

I think this is a tremendously exciting time to be writing iOS and OS X apps. Our future is Swift. But Swift may not be what you think it is.

It's easy to learn the language and much of the standard library. I teach a class that does it in a day.

But it's going to take us a while to learn the subtleties of the language. What is it good at? How do we use it to our advantage? What are the design patterns? What are the best practices?

I love that we're on this journey together. I've already learned so much from this community. For me, there's a vibe - an excitement - that I haven't felt about a language in nearly twenty years.

_Excited about Swift? Daniel will speak at [dotSwift](http://dotswift.io) in Paris on February 6th!_
