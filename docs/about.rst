*****
About
*****

What is BOINSO?
===============

BOINSO stands for "Berkley Open Infrastructure for Networking Satellite Operations". This name was chosen in honor to the BOINC and GENSO projects.

BOINSO is an attempt to create a Genso_ like structure from scratch. In contrast to GENSO this project will be open source and free to use in a less localized way so that every mission control center can tweak the system to its needs.

.. _Genso: https://en.wikipedia.org/wiki/Global_Educational_Network_for_Satellite_Operations

The current situation
=====================

A typical student space segment
-------------------------------
A small satellite in Low-Earth Orbit, often Sun Synchronous, Low-power transmitters, Simple and standard communications protocols (such as AX25), Use of the Amateur Radio frequency bands: VHF, UHF and S-Band.

A typical student ground segment
--------------------------------
A single, local, groundstation, usually at the host university, Capable of communication on one or two of the Amateur Radio frequency bands, A single rotator and a single elevator to track the spacecraft, A single PC controlling the groundstation hardware and the mission data.

Typical Limitations
-------------------
From ~15 orbits there are around six passes a day, averaging perhaps five minutes each, Satellite is in communications range less than 3% of the mission time, For 97% of the time the groundstation is idle, The groundstation is not configured to communicate with other educational spacecraft, The spacecraft is only configured to communicate with the specific groundstation.

Our approach
============

Advantages of sharing resources
-------------------------------
Provides near-global coverage for all participating missions, Allows for a dramatic increase in mission return, Many critical operations would benefit from having uninterrupted coverage for several hours, Powerful error-correction can be applied when using multiple downlink stations, Mutually beneficial at extremely low risk (original solution serves as backup).