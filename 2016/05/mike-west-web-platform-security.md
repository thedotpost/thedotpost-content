Conference: dotsecurity-2016
Tags: Security
Filmed: 2016-05-22
Author: mikewest
Image: https://farm8.staticflickr.com/7195/26678053894_6359907afd_k_d.jpg
Title: Web Platform Security
Curator: sylvinus
Category: Security
Summary: Even in an alternate universe in which the browser implements every standard perfectly, users aren't safe because the platform itself has holes like XSS and CSRF. Mike talks about some new features which allow developers to mitigate these platform-level risks by locking down their own applications.
Slides: https://speakerdeck.com/player/6497ed3af12941aaae5ca7747ad08b84
Video: https://www.youtube.com/watch?v=sgEv92XqdhM
Template: talk
Date: 2016-05-27 15:27:26

## Transcript:


Hi.

I get to live in a beautiful world. The world that I get to live in is
one in which everything works, except for the things that I am actually
responsible for.

I assume that the rest of the Chrome security team is doing their job. I assume
that the CPU is actually doing what it's supposed to be doing on a regular
basis. And in this beautiful and completely hypothetical world, we still have
issues, and I'd like to talk with you about some of them today.

The painting behind me is Ulysses and the Sirens. Are any of you familiar with
that painting? Culture. Excellent.

The sirens sing beautifully. They sing so beautifully in fact that it drives
men to the brink of madness. So when a sailor goes by their island the sailor
will listen. They'll hear the song of the sirens, all they'll want to do
is hear more of that song, so they'll throw themselves off the side of the ship,
in order to get to the island to get more and more of this beautiful music. And
then the sirens will eat them because, you know, that's what sirens do.

Ulysses is a man who is out for the Trojan War, and he had been away from home
for, like, ten years. And all he wants to do at this point is get back home with
his men.

He talks to a witch named Circe, and she tells him that to get back home he's
going to have to go by this island. There's simply no other way, so how can he
defend himself against these sirens?

As it turns out, Circe has a good idea for him. You can take wax. You can mold
the wax into little earplugs, and you can put the wax in your ears. And then you
don't hear the song of the siren, and by not hearing the song you're not driven
mad. You don't jump overboard, and you're not eaten. It sounds like a great
scenario.

Circe further tells him that if he wants he can actually listen to the song of
the sirens by having his men bind him to the mast, right. So if you tie your
hands and your feet tightly to the mast, then he can hear the song of the
sirens, but he's physically prevented from actually jumping off the ship.

He thinks this sounds like a great plan, so he has his men tie him to the mast.
They all put wax in their ears, and they start sailing by the island, and as
it turns out this works beautifully.

Ulysses hears the song of the sirens. He hears this beautiful music. He wants
to hear more of it, but he has physically prevented himself from actually
jumping off the side of the ship.

Now, this is incredibly relevant to security on the web. Let's look at the
threat model that we actually care about, in order to see how that might fit in.

So there are basically two things that I really care about with regard to the
web platform. Assuming we implement all of the specs correctly there are two
things that really worry me.

The first is cross-site scripting. Scott talked about this a little bit earlier
today. I want to give you a little bit more detail, just to make sure we're all
on the same page with regard to the dangers of content injection, and then we'll
move on.

Behind me you see five different places in which content can be injected into
pages, and all of these five places have different rules. So if you're injecting
something into a style sheet, you're going to want to escape that differently
than if you're injecting it into a paragraph or into an HTML attribute. All of
these have different rules, but these rules are completely mechanical. XSS is a
completely solved problem.

Theoretically.

The next kind of attack that I think is really interesting is something called
cross-site request forgery. The idea here is that the browser has ambient
authority for a wide variety of origins. If I'm logged into
`innocentvictim.com`, then all of the requests it makes and it expects will have
cookies associated with them and other sorts of authentication data. That means
that `innocentvictim.com` will honor my requests and will actually take whatever
action it is that I'm asking for. If `evil.com` however makes a sneaky request
on the side by loading an iframe, or loading an image, or sending an XHR
request, that request can have the same authentication tokens bound to it. What
this means is that it's difficult for `innocentvictim.com` to distinguish
between good requests and bad requests, and it's entirely possible for a third
party to maliciously force that victim site to do something that it wasn't
anticipating.

