class Car(object):
    def __init__(self,Price,Speed,Fuel,Mileage):
        self.Price = Price
        self.Speed = Speed
        self.Fuel = Fuel
        self.Mileage=Mileage

    def display_all(self):
        print "Price :",self.Price
        print "Speed :",self.Speed
        print "Fuel :",self.Fuel
        print "Mileage :",self.Mileage
        if  self.Price > 10000:
            self.Tax = 0.15
        else:
            self.Tax = 0.12
        print "Tax:",self.Tax
        print ''
        return self

car1= Car(2000,"35mph","Full","15mpg")
car1.display_all()
car2=Car(200,"5mph","Not Full","105mpg")
car2.display_all()
car3=Car(2000,"15mph","Kind of Full","95mpg")
car3.display_all()
car4=Car(2000,"25mph","Full","25mpg")
car4.display_all()
car5=Car(2000,"45mph","Empty","25mpg")
car5.display_all()
car6=Car(20000000,"35mph","Empty","15mpg")
car6.display_all()


    