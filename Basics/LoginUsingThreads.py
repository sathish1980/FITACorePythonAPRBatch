import time
from threading import *;

import mysql.connector
from mysql.connector import Error


class SQLREAD(Thread):

    loginDetails=[]
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 database='fitapython',
                                                 user='root',
                                                 password='Admin@123')
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                #print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                #print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        """finally:
            if self.connection.is_connected():
                cursor.close()
                self.connection.close()
                print("MySQL connection is closed")"""
    def Get_DataFromSQL(self):
        self.connect()
        sql_select_Query = "select username,password from Login where status ='Active'"
        cursor = self.connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        #print("Total number of rows in table: ", cursor.rowcount)
        for eachRow in records:
            #print(eachRow)
            self.loginDetails.append(eachRow)
            #print("Id = ", eachRow[0], )
            #print("coursename = ", eachRow[1])
        #print("Fetch Done")
        #print(self.loginDetails)

    def run(self):
        self.Get_DataFromSQL()


class GetUserInput(Thread):

    def Login_Details(self):
        username = input("Enter username: ")
        time.sleep(1)
        password= input("Enter password: ")
        #time.sleep(2)
        for eachvalue in SQLREAD.loginDetails:
            if(eachvalue[0]==username and eachvalue[1]==password):
                print ('Hi' , eachvalue[0])
                print("your login is Sucessfull enjoy the day")
                return
        print("your login is not Sucessfull please check your credentials")


    def run(self):
        self.Login_Details()


obj =SQLREAD()
obj.start()
obj= GetUserInput()
obj.start()
