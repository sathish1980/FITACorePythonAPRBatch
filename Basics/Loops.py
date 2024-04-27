class Loops():

    def __init__(self,a):
        print("constructor",a)

    def print10Number(self):
        print(1)
        print(2)
        print(3)
        print(4)
        print(5)
        print(6)
        print(7)
        print(8)
        print(9)



    def whileLoops(self,startingValue , endValue):
        while(startingValue <=endValue):
            startingValue += 1
            if (startingValue == 10 or startingValue==14):
                continue
            print(startingValue)

            #startingValue=startingValue+1

    def whileLoopsreverse(self,startingValue , endValue):
        while(endValue >=startingValue):
            print(endValue)
            endValue-=1

    def forloop(self):
        age =30
        fruits =["apple","orange","banana","grapes","watermelon"]
        for eachFruit in fruits:
            if(eachFruit=="banana"):
                continue
            print(eachFruit)
        #age =[1,5,6,80,35,45,23]
        for eachnumber in range(1,100):
            print(eachnumber)

obj= Loops(2)
#obj.print10Number()
#obj.whileLoops(5,15)
obj.forloop()
obj.whileLoopsreverse(90,100)