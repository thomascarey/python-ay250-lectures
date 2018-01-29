import time

class MyDecor1:
    
    def __init__(self,expression="None"):
        self.expression = expression
        print("init",time.time())

    def __enter__(self):
        print("Entered a wonderful technicolor world. Build it up") 
        print("enter",time.time())
        print(eval(self.expression))
        return self #eval(self.expression) # self = entire instance of the class itself - effectively just printing expression

    def __exit__(self,*args):
        print("exit",time.time())
        print("...exiting this wonderful world. Tear it down.")