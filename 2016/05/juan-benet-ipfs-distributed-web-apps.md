Conference: dotscale-2016
Tags: IPFS
Filmed: 2016-05-25
Author: juanbenet
Image: https://farm2.staticflickr.com/1532/26593579021_7b9d58b4be_k_d.jpg
Title: IPFS: Distributed Web Apps
Curator: sylvinus
Category: Backend
Summary: Juan presents his project IPFS (the InterPlanetary File System), a new hypermedia distribution protocol, addressed by content and identities.
Slides: https://speakerdeck.com/player/930adec374974bacbd3c8f24d6ba1b7d
Video: https://www.youtube.com/watch?v=_qzPUlNoC0E
Template: talk
Date: 2017-01-13 15:21:56
Status: draft


# IPFS: Distributed Web Apps @ dotScale 2016

[This is a transcript of Juan Benet's talk on 2016-04-25 at dotScale, in Paris. It is almost word-for-word.]

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-001.png" style="width:100%;height:auto;"/>

Before I start, take a look around. Isn't this an amazing venue? This is an amazing theater. So please, a huge round of applause and thanks to the dotScale team because this is one of the best conferences I've ever been to.

[APPLAUSE]

Computation is about functions. Functions are encoded. And Code is data.

So computation is about data. How data moves, how it transfers in the network, what properties it has, how fault tolerant that system is, has _vast_ implications on what our computation can do, what our software does, what our applications do, and therefore, what we as humans are capable of doing. Because, for better or for worse -- really for better -- software is becoming -- has already become -- our superpower. We can do amazing things today that 30 years ago were absurd. This is because of our computation platform. And thus, how we _move_ that computation really matters, in a deep ethical way, and I'm here to talk to you about that.

There's a lot of problems, right? It makes sense to talk to you, the engineers, and developers, and designers of the Web, the architects that are constructing how this network operates. There are problems you need to be aware of, Solutions you may employ to fix them, and I want to tell you about one possible solution that we're working on. That's IPFS -- the InterPlanetary File System.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-004.5.png" style="width:100%;height:auto;"/>

So, in the days of yore there was packet switching. This is Paul Baran's classification of networks, from centralized, to decentralized, to distributed. And these have very different properties. Centralzied networks are very easy to take down, but they are very easy to work with; it is very simple to upgrade the thing, and so on. Distributed networks are much more fault tolerant, but are way harder to build.

The Internet is this amazing nervous system we all share. We can ship around our computations and our data to each other, and has made it possible for me to speak to you around the world in less than a second. It's incredible. And the Web is truly how we humans use the Internet. We don't speak encoded byte-streams, so we have to use applications on top of the Internet. These applications today govern most of our lives, and how the web is structured has deep implications on how these applicatiosn behave, and how our superpowers work.

The web is Sick. The web is Sick with Centralization. This is a disease. It started kind of simple, you have one server serving a bunch of clients, but then it grows to one massive web server serving billions of users. And in reality we all know that the one massive web server is truly a massive distributed system behind the scenes. But it all goes to this one choke point, which means that you, your clients, your mobile phones, and so on, _have to_ talk to the backbone. So this has deep implications on how we use the network.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-006.5.png" style="width:100%;height:auto;"/>

First off, it is obviously terribly inefficient. If you all loaded Gangam Style right now and had to download the same video you would peg the bandwidth of the entire uplink from here to there, and we would waste a ton of bandwidth. Why can't we be more efficient about this. Gangam Style has been viewed about 2.5 Billion times, and if you take the average sized video to be 200 MB, that's roughly 512 Petabytes -- this is totally back of the envelope, probably not right -- but this gives you the scale, the magnitude that we're talking about.

The web is basically kicked out of mobile, and not present in all the IoT stuff. Mostly because it just doesn't make sense-- it doesn't make sense to have to talk to a centralized server all the time. It doesn't work offline. It doesn't work in disconnected networks. Think about my supercomputer, in this pocket, this thing is incredibly powerful. Why can't I send a message to your computer right there. I just want the message to go from here, to there. This doesn't work today; it doesn't work very efficiently. Most of these applications force you to mediate all the transfers through the backbone.

The Web also has a terrible security model, in my point of view. Aside from the massive breaches, and the mass surveillance, and so on, there is a deeper problem. Even if we forced everyone to encrypt with TLS, the data itself is not encrypted at rest, or it's not even authenticated. So you can have all your email and all your social networking information, and someone on the server side could sneak in there and change it, and you wouldn't even know. Suddenly you could find old emails that "you wrote", theoretically, without any kind of signature. We've known about encryption and digital signing for many decades; we should know better. We should be working with these primitives in a much better way. I would love to get the web to be authenticated and encrypted at rest.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-008.5.png" style="width:100%;height:auto;"/>

There is also a point about data control. Here Europe is way far ahead than the US in thinking about this. There's these massive social networks that are gathering a ton of data, and making it possible for me to send a message to the world and for anyone in the world to send a message back to me -- and that's incredibly powerful and amazing. But these databases are not really ours. They're governed by these organizations, and the addresses to the resources always go through them. So if I want to link you to a Tweet, I have to link you through the applicaton they govern, there's no way to link to the data itself.

This one is particularly infuriating. The Internet is this amazing force for equality. It gives people equal access to knoweldge, equal access to communication, and so on. And the Web was like that for a while. But nowaddays with websites being Megabytes in size, or webservers cutting connections that have too bad latencies -- it happened to me, if your latency goes above 6 or 7 seconds a lot of webservers won't even talk to you. You may not even complete TLS handshakes. _That_ is a disaster, because we're blocking the people who need the Web the most. And that is, in my point of view, inexcusable and we need to fix it.

And even in the nice metropolises with fountains of data, natural disasters can occurr, so what happens when a network has no, or bad, connectivity to the backbone, but the local network still works? In many cases you can get realiable local connectivity, or you can deploy mesh networks, but the uplink may be off. So why is it that we can't make our communication systems operate in situations like these? What happens today is "oh, sorry, error. Try again later." Imagine that you're trying to find your family. It gets worse when it's about human disasters, when suddently there's massive censorship or "suprise oppression": one morning you wake up and your access to the internet is off. You can't talk to anyone. _That_ is not okay.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-011.5.png" style="width:100%;height:auto;"/>

The last problem I'll mention is that Links Break and sites disappear, beacuse this idealized web of documents is really a web of documents on specific machines. And this is like a book burners' paradise because all you have to do is take one server down. Or worse, we just carelessly change URLs all the time -- we don't even think about it, we just break tons of links and people's access breaks at that point...

So hopefully I've impressed upon you the weight of the matter here. These are serious issues that our society has to deal with. They don't enter our field of view most of the time. Beacuse you're focused on your application, on getting to the next thing, building the next cool feature, and deploying it, and so on. After all it's not your Threat Model to deal with situations like that. But whether or not it is your model, people are using your applications and they are depending on them. The amazing superpower you gave them -- with this beautiful piece of software -- they start depending on that superpower. And at any point whenever that superpower doesn't quite work right, or breaks, or you move on and stop maintaining it -- that is breaking a social contract that was implicit in the giving of the software.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-012.5.png" style="width:100%;height:auto;"/>
<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-015.5.png" style="width:100%;height:auto;margin-top:10px;"/>


A lot of these problems stem from the addressing model. When you think about the Web and how you point at all the content, you always point in terms of domain names and IP addresses. Names and Location. And you have to be Online to resolve all of this. It's a little bit like, imagine if I told you to go read a book, but my directions for reading the book were: go to a specific library, at a specific location; go and find this book there, and you couldn't go anywhere else to read this book. That's kind of crazy, right? It made a lot of sense at the time, it made the web scalable. But now we're in this bad situation where this is a very strong force for centralziation, and it makes it very difficult for us to build decentralized or distributed alternatives. It looks like this, even if a lot of people have the content they can't serve it to you.

So there's good news. The good news is that the hard part of building the internet is over. We wired up a lot of the world. There's still much more to go, but at the very least we have this amazing platform that we can deploy software updates to. And all it takes is new protocols and new code to fix things. And applications themselves are relatively easy to fix. So, you -- one of the things I want to impress upon you is that -- you _can_ fix this. You have the power to do this. It's kind of daunting to think "changing the entire internet", right? But all you need is to think about good ideas, and turn those into specs, create some implementations, and deploy them. And if they're good, you will grant humans more superpowers. It's the same thing you do with an application, but you can do it at the internet level. This goes from research, to development, to deployment and so on. It turns out that many of these problems have been fixed in the past, but the pipeline from Research to Usage is bad. Most of the Research never gets used. We need to fix this as well. This is another problem... but, different talk.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-018.5.png" style="width:100%;height:auto;"/>


I'll talk about Git a little for a little bit, and then I'll dive into IPFS. I wanted to impress upon you the magnitude of the problems because that's really what IPFS is about. It's solving those things. That's far more important for you to understand than the technical details. But, let's dive in.

We all understand Git to a good degree. In the good old days of CVS/SVN we had a centralized server, we had to talk to this one machine. And if you got disconnected from it, you couldn't work. If that thing went down, nobody could work. Git came in and solved the problem saying "no no no, this is madness, let's do distributed version control, have many servers, many clients able to talk to each other" If you get disconnected it doesn't matter, you can still work individually, you can still talk to others. You know, Honey Badger Don't Care. If the central things fall appart, still doesn't matter -- honey badger don't care -- you can still work, you can talk to each other, you can setup a new one, it's not a big problem. It's annoying but not a big problem. IPFS is about taking this type of approach and making it work across the entire web. It's what I like to call Hyperspeed, because it allows you to cheat the speed of light-- you might have the content locally.

And the whole reason Git is able to do this is because it merkle-links objects. One object is linked to another through its cryptographic hash. That makes it so that anyone can serve it to you, and you can check the integrity. So you can think of this chain of documents, of being able to verify all of these links. Another amazing development is CRDTs -- Conflict-free Replicated Data Types. This is an amazing development. Not enough time to cover it here, but wanted to point it out, because if you don't know about these, go find out. Huge deal. Still early days, but these are going to change how we build all applications.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-021.5.png" style="width:100%;height:auto;"/>

The other thing I'll mention is the explosion of a new wave of Peer-to-Peer 2.0 type protocols. It all started with Bitcoin, and reminding us that we could build distributed systems, reminding us that we can do transactions a different way, that we can cede control to the network and beahve as part of it. Ethereum took that up a notch by being able to do any kind of computation through it. And now we're starting to see the first kinds of applications of these networks on top of these. Things like OpenBazaar, a full ebay-like store system where you can sell anything, that works completely distributed and decentralized, uses Bitcoin as a payment system, and all of the content is accessible through the network and there is no central point. You can add central points to improve the performance, to optimize, but never as a point of control or failure.

If we were to categorize the Web in the 1.0 world, we just took the internet and we added the ability to point at data. In Web 2.0 we pointed at programs and had those programs run and manipulate the data. If I were to categorize Web 3.0, it's an inversion of the relationship, where data links to data itself or programs, and they operate with public verifiability, so that no organization, no entity can manipulate those results. Or that you don't depend on people. It's massive disintermediation.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-025.5.png" style="width:100%;height:auto;"/>

So maybe we can use these ideas to structure a better web. To link the web in a stronger way. To improve our system. Let's make the web faster, safer, operate in a distributed way, have permanent links, and work offline. So that's what IPFS is about. It's creating a new Hypermedia distribution protocol. That's just a fancy way of saying: a new transport for the Web. That uses merkle links as its core idea.

This is the stack of the protocol. It's broken up into different pieces. The bottom part -- which is the hardest thing to do -- is to build all this peer-to-peer software. Lots of p2p protocols that you have to think about and use, being able to connect locally, being able to deal with DHTs, being able to deal with pubsub, and so on, all these different kinds of transports, being able to be inside of a browser sandbox and being able to talk to the rest of the network, and so on. That is probably the hardest part, and we're creating a library around all that so you will be able to build all sorts of peer-to-peer systems out of it. When you think about IPFS you really think about a bunch of peer-to-peer protocols inside of this one node, and some really nice interfaces to just add and retrieve content by hash.

This core part of IPFS is the web of merkle-links. Think about structuring data, it has the same kind of properties as git, bitcoin, and bittorrent, and so on. And think of IPFS as this huge merkle-forest. So if individual trees that are merkle-linked are one tree, then you can think of blockchains as this massively tall tree, and you should be able to link between all the things. Naming, applications, and so on layer on top.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-029.5.png" style="width:100%;height:auto;"/>

The addressing model looks like this. At the bottom layer you have Content Addresses, those are immutable and get changed whenever you change the content. But those are dependable forever. You don't have to be around, servers don't have to be around, those are truly dependable. The next layer is naming with keys, there's a bunch of interesting stuff around that, but won't have time to cover it. And there's Human Readable Names on top that you can bind. These should be bound at the end, not as the core part that you depend on.

When you think of adding content to IPFS you can think of a file system, that maps directly to how Git does it, with merkle-linking. You hash contents, and take that hash put it as the link from a directory, and so on all the way to the root. So you have the ability to address and Path nicely as you would expect in the Web or in a file system. You can do more complciated stuff, like versioning data structures. It doesn't have to be a file. IPFS is not about files, even though it's a "file system". It's about data, and structuring realtionships between data. Think about a git commit and apply that to anything, not just files. You could `git commit` a version of your edits to a song or something. And so think about just accessing IPFS data through an interface like that.

So, you take the data model that is right now locked up in your databases, and just rip it open and spread it into the web. That is what we can do. You can address all the content directly. You don't have to depend on those organziations. You don't have to depend on those pieces of software. You can reason about how the content moves, how the syncs happen, and so on, to make offline possible. You can do things like have the whole PKI -- all the Certificate Authority stuff, all the certificates and so on -- put them on IPFS and all you need is one root hash and from it you can retrieve signatures, certificates, keys to validate stuff, and so on.

IPFS is about giving information "print-like qualities", where the references are to the work, and not to the physical location of a copy.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-032.5.png" style="width:100%;height:auto;"/>

This is the IPFS stack, it's about that central point -- how we represent data. It's a huge open source project. It has hundreds of contributors. It is very high velocity. This is really a call to you, to come and help us, and help build it. Because how we lay out this foundation now can have vast implications for you in the future and it would be fantastic to get your input now. There's a huge network, here's the kind of stuff that people build, distribution platforms, peer-to-peer chat, archives, totally distributed webapps. You can find all of this stuff on the web -- I don't really have to go through it here, just know you can build things like totally distributed chat applications entirely on IPFS. You type, enter stuff, each individual message is an object you can address. You can create new interfaces to access the same data. You can use it for package managers, so when you think of package managers being centralized and that being a problem. You can think of putting npm on ipfs, or a Go package manager. All these are projects that we have.

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-034.5.png" style="width:100%;height:auto;"/>


All right. That's really all I wanted to say about IPFS and about the network, and if I would end with one word it is this: Think carefully about the implications of the software you create, because whether you want it or not, people depend on the software you write, and depend on the failure modes that you create. So when you give somebody an amazing superpower, and you make it really good, and they start using it and depending on it, you will have to deal with that social contract you created. If you break that, bad things can happen.

Thank you, that's it.

[APPLAUSE]

<img src="https://ipfs.io/ipfs/QmbMSxDagNYR5Mzo8uReDbLaSGNzUAtrnNFdV3UhhRUTZP/dotScale-ipfs-035.5.png" style="width:100%;height:auto;"/>