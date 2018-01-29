
def entryExit(f):
    
    def new_f():
        print("Entering", f.__name__)
        x = f() # set value of execution of function
        print("hello, goodbye")
        print("Exited", f.__name__)
        return x
    return new_f # return function, but wrapped as something else

@entryExit
def func1():
    print("inside func1()")

@entryExit
def func2():
    print("inside func2()")
    y = "yeah!"
    return y

# logic: grab func2 (which is the value of f), now grab name of f, print that we've entered it, evaluate function (func2, returns y), and return back to original caller this value "yay"