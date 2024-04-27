from FoodOrder.Hotel import Hotels


class Item(Hotels):
    itemList = "idly"

    def Item_Exist(self, itemName):
        if (itemName == self.itemList):
            print("Item Exist")
            return True
        else:
            print(itemName," Is Not avaialable")
            return False