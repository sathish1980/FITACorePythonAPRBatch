from FileHandling.ExcelRead import ExcelRead


class Invoice(ExcelRead):

    def Fees_Paid(self,StudentFeesInfo):
        print(self.ReadData("Student")[StudentFeesInfo])


obj = Invoice()
obj.Fees_Paid("NameFT2")
obj.Fees_Paid("StatusFT2")