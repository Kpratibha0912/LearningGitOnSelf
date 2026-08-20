from UnderstandingOfConcepts import oopsClassAndObject

class DriveCar(oopsClassAndObject.Engine):
    def carModel(self):
        print("Honda City")

    def driveCar(self):
        oopsClassAndObject.Engine.startEngine(self)
        oopsClassAndObject.Engine.stopEngine(self)


myCar = DriveCar()
myCar.carModel()
# myCar.driveCar()