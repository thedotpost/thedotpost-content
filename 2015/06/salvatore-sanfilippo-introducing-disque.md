Conference: dotscale-2015
Tags: disque, redis
Filmed: 2015-06-08
Author: antirez
Image: https://farm1.staticflickr.com/493/18521479780_3329e1e1a2_k_d.jpg
Title: Introducing Disque
Curator: sylvinus
Category: Backend
Summary: Salvatore introduces a new open source message broker with a simple API and explains the motivations and the fundamental design choices that lead to Disque’s AP design with synchronous replication and optional persistence, enabling guaranteed message delivery and fault tolerance.
Slides: http://antirez.com/misc/DotScale2015.pdf
Video: https://www.youtube.com/watch?v=GRuFG7QVvCY
Template: talk
Date: 2015-07-02 08:15:11

Check out the [Disque Github repository](https://github.com/antirez/disque/)!

Disque is an ongoing experiment to build a distributed, in memory, message broker. Its goal is to capture the essence of the "Redis as a jobs queue" use case, which is usually implemented using blocking list operations, and move it into an ad-hoc, self-contained, scalable, and fault tolerant design, with simple to understand properties and guarantees, but still resembling Redis in terms of simplicity, performances, and implementation as a C non-blocking networked server.

Disque is a **synchronously replicated job queu**. By default when a new job is added, it is replicated to W nodes before the client gets an acknowledge about the job being added. W-1 nodes can fail and still the message will be delivered.

Disque supports both **at-least-once and at-most-once** delivery semantics. At least once delivery semantics is where most efforts were spent in the design and implementation, while the at most once semantics is a trivial result of using a *retry time* set to 0 (which means, never re-queue the message again) and a replication factor of 1 for the message (not strictly needed, but it is useless to have multiple copies of a message around if it will be delivered at most one time). You can have, at the same time, both at-least-once and at-most-once jobs in the same queues and nodes, since this is a per message setting.

Disque at-least-once delivery is designed to **approximate single delivery** when possible, even during certain kinds of failures. This means that while Disque can only guarantee a number of deliveries equal or greater to one, it will try hard to avoid multiple deliveries whenever possible.

Disque is a distributed system where **all nodes have the same role** (aka, it is multi-master). Producers and consumers can attach to whatever node they like, and there is no need for producers and consumers of the same queue, to stay connected to the same node. Nodes will automatically exchange messages based on load and client requests.

Disque is Available (it is an eventually consistent AP system in CAP terms): producers and consumers can make progresses as long as a single node is reachable.

Disque supports **optional asynchronous commands** that are low latency for the client but provide less guarantees. For example a producer can add a job to a queue with a replication factor of 3, but may want to run away before knowing if the contacted node was really able to replicate it to the specified number of nodes or not. The node will replicate the message in the background in a best effort way.

Disque automatically **re-queues messages that are not acknowledged** as already processed by consumers, after a message-specific retry time. There is no need for consumers to re-queue a message if it was not processed.

Disque uses **explicit acknowledges** in order for a consumer to signal a message as delivered (or, using a different terminology, to signal a job as already processed).

Disque queues only provides **best effort ordering**. Each queue sorts messages based on the job creation time, which is obtained using the wall clock of the local node where the message was created (plus an incremental counter for messages created in the same millisecond), so messages created in the same node are normally delivered in the same order they were created. This is not causal ordering since correct ordering is violated in different cases: when messages are re-issued because not acknowledged, because of nodes local clock drifts, and when messages are moved to other nodes for load balancing and federation (in this case you end with queues having jobs originated in different nodes with different wall clocks). However all this also means that normally messages are not delivered in random order and usually messages created first are delivered first.