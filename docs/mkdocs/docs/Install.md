#Set-up Instructions
---
appJar was designed for use in schools - it therefore doesn't require any kind of special  *installation*.  
Instead, just [DOWNLOAD](https://github.com/RWBA/appJar/blob/appJar/releases/appJar.zip?raw=true) the ZIP file, unzip, and go - just put the folder in the [right place](/install/#single-user-set-up).  

##Pip Installation  
However, if you can install python packages - we support that too!  

`sudo pip3 install appjar` - this will download & install **appJar** ready for python 3.  
`sudo pip3 install appjar --upgrade` - this will upgrade **appJar** to the latest version.  
```python
# import the appJar library
from appJar import gui
```

##Single-user Set-up  
If you can't/don't want to install using pip, simply:  

* [DOWNLOAD](https://github.com/RWBA/appJar/blob/appJar/releases/appJar.zip?raw=true) **appjar** and unzip it.  
* Put the **appJar folder** in your **code folder**, and you're done!  

```python
# import the appJar library
from appJar import gui
```
(As long as it's in the same folder as your code, it'll work...)  

##Multi-user Set-up  
If you're trying to install appJar in a school, everyone can download their own copy ([see above](/install/#single-user-set-up)), or:  

* Put the **appJar folder** in a **shared location** (eg. a folder on a network drive): `E:\PYLIB`  
* Then have pupils include the following 2-lines at the start of their code:

```python
# add the appJar folder to your PATH
import sys
sys.path.append("E:\PYLIB")
# import the appJar library
from appJar import gui
```

##Advanced Set-up  
If you've got friendly technicians, you can even avoid having to always add **appJar** to your path...  

###Windows
----
Create an environment variable, which will mean `E:\PYLIB` is always in your **path**.  

* Open **Control Panel**  
* Navigate to **System -> Advanced System Settings**  
![System](img/w_install_1.png)
* Click the **Advanced** tab  
![System](img/w_install_2.png)
* Under **System variables**, click the **New..** button  
![System](img/w_install_3.png)
* Set the **Variable name:** to be **PYTHONPATH**  
* Set the **Variable value:** as the folder you put **appJar** in (eg. "E:\PYLIB")  
![System](img/w_install_4.png)
* Press **OK**, and you're done!    

###Linux (Raspberry Pi) /MacOS 
----
If you're running python from a terminal:  

* Type the following:  
```bash
    echo 'export PYTHONPATH="${PYTHONPATH}:~/Documents/PYLIB"' >> ~/.bashrc
```
* Reopen the terminal (or type `source ~/.bashrc`), and you're done!  
* **NB.** Change `~/Documents/PYLIB` to the folder where the **appJar folder** is located.  

###IDLE on Linux (raspberry Pi)/MacOS  
----
If you're running python in  IDLE, you'll need to add appJar to your **site-packages**  

* Launch a **Terminal**  
* Type the following:  
```bash
    mkdir -p ~/Library/Python/3.4/lib/python/site-packages
    cd ~/Library/Python/3.4/lib/python/site-packages
    echo '~/Documents/PYLIB' > appJar.pth
```
* Close the terminal, and you're done!  
* **NB.** you'll need to make sure the version number (3.4) is correct.  
    * To check your version, run this in Python:  
```python
    import sys
    print(sys.version) 
```