Now I said cross-site scripting is a completely solved problem. It is
theoretically, but practically what we see in the Vulnerability Rewards Program
at Google, something that Fillipo talked about earlier today, the vast, vast
majority of the attacks that we actually pay for are cross-site scripting. Even
at Google. A company with a dedicated team doing nothing but preventing the
developers inside of Google from doing whatever it is they want to be doing. We
build really interesting tools, and we build out good, solid templating systems,
and yet we still have cross-site scripting attacks.

So what can we do to start mitigating these? And why do they happen in the first
place?

Well, as it turns out the browser is a confused deputy. That's the name of this
class of attack. It has power, and it can act on that power, but by doing so
it's not actually taking actions on your behalf. It's taking actions on an
attacker's behalf using your credentials.

Now, you shouldn't give a deputy like this a gun. You should instead give them
something a little bit softer.

Chrome in this case, and every other browser, is acting as a confused deputy,
because it's using your ambient authority to do things on the web that you don't
actually want it to be doing. It hears the siren song of JavaScript.

If you know anything about V8, you know that it loves JavaScript, and it wants to
execute that JavaScript just as quickly as it possibly can. So what can we do
about this?

The name of the game is privilege reduction. You heard earlier the notion of the
principle of least privilege. If you don't have any privileges, then it doesn't
matter if someone asks you to do something bad, because you have prevented
yourself from doing that. You don't have the privilege to do so.

What I'd like to talk about are a couple of mechanisms that exist that you can
use in browsers today to reduce the privilege of pieces of your application, in
order to ensure that your application can do the things that it needs to do, but
that it's not going to throw itself overboard at the first sign of interesting
JavaScript.

The first of these you've already heard about. It's called Content Security
Policy, and the idea of Content Security Policy, as Scott mentioned earlier today,
is to give you granular control over the things that are happening on your website.
So he talked a little bit about a fairly simple set of Content Security Policy that
can be applied to particular sites.
Now, as you can see, this is a fairly simple content security policy that's used
on a very small site called Twitter. This is copy and pasted this morning, and
it's ridiculous, right? This thing is absolutely huge, and as it turns out it's not
nearly as strong as you would expect from the amount of text that you see on the
page.

The idea of course is that it wants to allow you to talk to Twitter, but it doesn't
want to allow you to talk to `evil.com`. So load script, or load images, or any of
these things. What we've seen however is that these kinds of white lists are
actually really, really difficult to get right. They're hard to maintain, and if you
make them easy to maintain they're too loose to have any actual impact.

So the folks at Cure53 -- Mario Heiderich and a few others -- have noted that on
large origins, origins like `google.com` or various CDNs, there's enough code there
to do absolutely anything you want to do.

So if you whitelist `google.com`, you're not only whitelisting those individual
files that you yourself wrote. You're whitelisting a wide variety of things
including old versions of Angular that you actually do not ever want to run on a
website.

There has to be a better way, and in CSP3 we're looking at a couple of options
that the Google folks think are really interesting and I think are pretty
interesting in the browser as well.

The idea is called `'unsafe-dynamic'`, and it treats nonces and hashes as
capability tokens. So you put a script tag on your page, and the script tag
contains a particular attribute. The attribute contains a long random token.
That token is reflected in the HTTP header that you sent to the page.
This means that you're not whitelisting any script. You're whitelisting this
particular script, and because the nonce is long and random, the attacker can't
actually guess it. This has some really good properties, but we can go one step
further.

We can allow the script that you've loaded, the script that you've carefully
audited, and the one that you know is doing the right thing to then load its
own scripts. That is we'll use nonces for every script on the page or hashes
for every script on the page, and what that does is allow us to say, "We've
audited all of these scripts. We know these are the ones that ought to run,"
and then those scripts are empowered to do whatever it is that that widget
needs to do. So if you want to load Google Maps for instance, that's going to
load a script which loads a couple of more scripts and then shows a map.

