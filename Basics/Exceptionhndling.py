class Exception_Handling():

    def Div(self,a,b):
        try:
            c=a/b
            try:
                print(c)
            except:
                pass
        except ZeroDivisionError:
            # pass
            print("Hey ! you are trying to divide by zero please check your 2nd param")
        except:
            print(Exception)

        finally:
            print("I am finally")


    def add(self,a,b):
        c=a+b
        print(c)

obj = Exception_Handling()
obj.Div(10,5)
obj.add(3,4)