Conference: dotsecurity-2016
Tags: Security
Filmed: 2016-05-22
Author: diogomonica
Image: https://farm2.staticflickr.com/1648/26581522802_b661ff24ad_k_d.jpg
Title: Secure Software Distribution in an Adversarial World
Curator: sylvinus
Category: Security
Summary: As more of our applications become dependent on external modules, having secure software update systems becomes increasingly important. Diogo argues that we should operate under an attack model that considers the distribution infrastructure itself as being actively malicious.
Slides: http://www.slideshare.net/slideshow/embed_code/key/5yiX4z8VwK0wq6
Video: https://www.youtube.com/watch?v=2Dyz8huMfIo
Template: talk
Date: 2016-06-09 16:01:34


Secure software distribution is a hard problem. The thousands of different software update systems in use today, most of which are vulnerable to a myriad of attacks that leave the end users potentially vulnerable to compromise, are a testament to this fact.

With the explosion in popularity of package managers and distributors such as RubyGems, PyPI and npm, more and more of our applications are dependent on small, reusable, modules, developed by thousands of different developers, and distributed by infrastructures outside of our control. Given that distributed systems are only as secure as their weakest link, it only takes compromising one of these modules to be able to compromise the entire infrastructure.

It is time for software developers and publishers to start operating under an attack model that considers the distribution infrastructure itself as being actively malicious, and to start following best practices concerning role responsibility separation, offline storage of signing keys, and routine rotation of signing keys.

Enter Notary, an open-source application built at Docker that aims to make the internet more secure by making it easy for people to publish and verify content. Notary follows a flexible security framework called TUF (The Update Framework), allowing publishers to sign their content offline and manage their keys securely.

Get Notary here: [https://github.com/docker/notary](https://github.com/docker/notary)

Learn more about The Update Framework here: [https://theupdateframework.com](https://theupdateframework.com)