Conference: dotjs-2015
Tags: JavaScript
Filmed: 2015-12-07
Author: mafintosh
Image: https://farm1.staticflickr.com/585/23360518920_af66bdf1d2_k_d.jpg
Title: Hyperdrive, a P2P filesharing network
Curator: sylvinus
Category: Frontend
Slides: https://github.com/mafintosh/slides/blob/gh-pages/dotjs-2015/README.md
Summary: Mathias introduces Hyperdrive, a BitTorrent-style file-sharing network written in JavaScript. It is based on techniques such as rabin file chunking and merkle trees to ensure only the diff of a file is shared when it is updated.
Video: https://www.youtube.com/watch?v=vTHRHWIacI0
Template: talk
Date: 2016-03-23 15:52:04
Status: draft


[Hyperdrive](https://github.com/mafintosh/hyperdrive), is a JavaScript library that allows you to distribute feeds of binary data to multiple peers on the internet. It was developed to be the main data and file distribution layer for the [dat project](https://dat-data.com). It works both in the browser using browserify or in node.js.

On a technical level it works in a similar way to BitTorrent. You can use Hyperdrive to distribute any kind of dataset or just to do classic file sharing with multiple peers where every peer is helping share the data.

This talk starts out with a short technical overview about how Hyperdrive works, including:

* Diffing - Given two version of a file how do you figure out which parts has changed?
* Deduplication - How do you make sure a single file is only downloaded once even though it is shared multiple times in different feeds?

At the end of the talk you'll see live demos, using a Hyperdrive build in the browser, to share CSV files, pictures and videos.

If you're interested in learning more about the low level details a full technical explaination on how it works can be found here: [https://github.com/mafintosh/hyperdrive/blob/master/SPECIFICATION.md](https://github.com/mafintosh/hyperdrive/blob/master/SPECIFICATION.md)
