from Basics.Overloading import overloading


class overriding(overloading):

    def add(self,a,b,c):
        d=a-b-c
        print(d)


obj =overriding()
obj.add(10,3,5)