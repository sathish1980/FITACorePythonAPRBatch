import csv
class csvConcept():

    def readCSV(self):
        filepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\invoice.csv"
        with open(filepath, mode='r') as file:
            csvFile = csv.reader(file)

            for eacline in csvFile:
                print(eacline)
        print("done")

    def writeCSV(self):
        filepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\invoiceout.csv"
        rows = [['Nikhil', 'COE', '2', '9.0'],
                ['Sanchit', 'COE', '2', '9.1']]
        with open(filepath, mode='w') as file:
            csvFile = csv.writer(file)
            csvFile.writerows(rows)
        print("done")

    def readandWriteCSV(self):
        readFilepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\invoice.csv"
        writefilepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\invoiceout.csv"

        with open(readFilepath, mode='r') as file:
            with open(writefilepath, mode='w') as writefile:
                csvFile = csv.reader(file)
                print(type(csvFile))
                for eacline in csvFile:
                    if eacline.__contains__("java"):
                        writecsvFile = csv.writer(writefile)
                        writecsvFile.writerow(eacline)

        print("done")

obj =csvConcept()
obj.readandWriteCSV()

