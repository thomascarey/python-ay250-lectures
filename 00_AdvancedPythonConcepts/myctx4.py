
import time

def introspect(f):
    
    def wrapper(*arg,**kwarg): # taking in original arguments and keywords
        print("Function name = %s" % f.__name__)
        print(" docstring = %s" % f.__doc__)
        start = time.time()
        if len(arg) > 0:
            print("   ... got passed args: %s " % str(arg))
        if len(kwarg.keys()) > 0:
            print("   ... got passed keywords: %s " % str(kwarg))
        
        x = f(*arg,**kwarg)
        print(time.time() - start)
        return x
    
    return wrapper