# *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 
def myFun(*args):
    for arg in args:
        print(arg)
 
myFun('Hello', 'Welcome', 'to', 'my Assignment')

# **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
myFun(first='Geeks', mid='for', last='Geeks')
