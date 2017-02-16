Conference: dotswift-2017
Tags: Swift
Filmed: 2017-01-27
Author: huguesbernetrollande
Image: https://farm1.staticflickr.com/683/31822548284_11c1ac9a70_k_d.jpg
Title: IoT and iOS - Lessons Learned
Curator: sylvinus
Category: Frontend
Summary: After two years working on Connected Devices (IoT) on iOS, Hugues shares what he learned and best practices.
Slides: https://speakerdeck.com/player/6c058162a3314c94a790e0198d237b0b
Video: https://www.youtube.com/watch?v=m8yN9q_EpQ4
Template: talk
Date: 2017-02-16 15:38:45
Status: draft

Developing an iOS App which connect to a BLE device can be tedious. BLE connectivity is limited when working in Xcode Simulator and debugging can be tricky. Hugues shares some tips that help having a faster and most robust development cycle:
* Implementing Unit Tests to validate your BLE data transformation
* Containing your BLE layer using wrappers and protocols to be able to work on your App even in the Simulator
* Developing a Device Simulator (another iOS App) to simulate your device in order to avoid being block by longer hardware development cycle

This talk is not a BLE introduction, you should check Apple WWDC videos to get a good overview:
* WWDC 2012 - Core Bluetooth 101
* WWDC 2012 - Advanced Core Bluetooth
* WWDC 2013 - Core Bluetooth

You can also follow this good tutorial to work with BLE: [http://www.cloudcity.io/blog/2015/06/11/zero-to-ble-on-ios-part-one](http://www.cloudcity.io/blog/2015/06/11/zero-to-ble-on-ios-part-one)

Hugues has also done a workshop about BLE on iOS at FrenchKit 2015: [https://speakerdeck.com/huguesbr/introduction-to-ble-on-ios](https://speakerdeck.com/huguesbr/introduction-to-ble-on-ios)
