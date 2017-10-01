#Packaging appJar Apps ![PyInstaller](img/pyinstaller-draft1a-100_trans.png)
---

The recommended way to package appJar is to use [PyInstaller](http://www.pyinstaller.org)  

Simply [download](http://www.pyinstaller.org/downloads.html) and [install](https://pyinstaller.readthedocs.io/en/stable/installation.html) PyInstaller.  

If everything has been installed via pip, then you should be able to package your application with the following command:

```pyinstaller -F -w demo.py```

If not, then you may need to specify the path of certain libraries:  

```pyinstaller -F -w -p <path_to_appJar> demo.py```

###Setting an app Icon
---
To set an icon for the app, include the following option:

```pyinstaller -i <path_to_icon> -F -w demo.py```

###Including Images
---
To include images, include the following option:

```appinstaller --add-data image.png:. -F -w demo.py```

###Platform Support
---
This has been tested & works under both Windows & Linux, although no success (yet) on OSX.  

A lot more detail will be provided here, in a future release, on the exact process to follow to get everything built into  your package.  
