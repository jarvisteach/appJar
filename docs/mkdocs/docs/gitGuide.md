# Git Guide
----  
Below are some useful commands for using git & GitHub from the command line.  

## Setting Up  
* `git init`  
Creates a new local git repository, in the current directory  
* `git remote add origin [URI]`  
This will link your newly created, local repository, with the one specified on GitHub  
* `git clone [URI]`  
This will copy a git repository, from GitHub, to the current directory  

## Updating
* `git remote update`  
This will update your log of remote changes  
* `git pull`  
This will get any changes from GitHub, and update your local copy  

## Checking  
* `git status`  
This will compare your local copy, with the copy on GitHub, and tell you any differences.  

## Adding  
* `git add [file]`  
Add a new file to your local repository  
* `git add .`  
Add any changes youve made to your local repository  
* `git commit -m "message here"`  
Commit anything you've added to your local repository  
* `git commit -a -m "message here"`  
Combines `add` and `commit` Syncing all changes to your local repository  

# Pushing  
* `git push`  
Pushes all changes you've added & commited locally, to GitHub  
