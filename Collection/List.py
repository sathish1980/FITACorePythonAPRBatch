class listConcepts():

    hotels =["SVB","A2B","SRR","PSV","B2B","SVB"]
    nonvegHotel =["bilal","hyderab briyani"]
    SVBItem =["idly-10","dosa-19"]
    A2BItem =["idly-15","pongal-19"]
    hotalavailable =False
    def GetHotel(self):
        print(self.hotels)
        # specific value
        print(self.hotels[0])
        print(self.hotels[2])
        print(self.hotels[1:4])
        print(self.hotels[-1])
        #total value
        print(len(self.hotels))
        print(self.hotels[len(self.hotels)-1])
        """for eachval in self.hotels:
            if eachval=="A2B":
                print("hotel is avaialble")
                hotalavailable=True
                break
        if(hotalavailable==False):
            print("hotel is not avaialable")"""

        if "BKK" in self.hotels:
            print("hotel is avaialble")
        else:
            print("hotel is not avaialble")
        self.hotels[1:7]=["Hot Chips","balaji bhavan","parvathi bhavan","1","2","3"]
        print(self.hotels)
        self.hotels[2]="BH" # replace the value in the given index
        self.hotels.insert(2,"BH") # it will newly insert the value in the given position
        print(self.hotels)
        self.hotels.append("last hotel")
        print(self.hotels)
        self.hotels.extend(self.nonvegHotel)
        print(self.hotels)
        self.hotels.remove("BH")
        print(self.hotels)
        self.hotels.pop(5)
        print(self.hotels)
        self.hotels.pop()
        print(self.hotels)
        del self.hotels[3]
        print(self.hotels)
        #del self.hotels
        newHotels = self.hotels.copy()
        self.hotels.clear()
        print(self.hotels)
        for eachval in self.hotels:
            print(eachval)
        print(type(self.hotels))
        self.hotels.sort(reverse=False)
        print(self.hotels)
        print(newHotels)



obj = listConcepts()
obj.GetHotel()