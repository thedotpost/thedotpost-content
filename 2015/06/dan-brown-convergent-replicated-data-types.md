Conference: dotscale-2015
Filmed: 2015-06-08
Author: danbrown
Image: https://farm1.staticflickr.com/529/18518051750_46bdf7962f_k_d.jpg
Title: Convergent Replicated Data Types
Curator: sylvinus
Category: Backend
Summary: Convergent Replicated Data Types offer a principled approach to eventually consistent data modelling, with defined data types always converging to single correct values. CRDTs are one of the key building blocks of a distributed system, enabling strong eventual consistency and highly available, low latency applications.
Video: https://www.youtube.com/watch?v=eeZUWJDWCNE
Template: talk
Date: 2015-06-25 14:03:11
Status: draft

# Convergent Replicated Data Types in Four Minutes

First a motivation. When building an online service or application, there are certain behaviours you want it to have. Being “online” is likely to be a key behaviour. Put another way, availability of a service is crucial for customers to access it. If it is unavailable, it is not serving it’s purpose. When a service you want to use is unavailable, you may look for a permanent alternative.

## Fault Tolerance

How can we prevent failure to avoid this unavailability? It turns out that is really hard, so we focus on building systems that tolerate forms of failure. Common design patterns have us build distributed systems, using redundancy of hardware, software and data, to ensure common failures within the service don’t impact overall service availability.

## Low Latency

Slow services are just as bad. Please wait, spinning loading wheels or a complete lack of feedback to the end user all result in frustration and the chance of the user abandoning their objective. Latency costs money; companies like Amazon and Google have data to prove it. High latency can be indistinguishable from failure.

## Distributed Systems

Building a distributed system allows us a level of fault tolerance to increase availability. It gives us other properties like the ability to deploy the service closer to the users. Geo-replication of data allows a smaller distance between client and server, thus reducing latency.

But there is a trade-off when building a distributed system. Distributed systems have to make choices during failure states.

## CAP

Eric Brewer conjectured that there are 3 desirable properties in any distributed system: consistency, availability and partition tolerance, and at any one time you can’t have them all. But this has lead to confusion and A LOT of debate. Too much to dive in to in this talk.

## CP <- - -> AP

Consistency and availability are what we adjust in our trade off. If you require consistency in the face of partitions, then you lose some ability to be available. Being unavailable costs money. If you choose availability, you need to relax consistency. Even when a distributed system is not in a partitioned state you trade consistency for latency. Consensus -which you need for consistency- costs latency. And latency costs money.

## CP

In a partitioned state a consistent system must decide how to prevent inconsistency in any replicated data. A common way is to have a “majority wins” approach where the minority of servers refuse operations until the partitioned state is resolved.

## AP

An available system can handle a partitioned state by still accepting operations on data and allowing resolution of any inconsistency once the partitioned state is resolved. The data is eventually consistent when all replicas converge.

## Eventually Consistent Resolution Strategies

So let’s look at some resolution strategies.

### LWW

A last write wins (or all other writes lose) strategy is one way to converge on a single version for all copies of a value in a distributed system. But what are you losing by dropping those other versions? Ignoring clock skew for a moment, you can’t even be sure the last write saw earlier writes from other clients. This is data loss.

### Semantic Resolution

Another strategy is storing multiple versions of the datum and using semantic resolution. Use the semantics of the domain to define a path to a single value. An example being union operation that takes two divergent copies of a value and creates a single consistent version. But this passes the pain to the developer to build ad-hoc resolution strategies for the use case at hand.

### CRDTs

What if someone built a series of reusable data types for you? Convergent Replicated Data Types are those data types, and offer a principled approach to eventually consistent data modelling. Some very cool maths ensures these defined data types always converge to a single correct value.

CRDTs can be considered one of the key building blocks of a distributed system, enabling strong eventual consistency and a highly available, low latency application.

Further reading: [Readings in conflict-free replicated data types](http://christophermeiklejohn.com/crdt/2014/07/22/readings-in-crdts.html) by Christopher Meiklejohn.