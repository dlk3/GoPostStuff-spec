#  GoPostStuff RPM Package For Fedora/CentOS

This folder contains the files necessary to create a RPM package for the
GoPostStuff application.  I created this for myself as there is no
official RPM package for this application.

GoPostStuff is a simple utility for posting files to UseNet binary news 
groups.  See https://github.com/madcowfred/GoPostStuff for details. 

I have created a Fedora COPR repository to support the installation of
the RPMs I created.  To install opentracker from this repository do:
```
$ sudo dnf copr enable dlk/rpms
$ sudo dnf install GoPostStuff
