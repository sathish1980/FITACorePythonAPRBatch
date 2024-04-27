from FoodOrder.Item import Item


class Invoice(Item):

    itemPrice = "idly-10"
    disountApplicalbeAmount = 500
    discountPercentage = 0.3 #30%
    def GetPrice(self,item):
        splitteditemPrice =self.itemPrice.split("-")
        itemName =splitteditemPrice[0]
        if(itemName==item):
            itemPrice =splitteditemPrice[1]
            print("your one item price is: ",itemPrice)
            return itemPrice
        else:
            print("no item availalbe")
            return 0

    def GetTotalItemPrice(self,item,quantity):
        eachitemPrice =self.GetPrice(item)
        print(int(eachitemPrice))
        if(int(eachitemPrice)>0):
            finalAmount = int(eachitemPrice)*int(quantity)
            print("Final amount is : ",finalAmount)
            return finalAmount
        return 0

    def CalculateDiscount(self,amount):
        if amount>self.disountApplicalbeAmount :
            discountamount = amount*self.discountPercentage
            afterdiscountAmount =amount-discountamount
            print("discount amount : ", discountamount)
            print("You have to pay Rs.  ",afterdiscountAmount)







