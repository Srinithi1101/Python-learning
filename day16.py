#Inherintance
# class animals:
#     def __init__(self,name,is_alive):
#         self.name=name
#         self.is_alive=is_alive
#     def eat(self):
#         print(f"{self.name} is eating")
# class Dog(animals):
#     pass
# class cats(animals):
#     pass
# dog=Dog("scooby",True)
# print(dog.name)            
# dog.eat()
# print(cats.name)
# cats.eat()

#subcls
# class animals:
#      def __init__(self,name,is_alive):
#          self.name=name
#          self.is_alive=is_alive
#      def eat(self):
#          print(f"{self.name} is eating")
# class Dog(animals):
#      def speak(self):
#           print("Woof")
# class Cat(animals):
#      def speak(self):
#           print("Meow")
# dog=Dog("scooby",True)
# cat=Cat("Tom",True)
# print(dog.name)            
# dog.eat()
# print(cat.name)
# cat.eat()
# dog.speak()
# cat.speak() 

#Task
# class vehicle:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
#     def show_methods(self):
#         print(f"{self.brand}  is moving")
#         print(f"{self.speed} speed is high ")
# class Car(vehicle):
#     def drift(self):
#         print(f"{self.brand} is drifting")
# class Bike(vehicle):
#     def wheeling(self):
#         print(f"{self.brand} is wheeling")
# car=Car("BMW",200)
# bike=Bike("Enfield",150)
# print(car.show_methods)     
# car.show_methods()
# print(bike.show_methods)
# bike.show_methods()
# car.drift()
# bike.wheeling()                      

#Polymorphism
class Dog:
    def sound(self):
        print("Woof!")
class Cat:
    def sound(self):
        print("Meow!")
class Cow:
    def sound(self):
        print("Moof!") 
# dog=Dog()
# dog.sound()
# cat=Cat()
# cat.sound()
# cow=Cow()
# cow.sound() 
# 
# oru line print call
animals=[Cat (),Dog(),Cow()]
for animal in animals:
    animal.sound()
    
     