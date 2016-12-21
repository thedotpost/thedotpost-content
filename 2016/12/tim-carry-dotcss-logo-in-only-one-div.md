Conference: dotcss-2016
Tags: CSS
Filmed: 2016-12-02
Author: timcarry
Image: https://farm1.staticflickr.com/273/31359196742_afcee1e616_k_d.jpg
Title: dotCSS logo in only one div
Curator: sylvinus
Category: Frontend
Summary: What if we recreated the dotCSS logo with only CSS and one div? Tim uses some tricks involving invisible text, box-shadow, and line breaks to achieve it.
Slides: https://pixelastic.github.io/talk-dotcss-onediv/#/
Video: https://www.youtube.com/watch?v=3z6JhjoG7nA
Template: talk
Date: 2016-12-21 11:31:46
Status: draft

You can have a look at the code on GitHub: [https://github.com/pixelastic/dotcss-onediv](https://github.com/pixelastic/dotcss-onediv)
The big yellow dot is made of a `:before` pseudo-element, with `border-radius:50%` and `position:absolute`.
The black dots of the background are all made through `box-shadow`, changing the size, color and positioning of the original big yellow dot.
The “dot” and “CSS” text are part of the `content` of the `:before`, with a new line added between the words (using `\A ` and `white-space:pre`) which lets me target each word individually using `:first-line` or not.
The “CSS” word is actually a white `text-shadow` of the original word displayed with “invisible ink” (aka. `color: transparent`) to position it where needed
