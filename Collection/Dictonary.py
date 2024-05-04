class Dictonary():

    userData ={"name":"sathish","age":"50","qualification":"B.tech"}

    def dic_implmentation(self):
        print(self.userData)
        print(len(self.userData))
        print(self.userData["age"])
        print(self.userData.get("qualification"))
        print(self.userData.keys())
        print(self.userData.values())
        print(self.userData.items())
        if "age1" in self.userData:
            print("pass")
        #update
        self.userData["name1"]="raja"
        print(self.userData)
        self.userData.update({"age1":"75"})
        print(self.userData)
        #remove
        #self.userData.pop("age1")
        self.userData.pop("age1","85")
        print(self.userData)
        self.userData.popitem()
        print(self.userData)
        del self.userData["name"]
        print(self.userData)
        self.userData.clear()
        print(self.userData)




obj= Dictonary()
obj.dic_implmentation()