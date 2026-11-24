# #method overriding example

# # class animal:
# #     def sound(self):
# #         print("Animal makes a sound")

# # class atul(animal):
# #     def sound(self):
# #         super().sound()
# #         print("Dog barks")

# # class priya (animal):
# #     def sound(self):
# #         print("Cat meows")

# # a1 = animal()
# # d1 = atul()
# # c1 = priya()        

# # class Calculator:

# #     def add(self, a, b, c=0):

# #         print("Addition:", a + b + c)


# # obj = Calculator()

# # obj.add(10, 20)

# # obj.add(10, 20, 30)

# # class Calculator:

# #     def add(self, *numbers):

# #         total = 0

# #         for num in numbers:
# #             total = total + num

# #         print("Addition:", total)


# # obj = Calculator()

# # obj.add(10, 20)

# # obj.add(10, 20, 30)

# # obj.add(10, 20, 30, 40)


# # import numbers


# # class calulator:

# #     def multiply(self, *numbers):

# #         total = 1

# #         for num in numbers:
# #             total = total * num

# #         print("multiplication:", total)

# # obj = calulator()
# # obj.multiply(20, 30, 40)
# # obj.multiply(10, 20, 30)

# #division

# # import numbers


# # class calculator:

# #     def divide(self, *numbers):
# #         total = 1

# #         for num in numbers:
# #             total = total / num

# #         print("division:", total)

# # obj = calculator()
# # obj.divide(5,5,10,20)
# # obj.divide(10, 20, 30)    


# #abstract method


# # from abc import ABC, abstractmethod

# # # Parent Abstract Class
# # class Animal(ABC):

# #     @abstractmethod
# #     def sound(self):
# #         pass


# # # Child Class
# # class Dog(Animal):

# #     def sound(self):
# #         print("Dog barks")


# # # Child Class
# # class Cat(Animal):

# #     def sound(self):
# #         print("Cat meows")


# # # Creating objects
# # d = Dog()
# # c = Cat()

# # d.sound()
# # c.sound()


# # from abc import ABC, abstractmethod

# # # Abstract parent class
# # class Shape(ABC):

# #     # Child classes must implement this method.
# #     @abstractmethod
# #     def area(self):
# #         pass


# # class Rectangle(Shape):

# #     def __init__(self, length, width):
# #         self.length = length
# #         self.width = width

# #     # Implement the required method.
# #     def area(self):
# #         return self.length * self.width

# # class Circle(Shape):

# #     def __init__(self, radius):
# #         self.radius = radius

# #     def area(self):
# #         return 3.14 * self.radius ** 2

# # # Create a concrete object.
# # r1 = Rectangle(5, 3)
# # c1 = Circle(4)
# # print("Area:", c1.area())

# # print("Area:", r1.area())
        


# from abc import ABC, abstractmethod


# class car(ABC):
#     @abstractmethod
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model

#     @abstractmethod
#     def display(self):
#         print("Car Name:", self.name)
#         print("Car Model:", self.model)

# class electriccar(car):
#     def __init__(self, name, model, battery_capacity):
#         super().__init__(name, model)
#         self.battery_capacity = battery_capacity

#     def display(self):
#         super().display()
#         print("Battery Capacity:", self.battery_capacity)

# car1 = car("Toyota", "Camry")
# car1.display()
# electric_car1 = electriccar("Tesla", "Model S", "100 kWh") 
# electric_car1.display()


# from abc import ABC, abstractmethod


# class car(ABC):
#     @abstractmethod
#     def breakK(self):
#          pass
#     @abstractmethod
#     def clutch(self):
#         pass
# class BMW(car):
#     def breakK(self):
#         print("BMW break")
#     def clutch(self):
#         print("BMW clutch")
# obj=BMW()        
# obj.breakK()
# obj.clutch()


# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def stop(self):
#         print("Brake dabaya — bachiyaaa oyeeeee ting ning ning.")

# car = Car()
# answer = input("Brake dabao? (yes/no): ")

# if answer.lower() == "yes":
#     car.stop()
# else:
#     print("Brake nahi dabaya — oyiyaaaaa solaaaa!")



from abc import ABC, abstractmethod
class Car(ABC):

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def accident(self):
        pass
class MyCar(Car):

    def brake(self):
        print("Car Stopped Safely.")

    def accident(self):
        print("Accident !")

car = MyCar()
choice = input("Press B for Brake or A for Accident: ").lower()
if choice == "b":
    car.brake()
elif choice == "a":
    car.accident()
else:
    print("Invalid Choice!")

















































































































