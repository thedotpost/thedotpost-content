Conference: dotcss-2014
Tags: css
Filmed: 2014-11-14
Author: moox
Image: https://farm6.staticflickr.com/5612/15634613859_7e0d36eca3_k_d.jpg
Title: Back to the CSS
Curator: sylvinus
Category: Frontend
Summary: Maxime explains the need for CSS preprocessors in large frontend projects and introduces cssnext, a project that allows us to use CSS specs not yet implemented in popular browsers.
Slides: https://speakerdeck.com/player/a8b246004ec9013264a712c8f4a94aec
Video: https://www.youtube.com/watch?v=bUDcGfuHzJI
Template: talk
Date: 2015-05-06 00:30:57

Transcript of this lightning talk below:

---

I’m sure most of you here love CSS, like I do, but I’m also sure one day, you have been frustrated because you don’t have variables, you don’t have math, you cannot customise colors and stuff...
Because it’s not a programming language and we are still looking sometimes for some similar features that you find in this kind of languages.

We use CSS preprocessors to stop being frustrated. And with preprocessors, we have some new features (@include, @extend and this kind of stuff).

But our website is getting bigger and bigger. The codebase is more complex and we are starting to have a new problem (which is not about the language itself).

It’s about the organisation. What should we do?

There is a lot of people right now that have worked to make new methodologies. For my concern, I was happy with [BEM](http://blog.kaelig.fr/post/48196348743/fifty-shades-of-bem), which helps me a lot to avoid deprecated @include, @extend features, because I found this is not CSS & this can make some crappy code.

Meanwhile the [W3C have worked on a lot of stuff](http://dev.w3.org/csswg/), like [custom properties](http://www.w3.org/TR/css-variables/).
We have variables right now, already available in Firefox. We can make some math too.
We will have [custom media queries](http://dev.w3.org/csswg/mediaqueries/#custom-mq) (soon in Internet Explorer).
We will have [a lot of color manipulations](https://github.com/cssnext/cssnext#features) possible with mainly [the new function color()](http://dev.w3.org/csswg/css-color/#modifying-colors) which allows you to modify and use a lot of modifiers like lightness, alpha, tint, saturation, whiteness, blackness and... (there is too much for my brain so I cannot tell you everything).

There is more, there will always be more selectors (like :matches(), :has()…).
There are new functions (like color()). You will have soon [nesting](http://tabatkins.github.io/specs/css-nesting/) available.

So maybe we can say that we can go back to CSS!
It will be doable and that’s why I’ve worked on a project called cssnext.
cssnext is just css specs.
You can use (with some limitations, for now only one - that does not frustrate me) [css specifications right now](http://cssnext.github.io/cssnext-playground/)!

You can check the website: [cssnext.github.io](https://cssnext.github.io).
You will find some links about the new specifications.
There is a lot of plugins (for you workflow):
[grunt](https://github.com/cssnext/grunt-cssnext),
[gulp](https://github.com/cssnext/gulp-cssnext),
[brunch](https://github.com/cssnext/cssnext-brunch),
[broccoli](https://github.com/cssnext/broccoli-cssnext),
[duojs](https://github.com/cssnext/duo-cssnext)
and it’s even in [Prepros 5](https://prepros.io/) already.

So [give it a try](http://cssnext.github.io/cssnext-playground/). Thanks!