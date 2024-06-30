import re

class regex():
    def find_all(self):
        txt = "The rAin in Spain and Spain"
        x = re.findall("in.+i", txt)
        print(x)

    def search_func(self):
        txt1 = "The rain in Spain"
        x = re.search("z", txt1)
        print(x)

    def split_func(self):
        txt = "The rain in Spain"
        x = re.split("z", txt)
        print(x)

    def replace_fun(self):
        txt = "The rain in Spain"
        x = re.sub("[a-i]", "A", txt)
        print(x)

    def invoice(self,quantity,itemno,price):
        myorder = "I want {} pieces of item number {} for {:.2f} dollars."
        print(myorder.format(quantity, itemno, price))



obj = regex()
obj.replace_fun()
obj.invoice(10,111,12.34353535)
obj.invoice(5,112,100)