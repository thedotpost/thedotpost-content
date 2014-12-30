Conference: dotcss-2014
Tags: css
Filmed: 2014-11-14
Author: gregoradams
Image: https://farm6.staticflickr.com/5606/15635408350_eea86d722f_k_d.jpg
Title: Functionality in CSS
Curator: sylvinus
Category: Frontend
Summary: Gregor shows how to achieve behaviours similar to event listeners in pure CSS with a few hacks.
Slides: http://slides.pixelass.com/dotcss2014/
Video: https://www.youtube.com/watch?v=hXTRISz5q_Q
Template: talk
Date: 2014-12-30 12:12:07
Status: draft

## Functionality, what is that?
You can imagine functionality as something similar to event listeners. We have different ways to simulate these events in pure CSS.

Some examples can be seen on [my Codepen](http://codepen.io/collection/LcaEb/). Below I also explain how I used them to create a [CSS drawing app](http://codepen.io/pixelass/pen/JojdgK).

## How does it work?

The following snippets will show the basic code for the events.

### hover

```css
.action:hover {
  /*
   * actions in here will be fired on hover
   * This is similar the mouseenter or mouseleave event
   */
}
```

### focus

```css
.action:focus {
  /*
   * actions in here will be fired on focus
   */
}
```

### mousedown

```css
.action:active {
  /*
   * actions in here will be fired on mousedown
   */
}
```

### mouseenter

```css
.action {
  transition: all 0;
  transition-delay: 999999999999999999999999s;
}
.action:hover {
  transition-delay: 0;
  /*
   * actions in here will be fired on mouseenter
   * This is similar to the hover event
   */
}
```

### mouseleave

```css
.action {
  transition: all 0;
  transition-delay: 0;
}
.action:hover {
  transition-delay: 999999999999999999999999s;
  /*
   * actions in here will be fired on mouseleave
   * This is similar to the hover event
   */
}
```

### click

```css
input[type="radio"]:checked + label{
  /*
   * actions in here will be fired on click
   */
}
/*
 * abstraction
 */
._2:checked ~ .app ._2 {
  /*
   * actions in here will be fired on click
   */
}
```

## A pure CSS drawing app
I created a pure CSS drawing app making use of a few of these events. You can see it [here](http://codepen.io/pixelass/pen/JojdgK).

The basic app is built on radio-buttons (click event) and transition-delay (mouseenter & mouseleave).

What is actually happening in this app is the following:

1. if we select a color we are actually checking a radio button
   * all radio buttons share the same name attribute
   * radio buttons toggle each other
1. while a color is selected we set the background-color of a pixel
1. we are only changing the background-color on mouseenter (not on mouseleave)


## More examples

* [slot machine](http://codepen.io/pixelass/pen/tojac)
* [memory game](http://codepen.io/pixelass/pen/nuhyG)
* [color picker](http://codepen.io/pixelass/pen/lgkJr)
* [scrollTo](http://codepen.io/pixelass/pen/vqoyf)
* [quiz](http://codepen.io/pixelass/pen/KsEJa)
* [advanced click](http://codepen.io/pixelass/pen/PwqNyG)
