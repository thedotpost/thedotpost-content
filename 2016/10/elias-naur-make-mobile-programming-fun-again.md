Conference: dotgo-2016
Tags: Golang
Filmed: 2016-10-10
Author: eliasnaur
Image: https://farm9.staticflickr.com/8617/29646642794_e6f404d5fb_k_d.jpg
Title: Make mobile programming fun (again)
Curator: sylvinus
Category: Backend
Summary: Elias takes us on a quick tour of Go Mobile to see just how much of your mobile app can be in Go.
Slides: https://talks.godoc.org/github.com/eliasnaur/talks/gomobile-dotgo-2016.slide
Video: https://www.youtube.com/watch?v=QfFwceFo97E
Template: talk
Date: 2016-11-03 16:09:30
Status: draft

For quite a while, Go programmers have been able to export their Go package to mobile iOS and Android apps through Go Mobile.
With recent additions to Go Mobile, the reverse is now possible: importing and using the platform Java or Objective C API directly from Go, as well as declaring custom Java or Objective C classes that are implemented in Go.
For Android, the Go Mobile gradle plugin is now tightly integrated with the Android gradle build system. Project resources, Java code, libraries and even the databinding classes are now all available from Go.


More information:

The [golang.org/x/mobile/example/reverse/reverse](https://godoc.org/golang.org/x/mobile/example/reverse/reverse) example is a Android app in 100% Go using the new Java bindings described in the talk. The Gradle plugin is described in [godoc.org/golang.org/x/mobile/cmd/gomobile](https://godoc.org/golang.org/x/mobile/cmd/gomobile).


An overview of using Java or Objective C from Go is described in [godoc.org/golang.org/x/mobile/cmd/gobind](https://godoc.org/golang.org/x/mobile/cmd/gobind).


For even more detail about writing native language bindings, these original proposals are a good start:

- [golang.org/issues/16876](https://golang.org/issues/16876) (Java, Android)
- [golang.org/issues/17102](https://golang.org/issues/17102) (Objective C, iOS)