class userInput():
    dob = 0
    def GetMYName(self):
        name = input("Enter your name: ")
        print("My Name is : ", name)

    def GetMyAge(self):
        self.dob = input("Enter your date of birth year :")
        currentyear = 2024
        actualage = currentyear-int(self.dob)
        print("My age is : ", actualage)

    def myNewAge(self):
        print("My dob is : ",self.dob)

obj = userInput();
obj.GetMYName()
#obj.GetMyAge()
obj.myNewAge()