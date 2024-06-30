from threading import *;
import time


class Threadconcept(Thread):

    def add(self):
        for x in range(0,10):
            print("add")
            #print("add: " ,a+b)
            time.sleep(1)


    def run(self):
        self.add()

class another(Thread):

    a =0
    b =0
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b

    def sub(self):
        for x in range(0, 10):
            print("sux")
            print("sub: ", self.a-self.b)
            time.sleep(2)

    def run(self):
        self.sub()



t2 = another(10,20)
t1 = Threadconcept()
t1.start()
t2.start()
#t1.join()

#obj.add()
#obj.sub()
