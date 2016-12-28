Conference: dotgo-2016
Tags: Golang
Filmed: 2016-10-10
Author: simonecarletti
Image: http://i.imgur.com/h4oP9LH.jpg
Title: Using Go to Guide API Design Decisions
Curator: sylvinus
Category: Backend
Summary: Two years ago, the DNSimple team started a major redesign of their public API, and the Go language played a key role in the process. Simone explains why Go was so important to them and why it was used to guide the development design decisions.
Slides: https://speakerdeck.com/player/fc2cc1c53efc4d7ab9682305bcde4f0e
Video: https://www.youtube.com/watch?v=NWNEjC4Y4X4
Template: talk
Date: 2016-12-23 14:47:38
Status: draft


Two years ago, at DNSimple, we started to redesign our HTTP API, along with official clients for several languages.

For weeks I developed in parallel in 3 different languages: Ruby, Elixir, and Go. The more I was writing code, the more I was realizing that for some reason the Go client was leading the development. In fact, the common approach was to develop a feature in Go, and then in other languages. It turned out it was not a coincidence.

In this lightning talk you'll discover why Go was so important to us and why we used it to guide our development design decisions. Thanks to Go we were able to come with a simplified and standardized approach that so far worked extremely well in any other language. Go had a major impact on our decisions and success.

If you are planning to work on a project that should interact with several languages, then consider to use Go as your leading language.

The API v2 documentation is available at:
[https://developer.dnsimple.com/v2/](https://developer.dnsimple.com/v2/)

The API clients, whose design was influenced by Go, are available at:
- [https://github.com/dnsimple/dnsimple-go](https://github.com/dnsimple/dnsimple-go) (Go)
- [https://github.com/dnsimple/dnsimple-elixir](https://github.com/dnsimple/dnsimple-elixir) (Elixir)
- [https://github.com/dnsimple/dnsimple-ruby](https://github.com/dnsimple/dnsimple-ruby) (Ruby)
- [https://github.com/dnsimple/dnsimple-node](https://github.com/dnsimple/dnsimple-node) (Node.js)
- [https://github.com/dnsimple/dnsimple-java](https://github.com/dnsimple/dnsimple-java) (Java)