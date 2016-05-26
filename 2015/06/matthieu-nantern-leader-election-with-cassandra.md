Conference: dotscale-2015
Tags: paxos, cassandra
Filmed: 2015-06-08
Author: mnantern
Image: https://farm1.staticflickr.com/265/18519450099_c070806357_k_d.jpg
Title: Leader election with Cassandra
Curator: sylvinus
Category: Backend
Summary: In every distributed architecture we need, from time to time, to elect a leader amongst servers. Matthieu explains how to implement a classic leader election with Cassandra. No need to install Zookeeper anymore!
Slides: http://speakerdeck.com/player/4afac5f2aa5c4b66bb3ed7958ee9871e
Video: https://www.youtube.com/watch?v=wBv1CFphR5k
Template: talk
Date: 2015-06-25 13:48:57
Status: draft


Full transcript:

Slide 1:
Today I will talk about leader election with Apache Cassandra.

Since version 2.0 Cassandra offers a new mecanism called lightweight transaction. It is based on "Paxos" a consensus protocol that allows a distributed system to agree on proposals with a quorum-based algorithm, with no masters required and without the [http://the-paper-trail.org/blog/consensus-protocols-two-phase-commit/](problems of two-phase commit). There are two steps in Paxos: prepare/promise, and propose/accept.

Prepare/promise is the core of the algorithm. Any node may propose a value; we call that node a leader. The leader picks a number and sends it to the participating replicas. If the number is the highest a replica has seen, it promises to not accept any proposals associated with any earlier number.
Along with that promise, it includes the most recent proposal it has already received.

If a majority of the nodes promise to accept the leader’s proposal, it may proceed to the actual proposal, but with the wrinkle that if a majority of replicas included an earlier proposal with their promise, then that is the value the leader must propose. Conceptually, if the leader interrupts an earlier leader, it must first finish that leader’s proposal before proceeding with its own. If the responses reported no proposals then the leader can send any value.

But that's not all, in Cassandra we have 2 more steps:
A read/results after prepare/promise to read the value and see if it matches the expected one in the CQL request
A last step commit/ack to insert the data into Cassandra storage

So now that we have seen the theory how to implement leader election with Cassandra ?


Slide 2:
Lightweight transaction can be used with INSERT using the IF clause.

A client acquires a lock by issuing the first statement. If he's the first one the statement is applied and he has the lock. 
If the lease already exists and is held by someone else we get back the information that the statement was not applied.

We can elect leaders with this approach by having nodes that want to become master try to grab the lease on start. Cassandra will return the same result to all clients except for the one that was elected leader.

But remember that the Paxos implementation into Cassandra has 4 steps so it's 4 times slower than an other request.

With that you don't need to install Zookeeper to elect a leader.

That's great but is this really working ?


Slide 3:
Well we can ask Aphyr who is with us today ! He tried Cassandra on 2013 and found several issues with the Paxos implementation.

All of them were resolved so maybe it's time for a new Jepsen ?

Thank you for listening !


Links:
- [http://blog.xebia.fr/2014/12/15/leader-election-avec-cassandra/](Leader election avec Cassandra)
- [http://www.cs.utexas.edu/users/lorenzo/corsi/cs380d/past/03F/notes/paxos-simple.pdf](Paxos made simple)
