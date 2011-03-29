p0wn 
====

p0wn is a small python system designed to run a set of binaries as a service on Windows.
This can be useful when a set of binaries need to be run in the background and managed
as a set rather than being managed individually (such as XAMPP or other similar systems).


Dependencies
============

p0wn depends on the following libraries

* py2exe
* pywin32
* pyyaml for configuration

History
=======

p0wn was originally written with the intention of running nginx, PHP, and MySql
in the background on Windows system and worked quite well in the capacity.