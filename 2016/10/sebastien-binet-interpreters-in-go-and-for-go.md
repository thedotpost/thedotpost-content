Conference: dotgo-2016
Tags: golang
Filmed: 2016-10-10
Author: sebastienbinet
Image: https://farm8.staticflickr.com/7517/30161637942_c4370e0c6b_k_d.jpg
Title: pygo: Interpreters in Go and for Go
Curator: sylvinus
Category: backend
Summary: Go is a great general purpose programming language and it is thus no surprise it can be a great fit for science work. But Go could be an even better fit for all kind of exploratory work, such as data analysis, if it had an interactive interpreter, also known as a Read-Eval-Print Loop (a REPL). Sébastien introduces pygo, a very first step in that direction.
Slides: https://talks.godoc.org/github.com/sbinet/talks/2016/20161010-dotgo-pygo/talk.slide
Video: https://www.youtube.com/watch?v=MWZrZH9Xz84
Template: talk
Date: 2016-10-25 10:33:12
Status: draft

Go is a great general purpose programming language and it is thus no surprise it can be a great fit for science work.
Indeed, Go provides an efficient and quick edit/compile/run development cycle, while being also reasonably fast at runtime.
The Gonum community[1] already provides a set of robust scientific libraries.
Thanks to its static binaries, Go is easy to deploy on various hardware (laptop, desktop, clusters, …): this is also facilitated by its simple cross-compilation mechanism.
Last but not least, Go is a simple language that scientists can quickly learn and become proficient, if not master.
But Go could be an even better fit for all kind of exploratory work, such as data analysis, if it had an interactive interpreter, also known as a Read-Eval-Print Loop (a REPL).

Of course, there are already many Go interpreters and REPLs:
[github.com/motemen/gore](github.com/motemen/gore)
[github.com/sbinet/go-eval](github.com/sbinet/go-eval)
[golang.org/x/tools/ssa/interp](golang.org/x/tools/ssa/interp)
...

Unfortunately, none of them provide an interactive interpreter with support for the full Go language.
The [github.com/go-interpreter](github.com/go-interpreter) organization is a nascent community effort to address this issue to design, implement and provide an interactive interpreter, for the full Go language (and implemented in Go.)
This is still early days and development process is still at the design phase [2].

What can you do when you have next to no expertise in designing and building REPLs?
When you need to assemble an interpreter from its core components?
When you don’t know what are these components?
When you need to decide between using a virtual machine to interpret a Go program or whether to directly interpret the AST?
Should you use a stack-based or a register-based VM?
What opcodes should your VM use? etc…

To help navigate through this flock of existential questions, it is best to have a kind of skeleton which can be iterated over, experimenting with various approaches.
For this talk, I started with the blueprint from the “Architecture of Open Source Applications” book [3]: the nice article “A Python Interpreter Written in Python” by Allison Kaptur [4].
“pygo” is the translation of this article into a Go space: “pygo” is a toy virtual machine interpreter for CPython-3, written in Go.
Like in the AOSA article, “pygo” uses the “python3” interpreter to compile python source code into bytecode.
This bytecode is then fed to the “pygo” VM that will read, decode and interpret instructions from the bytecode.

The full code of “pygo” [5] is available at: [github.com/sbinet/pygo](github.com/sbinet/pygo)
There are still many more issues to address and implement (functions, frames, blocks, closures, classes, …) to, finally, provide a REPL.
It is still very much a work in progress.

Thanks!

[1]: <a href="https://github.com/gonum" target="_blank">https://github.com/gonum</a>
[2]: <a href="https://github.com/gonum/proposal/issues/1" target="_blank">https://github.com/gonum/proposal/issues/1</a>
[3]: <a href="http://aosabook.org" target="_blank">http://aosabook.org</a>
[4]: <a href="http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html" target="_blank">http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html</a>
[5]: <a href="https://github.com/sbinet/pygo" target="_blank">https://github.com/sbinet/pygo</a>