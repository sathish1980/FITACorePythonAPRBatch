class Set():

    fruits={"apple","orange","pineapple","grapes","apple"}
    newFruits = set({"mango","watermelon"})
    name1 ={"python","java","c#","Testing"}
    name2 ={"python","c#","SQL"}

    def set_implementation(self):
        print(self.fruits)
        print(type(self.fruits))
        print(len(self.fruits))
        print(self.newFruits)
        for eachvalue in self.fruits:
            print(eachvalue)
        if "grapes" in self.fruits:
            print("pass")
        # add
        self.fruits.add("Cherry")
        print(self.fruits)
        #update
        self.fruits.update(self.newFruits)
        print(self.fruits)
        #remove
        self.fruits.remove("pineapple")
        print(self.fruits)
        #discard
        self.fruits.discard("sathish")
        print(self.fruits)
        #pop
        self.fruits.pop()
        print(self.fruits)
        #clear
        #del
       # del self.fruits
        #print(self.fruits)
        """self.name1.difference(self.name2)
        print(self.name1)
        newvalue =self.name1.copy()
        self.name1.difference_update(self.name2)
        print(self.name1)
        print(newvalue)"""
        #newval =self.name1.intersection(self.name2)
        #print(newval)
        """name1 ={"python","java","c#","Testing"}
    name2 ={"python","c#","SQL"}"""
        #self.name1.intersection_update(self.name2)
        print(self.name1)
        print(self.name1.issubset(self.name2))
        print(self.name2.issubset(self.name1))
        print(self.name1.issuperset(self.name2))
        print(self.name1.symmetric_difference(self.name2))






obj = Set()
obj.set_implementation()