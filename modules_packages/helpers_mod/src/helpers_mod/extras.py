__all__ = ['fun'] #we can put this anywhere in the file
print("WE ARE IN THE EXTRAS MODULE")

from helpers_mod import helpers

name = "Aradhya Rai"

def fun():
    print("This is the fun function inside extras module")


#Now what if we want to hide module entities ?
#Well its not really possible - we have one way or the other to get around that privacy.Still here are some of the methods we follow:

#a) In the module, we make a list var - __all__ = ['names we want to be acceesible']
# BUT THIS WILL ONLY WORK WHEN WE DO : from extras import *
#IT WILL FAIL WHEN WE DO EITHER : import extras / from extras import name-of-the-var-we-want-to-access

#b)we put an underscore before defining the var/func - but it can be again overriden by the above mentioned rules 