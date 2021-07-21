class Car(object):
    def __init__ (self,model,color,age,topSpeed):
        self.model = model
        self.color = color
        self.age = age
        self.topSpeed = topSpeed

    def start(self):
        print("starting")

    def change(self,speed):
        self.topSpeed = speed

car1 = Car("Honda Civic", "red",3 ,120)
car1.start()
car1.change(100)
print(car1.topSpeed)