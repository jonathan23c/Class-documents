try:
    x = 10
    y = 0
    z = x / y
    print(z)
except:
    print("can't divide a number by zero")

try:
    myfile = open("opera.txt", "w")
    myfile.write("hello there, this is our python class")
    print('file created')
except:
    print("we can't create such a file")


#on a remote module, create a function to be called on your main module.
#allow the function to recieve a list of string items from user and let function
#generate a new list containing only those items with more than 5 characters
#use a while loop to print the generated list

from module2 import listmodule
listmodule()