Now, this is possible to do today with whitelists. You can whitelist absolutely
every file that you might need. That becomes very brittle, very difficult to
maintain, or very easy for the library owner to actually break you, because the
library owner doesn't know that you're using a very strict CSP and probably isn't
going to notify you when they update it.

So we think unsafe dynamic is a really interesting property. It's going to be
shipping in Chrome 52, and we'd really like people to start playing around with
it, so that we can kind of understand the properties and understand whether it
actually solves the problems that we think it's going to solve as well as we
think it's going to solve them.

The next thing I'd like to talk about is called Suborigins. Now, all of you are
probably familiar with the idea of the same origin policy. Every website on the
Internet has a tuple of a scheme, a host, and a port. So "HTTP", "example.com",
"80". That defines an area of influence and a set of data that everything
executing within the context of an origin has access to.

Now, I'll repeat that. Everything in that origin has access to everything in the
origin, so if I execute some script in example.com, then I get all the local
storage. I can talk to the backend and pretend that I am example.com. This ends
up being a good isolation property for most of the web, but for a lot of origins
that have multiple applications running on them we'd like to be able to segregate
things even more.

So if you think about google.com for instance, we have Docs, we have Maps, and we
have Gmail, and a variety of other applications including marketing applications
from 2004 that are all running on google.com.

And those have very different levels of audit that have been applied to them, but
because they're all running on google.com they all have that same set of privilege.

What we'd like to do is allow developers to actually shard that physical origin
into a number of logical origins, so that you can say that, "This page that I'm
loading is actually part of the Docs application, and this page is part of the Maps
application." And they shouldn't be able to talk to each other directly. They
shouldn't be able to access each other's data.

This is similar in concept to the notion of a sandbox, so iframes have this sandbox
attribute that lets you push them into a unique origin.

The nice property here is that this is actually a named sandbox which means there
are some properties about communication that we can start to enable, because we
know that this is going to be the same name going forward.

Now, there are some questions about what exactly this sharding should amount to.
What kinds of communications can we enable between the physical origin and these
logical origins? What do we do with cookies? Because of course cookies span across
origins. They span across domains, and they are a big pain in the butt for
basically anyone who needs to deal with security on the web. So there are some
open questions there, and it would be really helpful to us if you all would take a
look at the prototype implementation that's in Chrome today and the specification
that I showed just a moment ago, and help us figure out what kinds of use cases we
should be addressing with this kind of functionality.

 This is all experimental, and it's not something that I think we're going to ship
in the very near future.

Subresource integrity, on the other hand, has already shipped in both Chrome and
Firefox, and other browsers are starting to get interested in it. The idea is that
you can whitelist a particular set of content coming from a CDN or coming from some
external server. You can say, "I want this script to run, and not just this script
at this location, but this exact script."

You put a digest into an `integrity` attribute within the tag, and that gives you
the ability to say, "Not only this script from this location is going to execute,
but that we can verify that it is exactly the scrip that I think it's going to be."

This removes some of the potential for damage that CDNs can cause, because of
course CDNs are a juicy target for attackers. If I can own CloudFlare, then I'm
not only owning CloudFlare. I'm actually able to attack a wide variety of sites
on the Internet.

By using an integrity attribute to get out to those CDNs, I can verify that the
CDN is doing its job and that it hasn't been compromised. This has some really
interesting properties.

A future version of this will probably do something more than just digests. I
think we're very interested in looking at signatures. We're very interested in
looking at the kinds of things that Diego talked about earlier. We're just not
there yet with regard to this specification.

Finally, cookies. Cookies are super interesting. They're super interesting
because they're super broken, from a security perspective. Cookies don't honor
the same origin policy. They have no understanding of ports, and they span
across schemes. This is kind of problematic.

