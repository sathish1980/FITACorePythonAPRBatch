class Tupleimplmentation():

    fruits=("orange","apple","pineapple","mango","grapes","mango")
    newFruits =["mulberry","blueberry","strawberry"]
    def getFruits(self):
        print(self.fruits)
        print(type(self.fruits))
        # retrieve
        print(self.fruits[0:3])
        print(self.fruits[4])
        print(self.fruits[-1])
        print(len(self.fruits))
        #self.fruits[1]="Green apple"
        #del self.fruits
        print(self.fruits.count("mango"))
        print(self.fruits)
        #self.newFruits.extend(self.fruits)
        newlist =list(self.fruits)
        print(type(newlist))
        print(self.newFruits)
        print(self.fruits)



obj = Tupleimplmentation()
obj.getFruits()