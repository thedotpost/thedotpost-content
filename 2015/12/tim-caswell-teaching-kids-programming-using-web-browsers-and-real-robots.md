Conference: dotjs-2015
Tags: JavaScript, Live coede
Filmed: 2015-12-07
Author: creationix
Image: https://farm6.staticflickr.com/5774/23285767359_5b325888e5_k_d.jpg
Title: Teaching Kids Programming using Web Browsers and Real Robots
Curator: sylvinus
Category: Frontend
Summary: Watch Tim's son livecode real hardware robots over wifi using JavaScript compilers in the browser, C VMs on micontrollers, and a Lua server as relay system. Then dive into the tech.
Slides: https://gist.github.com/creationix/507719a418be365c7631
Video: https://www.youtube.com/watch?v=e6BEMQNyiRY
Template: talk
Date: 2016-01-08 11:42:19
Status: Draft

Tim explains:

There are not enough good programmers in the world so I had the idea to help by instilling a love for programming in kids via simple hardware kits and a webpage.

To demonstrate this technology, you will see my son live-code a small program and send it to a robot on stage.

This is a multi-year hobby project, but this particular demo involves the following parts:
 - Bytecode Interpreter written in C running on the microcontroller inside the robot.
 - Compiler written in JavaScript running in the webpage
 - Bridge written in luvit that serves the webpage and sends programs to the robot. (http + websockets + tcp)

Partially implemented components not in the demo include:
 - Git implementation written in JavaScript that runs in the browser and acts as client to global code repository.
 - High Level language that kids write that's compiled by JS and pulls in dependencies via websockets and git implementation in JS.

I plan on writing a blog post on [luvit.io](http://luvit.io/) soon and/or porting the server to a packaged app to run offline on chromebooks (which kids often have access to in school).
