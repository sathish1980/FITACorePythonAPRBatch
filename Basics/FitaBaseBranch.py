class FitaBaseBranch():
    name = "Fita Main Branch"
    course =["Java","Python","C#","SQL"]

    def GetMainBranchName(self):
        print(self.name)

    def GetCourses(self,expectedCourse):
        for eachvalue in self.course:
            if(eachvalue==expectedCourse):
                print(eachvalue, " is available")
                break
        print(eachvalue, "is not available")

    def GetCourse(self,expectedCourse):
        for eachvalue in self.course:
            if(eachvalue==expectedCourse):
                return True
        return False



