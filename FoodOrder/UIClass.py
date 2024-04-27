from FoodOrder.Invoice import Invoice


class UIClass(Invoice):

    def GetOrdersOnline(self,hotel,item):
        if self.Hotel_Exist(hotel)==True:
            if self.Item_Exist(item):
                self.GetPrice(item)

    def GetOrdersFromStore(self,):
        hotel =input("Enter Hotel Name: ")
        if self.Hotel_Exist(hotel)==True:
            item = input("Enter Item Name: ")
            if self.Item_Exist(item):
                qty = input("Enter total qty: ")
                print(type(qty))
                totalAmount = self.GetTotalItemPrice(item,qty)
                print(type(totalAmount))
                self.CalculateDiscount(int(totalAmount))


obj =UIClass()
obj.GetOrdersFromStore()