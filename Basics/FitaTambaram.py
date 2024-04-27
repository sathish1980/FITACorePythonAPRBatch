from Basics.FitaBaseBranch import FitaBaseBranch


class FitaTambaram(FitaBaseBranch,):
    branchName = "FitaTambaram"
    javatiming = ["9.00 AM - WeekDay", "7.00 PM - WeekDay", "11.00 AM - WeekEnd"]
    pythontiming = ["10.00 AM - WeekDay", "3.00 PM - WeekDay", "9.00 AM - WeekEnd"]
    Csharptiming = ["11.00 AM - WeekDay", "9.00 PM - WeekDay", "12.00 AM - WeekEnd"]
    SQLtiming = ["1. 8.00 AM - WeekDay", "2. 2.00 PM - WeekDay", "3. 10.00 AM - WeekEnd"]

    def GetTambaramBranchName(self):
        print(self.branchName)

    def GetTimeSlot(self, course):
        print(" We have below time slot")
        if (course == "java"):
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
            print("We dnt have a slot for ", course)
        userinput = input("please choose your slot: :")
        print("you have choosed slot no: ", userinput)

    def GetTambaramCourse(self,course):
        if(self.GetCourse(course)):
            self.GetTimeSlot(course)

obj=FitaTambaram()
obj.GetTambaramCourse("SQL")