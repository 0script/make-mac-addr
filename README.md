#make-mac-addr

##Table of content
* [About the project](#about-the-project)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)

##About the project

    Create random valid mac address

##Technologies

* python3

##Features

* cli , argparseur


##Setup

```shell
$git clone git@github.com:0script/make-mac-addr.git
$cd make-mac-addr.git/
#download hexify.py
$wget https://raw.githubusercontent.com/0script/int-to-hexaString/main/hexify.py
#specify vendor , vendor OUI can be added in the dictionary
$python3 makeMAC.py -n 3 --oui hp
18:60:24:19:7F:7B
18:60:24:F1:D:F8
18:60:24:62:E9:63
```