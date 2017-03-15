#Packaging appJar Apps ![PyInstaller](img/pyinstaller-draft1a-100_trans.png)
---

The recomended way to package appJar is to use [PyInstaller](http://www.pyinstaller.org)  

Simply [download](https://github.com/pyinstaller/pyinstaller/releases/download/v3.2.1/PyInstaller-3.2.1.zip) PyInstaller and [install](https://pyinstaller.readthedocs.io/en/stable/installation.html) it.  

pyinstaller -p <PATH_TO_APPJAR> --onefile --windowed demo.py
