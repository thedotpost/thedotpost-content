Conference: dotcss-2014
Tags: css, sass
Filmed: 2014-11-14
Author: hugogiraudel
Image: https://farm9.staticflickr.com/8265/15820030305_132af531b7_k_d.jpg
Title: Keep Calm and Write Sass
Curator: sylvinus
Category: Frontend
Summary: In this talk, Hugo gives us some "do's and don'ts" when it comes to writing Sass code, as well as a couple of resources to get things started.
Slides: http://www.speakerdeck.com/player/117e5ae04f2501329d875e31c290001e
Video: https://www.youtube.com/watch?v=WHMFaN-Qaxo
Template: talk
Date: 2015-04-04 14:19:17


Here are the links to the tools and articles addressed in Hugo's talk:

- [Your CSS is a Mess](http://vimeo.com/99877232) from Jonathan Snook
- [Keep Sass Simple](http://www.sitepoint.com/keep-sass-simple/)
- [Beware of Selector Nesting](http://www.sitepoint.com/beware-selector-nesting-sass/)
- [Rethinking the Atwood law to apply it to Sass](http://hugogiraudel.com/2014/10/27/rethinking-atwoods-law/)
- [SassyJSON experiment](https://github.com/HugoGiraudel/SassyJSON)
- [SassySort experiment](https://github.com/HugoGiraudel/SassySort)
- [SassyBitwise experiment](https://github.com/HugoGiraudel/SassyBitwise)
- [Autoprefixer](https://github.com/postcss/autoprefixer)
- [px_to_rem](https://github.com/songawee/px_to_rem)
- [CSSGuidelines](http://cssguidelin.es) from Harry Roberts
- [scss-lint](https://github.com/causes/scss-lint)
- [SassDoc](http://sassdoc.com)
- [True](https://github.com/ericam/true) (Sass testing framework)
- [Bootcamp](https://github.com/thejameskyle/bootcamp) (Sass testing framework)

Full transcript below:

---

A couple of days ago, someone told me: "try not to annoy people too much with your talk", so *challenge accepted*. We'll try to do something nice.

So, want to talk about Sass but I don't want to bring another introduction. We have way too many of them. Too many articles, blog posts, screencasts and everything. So today I would like to present you some "do's and don'ts" of writing Sass code.

A couple of years ago, Jonathan Snook presented a talk called [Your CSS is a mess](http://vimeo.com/99877232). Great talk by the way. I think, the *your* is optional. (The line is quite thin but the *your* is actually striked-through.) So CSS is kind of a mess at a whole level.

It's not that it's been broken from the start. It's not that CSS is poorly designed. It's just that it wasn't meant to do such complicated stuff. When it was designed 20 years ago, CSS was meant to style basic text documents like reports or letters or whatever.

Today we want CSS to be able to do like *fully-fluid-3-columns-layout-with-responsive-images*. It's just crazy and this is why we need tools to help us and kind of bridge the gap between the legacy we have to support and new challenges.

Sass is one of those tools. It has been for 7 years now. Great tool really, it does a lot of stuff. It solves a lot of problems. But I feel like I have to kind of warn you because it's not all bright and shiny.

Sass not only solves problems but it also creates a lot of them. For many designers, many developers, CSS wasn't meant to be written with such complicated structures like loops, functions, mixins... It was like a simple declarative language and now it's close to programming.

So for many designers and developers, Sass is just scary code. It's just too complex, it's just *unmaintainable*. Look the irony, right?

My first advice today would be, try not to *overthink* things too much. It's very tempting with such a powerful tool as Sass to do a lot with it. Harry [Roberts] told us a couple of hours ago how [we shouldn't build something that wasn't asked for](https://speakerdeck.com/csswizardry/ten-principles-for-effective-front-end-development?slide=30). So my first advice would be try not to overthink things. If you need something to do A: make it do A, not the whole alphabet.

You know the [KISS principle](http://en.wikipedia.org/wiki/KISS_principle): Keep It Simple Stupid. I tweaked it to apply it to Sass: Keep Your Sass Simple. It's a fairly popular [article on SitePoint](http://www.sitepoint.com/keep-sass-simple/). And you could add another *S*: Keep Your Sass Simple and Straightforward. And you could add another *S*: Keep Your Sass Simple Smart and Straightforward. And you could add another *S*, but you get the idea.

My second advice would be: write simple APIs. Whenever you build a library, a mixin, a framework, a grid system, whatever, you are building some code that over developers will use &mdash; your team for instance &mdash; and this is your API. This is what you build. This is what you provide to other developers. So try to build simple stuff.

*This*, whatever it is, is not simple. It's probably very clever, it does a lot of stuff but it's not simple. "Underscore, 10, 8, 6, 4, alpha, omega, omega, default" is not simple. It's like some kind of military code so this is not the kind of thing you should build.

On the other hand, *this* is plain English. You could bring this to anybody with absolutely no tech background, he could almost tell you what's going on here. It's simple, it's easy, it makes sense.

(Let me skip this, and skip this. Here.)

Please! Stop nesting too much... I can't count the number of articles nesting 5 levels deep. It's a mess to understand, it's a mess to read, it's a mess to debug so please beware of selector nesting. It's a powerful feature when it's not abused. So try not to nest things too much, please.

My next advice would be not to do everything in Sass. Again it's very tempting because Sass is a very powerful tool. Jeff Atwood, a couple of years ago, told "[Any application that could be written in JavaScript will eventually be written in JavaScript](http://blog.codinghorror.com/the-principle-of-least-power/)", and God he was right. I think we could [apply it to Sass](hugogiraudel.com/2014/10/27/rethinking-atwoods-law/) so "any application that could be written in Sass will eventually be written in Sass" and... probably be me, right?

Trust me, we can do very silly stuff for experimental purpose. For instance *this*. This is a JSON parser written in Sass, no Ruby. Or *this*. This is sorting algorithms written in Sass, still no Ruby. Or *this*. This is bitwise operations written in Sass, no Ruby. So trust me we can do a lot of stuff that shouldn't be done. If you ever come up with something *that* crazy, just keep it on the experimental level and never ever try to bring it in a live project. It's a bad idea.

Some things should not be done in Sass, obviously. For instance, vendor prefixing. Vendor prefixing is probably something you should not do in Sass because it's probably better to keep it with [Autoprefixer](https://github.com/postcss/autoprefixer). I think you almost all know Autoprefixer. It's a postprocessing tool. So you use it when you want to autoprefix all your CSS properties according to a configuration file.

Obviously this is much better than doing it in Sass because you don't bloat your stylesheets with some conditional stuff that is likely to be gone in 2 years, 5 years, 10 years... This is less code, this is easier to maintain. So this is probably not a good idea to use Sass to vendor-prefix.

It's the same for `rem`. (I don't know if we can light up the room. That's cool, thanks guys.) So how many of you are using Sass to *rem* your font size and everything? Okay, so quite a couple of you. Don't be ashamed, there is no punition or anything.

For *reming* you better use some kind of postprocessing tool: [px_to_rem](https://github.com/songawee/px_to_rem) is a great one. Again it's much less code in your code base, it's easier to maintain, it has a configuration file, it doesn't use some kind of old hack with Sass variables... And as a proof, [Kaelig](https://twitter.com/kaelig) who spoke a couple of hours ago, removed 3000 lines from The Guardian codebase with a single pull request using px_to_rem instead of Sass. 3000 lines, it's pretty huge.

So don't try to do those kind of things with Sass, it's probably not a good idea. Let's change the subject for a second. Not only should some things not be done in Sass, simple APIs and everything doesn't mean your code will be easy to maintain.

You also have to write clean code. *This* isn't clean, obviously. *This* is clean. Or kind of. So... [CSS Guidelines](https://cssguidelin.es), right? Harry has done a massive work with those guidelines. It's absolutely great. Try to stick to them please, please, it would help a lot! If they don't suit your project very well, try to write your own but don't go deep into the wild without some kind of guidelines, it's pretty critical.

So you can use [scss-lint](https://github.com/causes/scss-lint) which is a great tool if you have a Sass codebase and have some guidelines written and want to have some kind automated process to make sure your code stick to the guidelines. It's fully customisable, it's very powerful so if you use Sass today, you probably should use this tool.

Clean code, simple code, and then document it! CSS as we all know from [Daniel's talk](http://disruptive-innovations.com/zoo/slides/20141114-dotCSS/dotCSS2014.pdf) is full of hacks and tricks and is kind of messy in its own way. When you have some kind of code like this, with hidden overflow and negative margins and random z-indexes, and you don't know what's going on, it means you have to comment it.

It doesn't take too much time, it's like what, 20 seconds and it saves a lot of time. It could save one hour debugging something because some guy comes here and just removes the `overflow: hidden` because he thinks it doesn't belong here and then everything breaks. So try to comment it. It doesn't take much time, it helps a lot, and everything that is not obvious from the first state should be commented.

And if you shoud document your CSS, you probably should document Sass as well. As we said earlier for many developers and designers, Sass is just too complex. It involves too many things, loops and everything. It's just a mess. Extends... Don't get me on extends. Anyway.

I built &mdash; with a couple of friends &mdash; [SassDoc](http://sassdoc.com). It's a tool, it's kind of the equivalent of JSDoc so it's to Sass what JSDoc is to JavaScript and everything. It's a comment annotation system so you write comments like *this*. For instance for a sizing mixin, you write like "this is my mixin, it takes this and this parameter, this is an example of use" and then you compile it and you have a beautiful generated documentation. It comes with a client search, all your mixins, variables, placeholders, functions, everything. It's pretty deep, it's a pretty cool tool. Kind of self promotion here.

Anyway, the point is if you write Sass especially public APIs like, you write a framework or a grid system, think of this kind of tool. If it's not this one, it's not this one, it doesn't matter. Think of documenting your code, it's very important.

And please test it. As much as you can. Either you could use some kind of custom tool like "this is my input, this is my output" and then you compile and you make sure the expected output matches the actual output. This is some kind of easy-to-do stuff.

Or you could use a Sass testing framework. There are 2 of them: [True](https://github.com/ericam/true) and [Bootcamp](https://github.com/thejameskyle/bootcamp). True is made by Eric Suzanne, the guy behind [Susy Grids](http://susy.oddbird.net) so you can say it's rock solid. Bootcamp unfortunately is not maintained anymore. It's too bad because it's really a great tool.

Anyway, both are heavily inspired by JavaScript, especially [Jasmine](http://jasmine.github.io/). It's a basic assertion system, so you have like "I expect my function with those parameters to return this".

Again if you build some kind of public API with Sass, either for open source or your team because it often happens that you're charged to build a grid-system for your own project; if you do this, try to run a testing framework like Bootcamp and make sure your functions work fine. It's not a big deal and it helps a lot.

So if we sum up: keep your code simple, keep your Sass simple. Don't nest too much. Try to build simple APIs, clear APIs with clean code. Obviously tested, it's important. Documented, as much as you can. There is no such thing as too much documentation, it doesn't exist.

And everything will be fine. Trust me. That's all I got, thank you!