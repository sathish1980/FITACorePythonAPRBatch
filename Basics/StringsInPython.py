class StringInPython():

    name = " sathish Kumarssdsdsd "
    findMe = "Hi this is sathish from tambaram"
    Course = "Hi i hav choose \"JAVA\" in \"FITA\""
    name1=""

    def StringImplementation(self):
        count=0
        print(self.name)
        print(len(self.name))
        print(self.name[len(self.name)-1])
        for eachchar in self.name:
            print(eachchar)
            if(eachchar=="s" or eachchar=="S"):
                count+=1
        print("S present ",count," times")
        print("sathishkumar" in self.findMe)
        print("sathishkumar" not in self.findMe)
        if("sathish" in self.findMe):
            print("i am sathish")
        print(self.name[1:4])
        self.name1 =self.name.upper()
        print(self.name.upper())
        print(self.name.lower())
        print(self.name.capitalize())
        print(self.name.strip())
        print(self.name.lstrip())
        print(self.name.rstrip())
        print(self.name.replace("Kumar","Ku"))
        print(self.name.split(" "))
        print(self.name+self.findMe)
        print(self.name1)
        print(self.Course)
        print(self.name.count("s"))
        print(self.name.endswith(" d"))
        print(self.name.startswith(" s"))
        print(self.name.find("Kumar"))
        print(self.name.isalnum())

    def newfuction(self):
        print(self.name1)





obj=StringInPython()
obj.StringImplementation()
obj.newfuction()