We have a couple of ideas of how we can improve the state of cookies, so the
HTTP working group in the IETF is going through some of these ideas, in order
to figure out what pieces we can actually change without making breaking changes
to the Internet. One idea that I think is pretty interesting is the notion of a
same-site cookie. So I showed you earlier this picture of innocentvictim and
evil.com, and evil.com is able to talk directly to innocentvictim because again
the browser is an ambient authority.

It would be nice if innocentvictim could say, "You know, I don't actually want
this scenario to ever happen. No one should ever embed me. I should never be in
a situation where someone else has authority over me." So we can start looking
at the initiator of a request and not just the recipient of a request when
determining what cookies ought to be sent along with that request.

The idea is simple. The victim will specify a new attribute on the cookie called
"SameSite." They can set it either as "strict" or "lax", and those have slightly
different properties, but for the purposes today they're similar.

When evil.com makes a request -- maybe they've embedded an image, maybe they've
embedded an iframe -- that request will be coming from something different than
the victim site, and in that case because they've specified that this cookie
should never be sent in that kind of scenario, we can actually prevent a large
class of cross-site request forgery attacks. We think this is going to be really
quite interesting for a lot of sites out there, and I think it has a good amount
of potential to really reduce the impact of both cross-site request forgery
attacks and cross-site script inclusion attacks which rely on the same sorts of
principles.

Finally, I'd like to talk a little bit about TLS. So TLS is a little bit outside
the model that we've been talking about before. It's not strictly about privilege
reduction. It is instead about bringing up a baseline of security for your
websites.

It is simply the case that if you're not delivering your websites over
HTTPS, then you have no security. There is literally nothing you can do on the
web, in browsers, that gives you any piece of security at all, if you don't have
TLS as a baseline. TLS gives you a couple of guarantees. It gives you a modicum of
confidentiality. It gives you integrity, because you know that the bits that the
server sent actually are the ones getting to you. And it gives you authentication,
because you know that that server is the one sending something to me, not any
router in between me and that server.

The Chromium project has started to lock down old APIs that were initially shipped
in such a way that they would work both over TLS and over non-TLS. Some examples
of this are geolocation, your microphone, and your camera. Powerful features that
we really never should have shipped over HTTP to begin with, because by shipping
them over HTTP you are not just granting permission to the site you think you're
granting permission to. You're actually granting permission to anyone between you
and that site. Anyone in a privileged network position, and that's something that
we simply can't allow, so we're starting to lock down those old APIs.

We're also looking at ways of making migration a little bit simpler. Scott talked
a little bit about mixed content before, and mixed content has come up very often as
a hard blocker for folks moving over to HTTPS. There are some CSP-related mechanisms
that you can use, like block-all-mixed-content and upgrade-insecure-requests.

One more thing that we're thinking about doing is actually reversing the order of
HSTS and mixed content checks. That is, if you set a strict transport security header
that says, "Only connect to me over HTTPS," we would like to do that upgrade before
we do mixed content checks.

We can't do that today, because there's a bit of a determinism problem. That is,
developers have always been to all of their origins, so they will never see an HSTS
error if they embed something in their page that isn't using the right scheme.
Users will see it. They'll file bugs. The developer will throw up their hands and
say, "Well, it works for me," and close the bug.

So we'd like to ensure that we can start doing HSTS first, but do it safely. And
the idea that we have is to send out what's called a priming request. If I'm
about to request an insecure object or an insecure resource, I'll first go out
to the website over HTTPS, check to see whether I get an HSTS header back, and
if I do, then I can do the upgrade, and everything will work out pretty well. This
should be really valuable for large sites, especially YouTube, because YouTube has
just started sending an HSTS header which gives us the ability to not block folks
from upgrading, because if they upgrade, then they couldn't get YouTube, and
they'd be a little bit sad.

Privilege reduction is the name of the game. There are a number of mechanisms
that have been released over the last six months to a year that are really, really
interesting, and I'd love for y'all to go out, and play around with them, and give
us some feedback. Both on the Chrome team, but also in standards bodies, so that we
ensure that we're building the tools that allow you to lock down your sites and to
tie it up a little bit because, you know, sites shouldn't jump overboard.

Thank you very much.