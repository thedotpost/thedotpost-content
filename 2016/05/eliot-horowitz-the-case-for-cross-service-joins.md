Conference: dotscale-2016
Tags: Cross-Service
Filmed: 2016-05-25
Author: eliothorowitz
Image: https://farm2.staticflickr.com/1642/26659151625_c086b94436_k_d.jpg
Title: The Case for Cross-Service Joins
Curator: sylvinus
Category: Security
Summary: Developing a modern application oftern means composing it with several services, many of them third-party. While this offers many benefits, it also traps your data in silos, preventing a holistic view. Eliot presents the cross-service-join: a means of querying across multiple services from a central database.
Video: https://www.youtube.com/watch?v=huwM-amMGnM
Template: talk
Date: 2016-06-13 11:06:23


Modern applications are composed of services, many of them third-party, orchestrated by the increasingly narrow band of behavior unique to any particular application: the business logic. Service-based architecture is faster to develop and more fault-tolerant than the monolithic and N-tiered applications that came before. But as a byproduct, it creates silos of data for each service, preventing a holistic view.

Current solutions to this problem, such as Data Lakes, are either nothing more than punting on the problem or themselves a huge hassle. If all services wrote their data to a single database owned by the application, it would be easy to query across it all, but providing reasonable SLAs under those circumstances seems impossible.

What we need is a cross-service-join, a method whereby a single database can optimize queries between multiple services, caching data where appropriate. Cross-service joins would build on the services that are already in place, and require extending them to support passing the meta-data to allow optimization. Eliot presents a proof-of-concept built on MongoDB’s aggregation framework.
