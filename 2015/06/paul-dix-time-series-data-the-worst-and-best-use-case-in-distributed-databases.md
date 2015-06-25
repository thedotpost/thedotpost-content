Conference: dotscale-2015
Filmed: 2015-06-08
Author: pauldix
Image: https://farm1.staticflickr.com/532/18698829242_2791d3601a_k_d.jpg
Title: Time series data: the worst and best use case in distributed databases
Curator: sylvinus
Category: Backend
Summary: Paul delves into some of the challenges involved in building a distributed database specifically for time series data. High write throughput, even higher read throughput, large range scans of data to answer queries, and large range deletes all conspire to make time series data both the worst and best use case to build for in distributed databases.
Tags: timeseries, databases, influxdb
Slides: http://speakerdeck.com/player/efb10631fa58468ebd2364858b62a70c
Video: https://www.youtube.com/watch?v=B0Apg5NpmYA
Template: talk
Date: 2015-06-25 11:01:49
Status: draft

Further reading:

 - [The Log Strucutred Merge Tree](http://bjturesearch.googlecode.com/svn/trunk/The%20Log-Structured%20Merge-Tree%20(LSM-Tree).pdf)
 - [Riak’s page on LevelDB](http://docs.basho.com/riak/latest/ops/advanced/backends/leveldb/)
 - [BTree vs. LSM in WiredTiger](https://github.com/wiredtiger/wiredtiger/wiki/Btree-vs-LSM)
 - [InfluxDB Clustering Design](https://influxdb.com/blog/2015/06/03/InfluxDB_clustering_design.html)
 - [BoltDB, a Go COW B+Tree implementation](https://github.com/boltdb/bolt)