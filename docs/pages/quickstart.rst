1) J2SPOT quickstart!!!...
=======================

J2SPOT is  a simple TCP honeypot for your system written in Python3.

2) How to install (installation):
++++++++++++++++++++++++++++++

  python -m pip install J2SPOT
  
3) Running:
**********

  python -m J2SPOT
  
4) BUILD DEBIAN PACKAGE:
""""""""""""""""""""""""
  download the package from github releases or build the package
  
Building the debian package:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-->dpkg-deb --build ./deb J2SPOT-1.0.0.deb

Installing after building:
^^^^^^^^^^^^^^^^^^^^^^^^^^
-->dpkg -i J2SPOT-1.0.0.deb
 
""To enable the honeypot-J2SPOT service in your system --type: ""
 
-->"" sudo systemctl enable J2SPOT""(FOR EXPLICIT CASE)
 
 ///[TO SEE THE LOGS GO TO ] :
 
   "/var/log/J2SPOT.log".
   
  [config defaults to]:
  
  "/etc/J2SPOT.ini". 
  
  
 

6) Source code:
##############

-->Https://github.com/codingpsych72/J2SPOT

7) Documentation:
@@@@@@@@@@@@@@@@


-->https://J2SPOT.rtfd.io
