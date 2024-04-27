from Basics.FitaBaseBranch import FitaBaseBranch


class FitaAnnanagar():

    branchName = "FitaAnnanagar"
    javatiming = ["10.00 AM - WeekDay","6.00 PM - WeekDay","10.00 AM - WeekEnd"]
    pythontiming = ["11.00 AM - WeekDay", "5.00 PM - WeekDay", "10.00 AM - WeekEnd"]
    Csharptiming = ["12.00 AM - WeekDay", "9.00 PM - WeekDay", "12.00 AM - WeekEnd"]
    SQLtiming = ["1. 6.00 AM - WeekDay", "2. 4.00 PM - WeekDay", "3. 9.00 AM - WeekEnd"]

    def GetAnnanagarBranchName(self):
        print(self.branchName)

    def GetTimeSlot(self,course):
        print(" We have below time slot")
        if(course=="java"):
            for eachtiming in self.javatiming:
                print(eachtiming)
        elif (course == "python"):
            for eachtiming in self.pythontiming:
                print(eachtiming)
        elif (course == "c#"):
            for eachtiming in self.Csharptiming:
                print(eachtiming)
        elif (course == "SQL"):
            for eachtiming in self.SQLtiming:
                print(eachtiming)
        else:
            print("We dnt have a slot for ",course)
        userinput = input("please choose your slot: :")
        print("you have choosed slot no: ",userinput)

    def FinalFlow(self,course):
        self.GetAnnanagarBranchName()
        if(self.GetCourse(course)):
            self.GetTimeSlot(course)
        else:
            print("Requested course is not available in this branch")





