# Git Guide
----  
Below are some useful commands for using git, GitHub & PyPI from the command line.  

##Simple Set-up

[Git](https://git-scm.com/) provides local version control - allowing you to keep backups of previous versions of your code.  

It's really easy to get started:  

* `git init` - will initialise Git for your current project,  
* `git add [filename]` - will queue a new file or changes to an existing file to be saved  
* `git commit` - will save the new versions of the files you've added - with a message describing the changes.  

That's it, you now have full **version control** over your code.  
It works in Windows, OSX or Linux and is supported by most popular IDEs (including Visual Studio).  

You can even take it a step further, by sharing your code on the Web.  
[GitHub](http://github.com) provides a free place to sink & share your code.  
It will also allow other people to view & contribute to your code.  

You first need to **create** an account on GitHub, and then a new **repo**:  

![new repository](/img/git/repoCreate.png)  

Then copy your repo's address, and **add** it to your local git account:  

* `git remote add origin [web_address]` - link your local Git repo to a GitHub repo.  

Then, once you've **commited** local changes, you can **push** them to GitHub:  

* `git push` - send your local changes to your online GitHub repository.  

##Reference

### Setting Up  
* `git init`  
Creates a new local git repository, in the current directory  
* `git remote add origin [URI]`  
This will link your newly created, local repository, with the one specified on GitHub  
* `git clone [URI]`  
This will copy a git repository, from GitHub, to the current directory  

### Updating
* `git remote update`  
This will update your log of remote changes  
* `git pull`  
This will get any changes from GitHub, and update your local copy  

### Checking  
* `git status`  
This will compare your local copy, with the copy on GitHub, and tell you any differences.  

### Adding  
* `git add [file]`  
Add a new file to your local repository  
* `git add .`  
Add any changes you've made to your local repository  
* `git commit -m "message here"`  
Commit anything you've added to your local repository  
* `git commit -a -m "message here"`  
Combines `add` and `commit` Syncing all changes to your local repository  

### Undoing  
* `git checkout XXX`  
This will restore a file to the latest version in Git.  

### Pushing  
* `git push`  
Pushes all changes you've added & committed locally, to GitHub  

### Tagging
* `git tag -a vXXX -m "Tag description`  
* `git push origin vXXX`  
This tags the current build in git  
Then pushes it to GitHub

## PyPI  
* `python setup.py register -r pypitest`  
This will register the package with PyPI Test  
* `python setup.py sdist upload -r pypitest`  
This will upload the stuff to PyPI Test  
* `pip install --verbose --index-url https://testpypi.python.org/pypi appJar  `  
This will attempt to install from the PyPI test server  
