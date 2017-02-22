Conference: dotswift-2017
Tags: Swift
Filmed: 2017-01-27
Author: drewmccormack
Image: https://farm1.staticflickr.com/694/32286401420_18f24607a1_k_d.jpg
Title: The Value in Trees
Curator: dimsumthinking, sylvinus
Category: Frontend
Summary: Swift introduces new ways to model data through value types like structs and enums. Drew discusses his experiences rewriting the data model of the vector graphics app Sketch to use value trees, and finishes off pondering whether future data modelling frameworks could be based on value trees, rather than entities and relationships. To that end, he also introduces the experimental project Impeller [https://github.com/mentalfaculty/impeller](https://github.com/mentalfaculty/impeller).
Slides: http://www.slideshare.net/slideshow/embed_code/key/zrneZ01bq4Mwnr
Video: https://www.youtube.com/watch?v=8jwGDHHLEpI
Template: talk
Date: 2017-02-22 14:0:41

Value types like structs and enums play an important role in Swift development, and have a number of advantages over classes for model data. Because they are generally stored in stack memory, they don't incur the cost of allocation and deallocation associated with heap memory. They also do not have to be garbage collected or reference counted, which adds to the performance benefits.

Perhaps even more important than performance, value types offer greater safety guarantees than mutable reference types like objects. Because each value gets copied when passed into a function or assigned to a variable, each value can be treated in isolation, and the risk of race conditions and other concurrency issues is greatly reduced. The ability of a developer to reason about a value is also greatly enhanced when there is a guarantee it will not be modified via an unrelated scope.

In the talk, Drew tells the story of how the developers of the popular design tool Sketch happened upon a value-based model, even though the app is written entirely in Objective-C. More recently developed Swift apps often also end up using value trees for modeling data.

Concluding that value types — and value trees in particular — are becoming a recurring theme in app development, Drew asks whether they might form the basis of future modeling frameworks, and even introduces such a framework, the new experimental project Impeller [https://github.com/mentalfaculty/impeller](https://github.com/mentalfaculty/impeller). Impeller was inspired by the notion that a persistent store, in the vein of Core Data and Realm, could be based on value types, rather than the usual reference types (classes). Additionally, such a store could be designed from day one to work globally, across devices, much like a DVCS such as Git.
