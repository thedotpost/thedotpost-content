Conference: dotswift-2017
Tags: Swift
Filmed: 2017-01-27
Author: loganwright
Image: https://farm1.staticflickr.com/712/32624892736_9219099767_k_d.jpg
Title: Representables in Swift
Curator: sylvinus
Category: Frontend
Summary: In this talk, Logan discusses about the representable design pattern in Swift and particularly how it can help library developers create more flexibility in their apis without sacrificing control internally.
Video: https://www.youtube.com/watch?v=V8bUUTqCrvI
Template: talk
Date: 2017-03-09 11:05:21
Status: draft

Some examples of this can be found in the Vapor repository, [here's a link](https://github.com/vapor/engine/blob/2d616d7cc1451752310007a2c8591ce11dc2cc37/Sources/HTTP/Models/Response/ResponseRepresentable.swift) to the ResponseRepresentable type.

This is used in vapor so a user can return the object as they would normally without having to construct an entire request on each end point.

One thing not discussed here for time concerns is that this can also be inverted into an Initializable type which is something that can be initialized by another type which can create some pretty interesting combinations and transformations between our models.