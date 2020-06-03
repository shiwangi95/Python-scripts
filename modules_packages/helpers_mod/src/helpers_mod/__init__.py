#how to install a package/project from PyPI(Python Package Index) 
#use : pip install packagename
#pip --help ------------------will give you all the cmds we can use with pip

#PyPA - Python Packaging authority - provides sample projects for creating installable packages

#how to create a package that is installable?

#make sure you have pip installed as a utility
#a)helpers_mod/src/helpers_mod(the last helpers_mod is the one that we had created previously)

#b)move the .py files to the shifted location of helpers_mod

#c)if you have to make a folder a package in python we conventionally include __init__.py file(it is not mandatory)

#d)curl -O https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py - we do this to include setup.py file in the first helpers_mod

#e)In setup.py file we basically have two main imp things : setup() and find_packages() [both are imported from setuptools module]

#f)

