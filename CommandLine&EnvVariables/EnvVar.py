import os

## before executing os.getenv
## execute export <argument> that you want to read
## example 
## 1. execute "eport OLDPWD=/workspaces/python"
## 2. read os.getenv("OLDPWD") 

print(os.getenv("OLDPWD"))