class Conditions():

    def ifConditions(self,vehicle_Type, TypeofVehicle, patientExistorNot):
        if(vehicle_Type=="Green"):
            print("you are good to go")
        elif(vehicle_Type=="Red"):
            if(TypeofVehicle=="Ambulance" and patientExistorNot==True):
                print("Hey ! You are ambulance good to go")
            else:
             print("You have to stop")
        elif (vehicle_Type == "Orange"):
            print("You are about to start/stop")
        else:
            print("Not a valid color")

    def amount(self,myAmount):
        if(myAmount>1000):
            pass

obj=Conditions();
obj.ifConditions("Red","bike",False)
