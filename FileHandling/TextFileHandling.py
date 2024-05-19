class filehandling():

    """
    read
    readline
    readLines
    """
    def read_File(self):
        filepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\Course.txt"
        file = open(filepath)
        print(file.read())

    def read_Fileonly(self):
        filepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\Course.txt"
        file = open(filepath,"r")
        newFile =file.read()
        allcourses = newFile.split(" ")
        for eachcourse in allcourses:
            if eachcourse=="Testing":
                print("pass")
        print(newFile)

    def read_Filelinebyline(self):
        filepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\Course.txt"
        # open the file
        file = open(filepath,"r")
        # read all the lines from the file
        newFile =file.readlines() # newFile =file.readline() --> read only one line in that file
        # taking line by line
        for eachvalue in newFile:
            listtostring = str(eachvalue)
            allcourses = listtostring.split(" ")
            for eachcourse in allcourses:
                if eachcourse=="Testing":
                    print("pass")
            print(newFile)

    def read_FilelinebylineCount(self,content):
        filepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\Course.txt"
        count =1
        # open the file
        file = open(filepath,"r")
        # read all the lines from the file
        newFile =file.readlines() # newFile =file.readline() --> read only one line in that file
        # taking line by line
        for eachvalue in newFile:
            listtostring = str(eachvalue)
            allcourses = listtostring.split(" ")
            for eachcourse in allcourses:
                if eachcourse==content:
                    count =count+1
            #print(newFile)
        print(content ,count)

    def writeFile(self):
        filepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\output.txt"
        count =1
        # open the file
        file = open(filepath,"a")
        file.write(""" 18-05-2024""")
        file.close()
        print("done")

    def readandWrite(self):
        readfilepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\Course.txt"
        writefilepath = "C:\\Users\\kumar\\PycharmProjects\\FITACorePythonAPRBatch\\Input\\output.txt"

        # open the file
        readfile = open(readfilepath,"r")
        writefile = open(writefilepath, "w")

        #read all lines
        readAllContent = readfile.readlines()
        #write all the content
        for eachvalue in readAllContent:
            if(eachvalue.__contains__("testing")):
                writefile.write(eachvalue)
        writefile.close()
        readfile.close()
        print("read and write is done")





obj = filehandling()
obj.readandWrite()