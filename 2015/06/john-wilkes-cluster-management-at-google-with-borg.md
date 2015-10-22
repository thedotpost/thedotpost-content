Conference: dotscale-2015
Tags: ClusterManagement
Filmed: 2015-06-08
Author: johnwilkes
Image: https://farm1.staticflickr.com/433/18516528538_31688660db_k_d.jpg
Title: Cluster management at Google with Borg
Curator: sylvinus
Category: Backend
Summary: John describes Borg, the Google's cluster management system which supports almost all the computation that Google does, and has informed the development of the open-source Kubernetes system.
Slides: https://drive.google.com/file/d/0B5g07T_gRDg9SFlIZHhoQUJCeXc/preview
Video: https://www.youtube.com/watch?v=wy3L7XUq-g0
Template: talk
Date: 2015-10-22 13:23:08
Status: draft

<p class="p1"><span class="s1"><a href="http://www.e-wilkes.com/john/papers/2015-EuroSys-Borg.pdf"><b>Large-scale cluster management at Google with Borg</b></a></span><span class="s2">. Abhishek Verma, Luis Pedrosa, Madhukar R. Korupolu, David Oppenheimer, Eric Tune, and John Wilkes. <i>European Conference on Computer Systems (</i><a href="http://eurosys2015.labri.fr/"><span class="s1"><i>EuroSys</i></span></a><i>)</i>, April 2015 (Bordeaux, France). [links: <a href="http://dl.acm.org/authorize?N95407"><span class="s1">ACM DL</span></a>, <a href="http://www.e-wilkes.com/john/papers/2015-EuroSys-Borg.bib"><span class="s1">bibtex</span></a>]</span></p>
<p class="p2"><span class="s2"></span></p>
<p class="p1"><span class="s2">Google's Borg system is a cluster manager that runs hundreds of thousands of jobs, from many thousands of different applications, across a number of clusters each with up to tens of thousands of machines.  </span></p>
<p class="p2"><span class="s2"></span></p>
<p class="p1"><span class="s2">It achieves high utilization by combining admission control, efficient task-packing, over-commitment, and machine sharing with process-level performance isolation. It supports high-availability applications with runtime features that minimize fault-recovery time, and scheduling policies that reduce the probability of correlated failures. Borg simplifies life for its users by offering a declarative job specification language, name service integration, real-time job monitoring, and tools to analyze and simulate system behavior.  </span></p>
<p class="p2"><span class="s2"></span></p>
<p class="p3"><span class="s2">We present a summary of the Borg system architecture and features, important design decisions, a quantitative analysis of some of its policy decisions, and a qualitative examination of lessons learned from a decade of operational experience with it.</span></p>