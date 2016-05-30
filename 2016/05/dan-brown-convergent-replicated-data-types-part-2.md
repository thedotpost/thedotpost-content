Conference: dotscale-2016
Tags: CRDT
Filmed: 2016-05-25
Author: danbrown
Image: http://i.imgur.com/jVf1nmB.jpg
Title: Convergent Replicated Data Types, Part 2
Curator: sylvinus
Category: Backend
Summary: Following up on [his talk at dotScale 2015](http://thedotpost.com/2015/06/dan-brown-convergent-replicated-data-types) where he presented the benefits of an eventually consistent "AP" system using CRDTs versus a strictly consistent "CP" system, Dan shares more information about some of the specific data types in the Riak database and how they behave when conflicts occur.
Video: https://www.youtube.com/watch?v=jPfBJo37qm0
Template: talk
Date: 2016-05-27 14:58:11
Status: draft



# Convergent Replicated Data Types /2

Following on from my talk at dotScale 2015 where I presented the benefits of an eventually consistent "AP" system using CRDTs versus a strictly consistent "CP" system, I’d like to share more information about some of the specific data types in the Riak database and how they behave when conflicts occur.

## Distributed Systems

First, a quick reminder of the motivation: In the applications and services we build today, we see more and more benefit in them being distributed. Distributing a system can provide fault tolerance, greater availability and lower latency.

Deploying an application or service in multiple countries means it can be closer to your global user base, making it faster and improving the customer experience. But if your database is distributed across three continents and connectivity between those continents is affected, what do you do?

## AP

An available system can handle this breakdown in connectivity by continuing to accept operations on data and allowing multiple versions of the same value to exist in different places.

When connectivity is restored the system has to decide how to resolve these multiple values. It could keep all the updated values and return them all when a client requests the data, or it could attempt to resolve the conflicts using some resolution logic.

## Resolution

In the first case, the system returns all the values to the client application. The client development team write a merge function which is applied so a single, correct version of the data is available for subsequent requests. No data loss, highly available, correct value.

> ...writing merge functions was likely to confuse the hell out of all our developers and slow down development...

-[http://www.infoq.com/articles/key-lessons-learned-from-transition-to-nosql](http://www.infoq.com/articles/key-lessons-learned-from-transition-to-nosql)

We know it is the correct thing to do as it provides a more available service and allows the use of specific business logic to determine the final value, but it can be difficult to reason about and can slow down development as you write numerous different merge functions.

> ...we found that much of our data could be modelled within sets so by leveraging CRDTs our developers don't have to worry about writing bespoke merge functions for 95% of carefully selected use cases...

-[http://www.infoq.com/articles/key-lessons-learned-from-transition-to-nosql](http://www.infoq.com/articles/key-lessons-learned-from-transition-to-nosql)

Moving this resolution logic from the client back to the system would mean fewer headaches for developers and faster implementation on a wider set of use cases. When this company were first looking at Riak to improve their service availability, data types were a significant factor in them feeling they could model their use cases and data effectively.

## CRDTs

So Convergent Replicated Data Types offer us resolution semantics we can apply to eventually consistent data modelling. They always converge to a single correct value, providing strong eventual consistency and you benefit from the availability and low latency of using a distributed system.

Looking specifically at the types in Riak we have…

### Registers
`{value, timestamp}`
`LWW`

Registers: Used within a map data type (which I’ll cover last) think of them like a single key/value pair, but available within a more complicated data structure, providing greater flexibility for data modelling. Registers are simple and can use last write wins logic to choose the most chronologically recent value. This is ok since the whole map isn’t affected by the use of last write wins, just the register.

```
{
	"name_register": "Dan Brown",
	"famous_author_flag": false
}
```

This is ok since the whole map isn’t affected by the use of last write wins, just the register. In this example, choosing the most chronologically recent change on the register would not affect the value of the flag within the same map.

### Flags
`true / false`
`True > False`

Flags are also used within a map. They have a single true or false value which can be updated independently of the other map values. When true and false values are merged, the flag resolves to true.

```
{
	"name_register": "Dan Brown",
	"famous_author_flag": false
}
```

When adjusting this flag we can update the map without having to re-write the same value to the register; something we would have done before data types were available. Since this particular flag is unlikely to change, a better example may be tracking if a user has opted in to a newsletter or completed an action on a website.

### Counters
`{actor, positive, negative}`
`Non-idempotent PN-counter`

Counters can be used on their own or within a map. A PN-counter keeps track of all increments and decrements that are made by an actor (an actor in this case represents a server within the distributed system) and the value is the difference between the sum of all positives and the sum of all negatives. During merge, the maximum positive and negative values for each actor are used.

```
{
	"name_register": "Dan Brown",
	"famous_author_flag": false,
	"asked_if_author_counter": 21
}
```

Here we’ve added a counter in to our map, although the most common example for counters is probably Facebook or Twitter “likes”.

###  Sets
`add / remove`
`"add wins"`

Sets can also be stored against a specific key or used within a map. Easy to imagine use cases would be your followers list on Twitter, attendees to an event or a playlist on Spotify. Sets support groups of operations, for example adding ElementX and removing ElementY in the same update. They have an “add wins” semantic meaning concurrent add and remove operations on the same element, result in the element being in the set.

```
{
	"name_register": "Dan Brown",
	"famous_author_flag": false,
	"asked_if_author_counter": 21,
	"books_written_set": [],
	"dotscale_events_set": [
		"dotScale2015",
		"dotScale2016"
	]
}
```

### Maps
`allthethings`
`Flags, Registers, Counters, Sets ... and Maps`

Maps can contain all other data types including other maps, giving you great flexibility to expose data structures where previously an opaque binary was being stored. If a field is added or updated and concurrently removed by different actors, the add or update will win during the merge, continuing the “add wins” semantic.

```
{
	"name_register": "Dan Brown",
	"famous_author_flag": false,
	"asked_if_author_counter": 21,
	"books_written_set": [],
	"dotscale_events_set": [
		"dotScale2015",
		"dotScale2016"
	],
	"contact_email_set": [
		"dbrown@basho.com",
		"dan.brown@basho.com"
	]
}
```

Hopefully this has demonstrated how CRDTs or Riak Data Types can be used to build more complex data structures that resolve to single correct values in a highly available, eventually consistent system, all without the headache of writing those merge functions yourself. Thank you.


[http://docs.basho.com/riak/kv/latest/developing/data-types/](http://docs.basho.com/riak/kv/latest/developing/data-types/)