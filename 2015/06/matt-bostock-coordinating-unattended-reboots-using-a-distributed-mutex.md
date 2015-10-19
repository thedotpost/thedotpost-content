Conference: dotscale-2015
Filmed: 2015-06-08
Author: mattbostock
Image: https://farm1.staticflickr.com/375/18516849469_1cc976b093_k_d.jpg
Title: Coordinating unattended reboots using a distributed mutex
Curator: sylvinus
Summary: Matt explains how GOV.UK borrowed an idea from CoreOS' reboot mechanism and are using etcd-backed distributed mutex to orchestrate unattended reboots across their Ubuntu server estate to apply essential security updates.
Slides: http://www.slideshare.net/slideshow/embed_code/key/xLYEPOJ1jg5Yu6
Category: Backend
Video: https://www.youtube.com/watch?v=w7o9xNyZCQo
Template: talk
Date: 2015-10-19 10:52:43


The open source Puppet module which is used at <a href="https://www.gov.uk/"><span class="s2">GOV.UK</span></a> to coordinate unattended reboots on Ubuntu can be found on <a href="https://github.com/gds-operations/puppet-unattended_reboot"><span class="s2">GitHub</span></a> and on the <a href="https://forge.puppetlabs.com/gdsoperations/unattended_reboot"><span class="s2">Puppet Forge</span></a>. Contributions are very welcome and encouraged. <br>


To understand more about the Raft consensus algorithm, I recommend following the <a href="http://thesecretlivesofdata.com/raft/"><span class="s2">visualisation</span></a> by <a href="https://github.com/benbjohnson"><span class="s2">Ben Johnson</span></a> and reading the <a href="https://raftconsensus.github.io/"><span class="s2">Raft paper</a>. <br>


You can find out more about engineering at <a href="https://www.gov.uk/"><span class="s2">GOV.UK</span></a> on the <a href="https://gdstechnology.blog.gov.uk/"><span class="s2">GDS Technology blog</span></a> and also at the <a href="http://gds-operations.github.io/"><span class="s2">GDS Operations open source</span></a> web site.