Conference: dotjs-2015
Tags: JavaScript
Filmed: 2015-12-07
Author: zeroload
Image: https://farm6.staticflickr.com/5628/23359074800_42c9c7e3e5_k_d.jpg
Title: Authoring and publishing ES6 modules today
Curator: sylvinus
Category: Frontend
Summary: You want to do some ES 2015 before its 2016 but you are afraid: will this run on the many existing JavaScript environments?  What about node.js, 0.10 0.12 4 5, browsers like IE 11, module loaders, script users..  How do you write and release reusable Modules using a syntax that is not yet implemented everywhere? We'll see how
Slides: http://slides.com/vvo/authoring-and-publishing-es6-modules-today-dotjs-2015#/
Video: https://www.youtube.com/watch?v=UJCJ5auXh7o
Template: talk
Date: 2016-01-15 16:30:45

Additional reads:</br>
We are all starting to play with ES6 in our applications and it works well, just plug babel and webpack or browserify and you are good to go.

But what about the modules we use and publish? Most of the time they are written in ES5: its the most compatible version of JavaScript today.

We wanted to be able to author and publish ES6 modules usable by anyone, no matter the setup as soon as they were supporting ES5.

Should you rely on webpack loaders and browserify transforms for your module to work? Nope you can’t, you would limit your module to only a subset of its potential users.

[The solution](http://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/) as other people have found is to publish and expose ES5 transpiled JavaScript for various package managers.

In a near future I hope we will be able to reduce all this boilerplate code so that we can focus on the module code and not the release process.

Nice things takes time to do!