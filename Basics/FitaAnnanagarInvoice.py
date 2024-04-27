from Basics.FitaAnnanagar import FitaAnnanagar
from Basics.FitaBaseBranch import FitaBaseBranch


class FitaAnnanagarInvoice(FitaAnnanagar,FitaBaseBranch):

    courseFees = ["java-20000","python-25000","c#-12000","SQL-17000"]

    def GetFees(self,course):
        for eachfees in self.courseFees:
            overallvalue =eachfees.split("-")
            if(overallvalue[0]==course):
                print("You have choosed the course : ",overallvalue[0])
                print("You have to pay RS. : ", overallvalue[1])
                break


    def FinalInvoice(self,course):
        if(self.GetCourse(course)):
            self.GetTimeSlot(course)
            self.GetFees(course)


obj =FitaAnnanagarInvoice()
obj.FinalInvoice("SQL")
