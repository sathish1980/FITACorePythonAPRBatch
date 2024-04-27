from Basics.Ferrari import Ferrari


class BMW:

    def fuel_type(self):
        print("petrol")

    def fuel_capacity(self):
        print("capactiy is 40 L")

    def MAx_speed(self):
        print("mas speed is 400KMPH")

ferrai =Ferrari()
bmw=BMW()
for car in (ferrai,bmw):
    car.fuel_type()
    car.fuel_capacity()
    car.MAx_speed()
