Conference: dotjs-2016
Tags: JavaScript
Filmed: 2016-12-05
Author: moox
Image: https://farm6.staticflickr.com/5537/31339879402_b538a442a2_k_d.jpg
Title: A static website with React? Really?
Curator: sylvinus
Category: Backend
Summary: What if you could reuse all the unit tested React components that you will find on npm to make your isomorphic/universal static website? What if this website will be static but dynamic at the same time? What if you can even offer the UX of a progressive web app?
Slides: https://speakerdeck.com/player/b9faea2ddaf64e23a36ce9fede6732cd
Video: https://www.youtube.com/watch?v=WpPc8MyYC5k
Template: talk
Date: 2017-01-06 16:26:23
Status: draft


### Transcript: 

Let's say you have to build a website.
It can be a blog, a documentation website,
or whatever you want.
If you want a low cost solution that is performant for your users, you might want to use a static website generator.
The current solutions are very limited.

Let’s say you could use your favourite stack.
The one you love.
The one that is easy to reason about.
The one that allows you to
improve the quality of your code with unit testing and type checking.
The one that can be used universally, in node, in a browser, even on a native app.
Let’s say you can build your website with React, webpack, Flow, CSS modules,
and literally anything from npm.

Some solutions, like metalsmith can offer a fraction of that,
but they just render a dumb string.

In these cases, React doesn’t kick in on the client, so your `onClick` events are ignored …

With a bit of courage, you might hack your way into it, still you won’t have
a proper asset graph.

I tried to hack my way into it

I ended up creating a athoner kind of generator.

It’s called Phenomic.

If you represent Phenomic simply, it’s basically a function that takes your content and transforms it through webpack and react and makes a website out of it.

	phenomic = (content) =>
		webpack(
			<Layout>{ content }</Layout>
		)


Your content can be written in
Markdown, LaTex, HTML, JSON…

Basically any format.

Forget the old templating languages 😐.

You build your website with React components.

You might ask, what does Phenomic adds to the equation ?

First off, hot reloading.

Next, top-notch UX. 
At build time, Phenomic render each page as a static HTML file.
The result is a website completely SEO friendly that will work for the two people in the whole world who disabled JS.

The big difference when JS is on is that when the user navigates, it just loads the minimal data-requirements.
In fact, for each page, Phenomic also creates a small chunk of JS
containing its data.

With this, you can finally offer real-smooth page transitions, without the hacky "pjax" solution.

Out of the box, if you deliver your website over HTTPs, you have a progressive web app (Service Worker included).

You can generate an RSS feed or a sitemap with just a plugin.

We’re currently working on making Phenomic able to consume anything with a minimal API.

You will be able to generate a static version of a Wordpress website.

Another thing we’re working on is built in search. This is really amazing on a static website. We’re going to make an index at build time, so you can add a static search without relying on an external service.

Phenomic is a static website generator that wants developers and writers to be happy. 

As it’s a project by and for developers, we’d be really happy to receive your input and contributions.

Thank you!

Do not hesitate to visit [https://phenomic.io](https://phenomic.io) for more information about the project.