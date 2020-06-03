from helpers_mod import helpers

helpers.print_details("Ayush",26,[34,67,90,54,78])
print("Result:",helpers.result([34,67,90,54,78]))


from helpers_mod import extras #here we will not get that helpers module message,we will get the print message in the module we are 
              #importing only when we do it the first time in the file
print(extras.name)

#Now what if we want the print message in a module to be dispalyed only when it s run as the main file we will do the one you see in the helpers
#module (We basically use the hidden variable __name__ with a conditional)