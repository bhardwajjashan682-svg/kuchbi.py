#  oops concept

#  class car:
#      def startengine(self):
#          print("start engine")

#  car1 = car()
# car1.startengine()



#  Calculator

#  class calculator:
#      def calculator1(self, a, b):
#         print("Addition:", a + b)
#         print("Subtraction:", a - b)
#         print("Multiplication:", a * b)
#         print("Division:", a / b)


# cal = calculator()
# cal.calculator1(10, 5)

# # Creating a class
# class Car:
#     # Method inside the class
#     def start(self):
#         print("Car is starting")

# # Creating an object
# car1 = Car()

# Calling the method
# # car1.start()
#     def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# # #     def display(self):
# # #         print("Name:", self.name)
        ##print("grade",self.grade)

# s1 = student("Rahul", 20,"B")
# # s2 = student("Priya", 21,"C")

# # s1.display()
# # s2.display() 


# # 

# #inheritance BASIC INHERITANCE    

# class Animal:
#     def speak(self):
#         print("Animal speaks")  

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# d1 = Dog()
# d1.speak()  # Output: Dog barks 

# #super() function

# class employee:
#     def __init__(self, name ):
#         self.name = name
#     def display(self):
#         print(self.name)
# class manager(employee):
#     def __init__(self, name, department):
#         super().__init__(name)
#         self.department = department

# m = manager("John", "it")
# m.display()  # Output: John

# print(m.department)     
# print(m.name)  
        



# class Employee:
#     def attend_meeting(self):
#         print("Employee is attending a meeting")


# class Trainer:
#     def teach_students(self):
#         print("Trainer is teaching students")


# class CorporateTrainer(Employee, Trainer):
#     def conduct_session(self):
#         print("Conducting a corporate training session")


# t1 = CorporateTrainer()

# t1.attend_meeting()  # From Employee
# t1.teach_students()  # From Trainer
# t1.conduct_session() # Own method


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_info(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)


# class Manager(Employee):            
    
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display_info(self):
#         super().display_info()
#         print("Department:", self.department)


#     

# MULTILEVEL INHERITANCE
# A class inherits from a child class in the next level.

# class Employee:
#     def show_employee(self):
#         print("I am an employee")


# class Developer(Employee):
#     def write_code(self):
#         print("I write Python code")


# class SeniorDeveloper(Developer):
#     def review_code(self):
#         print("I review other developers' code")


# # Create the last-level child object
# s1 = SeniorDeveloper()

# s1.show_employee()  # From Employee
# s1.write_code()     # From Developer
# s1.review_code()    # From SeniorDeveloper



# class parent:
#     def show_parent(self):
#         print("I am a parent")

# class child  (parent):
#     def show_child(self):
#         print("I am a child")

# class grandchild(child):
#     def show_grandchild(self):
#         print("I am a grandchild")


# g1 = grandchild()
# g1.show_parent()    # From parent
# g1.show_child()     # From child
# g1.show_grandchild() # From grandchild

# #multilevel inheritance example
# class car:
#     def company(self):
#         print("I am a car mahindra")

# class model(car):
#     def model_name(self):
#         print("I am a car thar")

# class variant(model):
#     def variant_name(self):
#         print("I am a car top model")
        

# v1 = variant()
# v1.company()    # From car
# v1.model_name() # From model
# v1.variant_name() # From variant



#basic of hybrid inheritance


# class atul:
#     def show_atul(self):
#         print("I am atul")  

# class shashaank:
#     def show_shashaank(self):
#         print("I am shashaank") 


# class sachin:
#     def show_sachin(self):
#         print("I am sachin")    

# class jashan:
#     def show_jashan(self):
#         print("I am jashan")

# class all(atul, shashaank, sachin, jashan):
#     def show_all(self):
#         print("all are boys")

# all1 = all()
# all1.show_atul()      # From atul     
# all1.show_shashaank()  # From shashaank
# all1.show_sachin()    # From sachin 
# all1.show_jashan()     # From jashan              



#hybrid multiple inheritance example

# # Parent Class
# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_person_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# # Child Class 1
# class Student(Person):

#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)

#         self.roll_no = roll_no
#         self.course = course

#     def show_student_details(self):
#         print("Roll Number:", self.roll_no)
#         print("Course:", self.course)


# # Child Class 2
# class Employee(Person):

#     def __init__(self, name, age, employee_id, salary):
#         super().__init__(name, age)

#         self.employee_id = employee_id
#         self.salary = salary

#     def show_employee_details(self):
#         print("Employee ID:", self.employee_id)
#         print("Salary:", self.salary)


# # Multiple Inheritance
# class TeachingAssistant(Student, Employee):

#     def __init__(self, name, age, roll_no, course, employee_id, salary):
#          # Directly initialize Person
#         Person.__init__(self, name, age)

#         # Initialize Student-specific attributes
#         self.roll_no = roll_no
#         self.course = course

#         # Initialize Employee-specific attributes
#         self.employee_id = employee_id
#         self.salary = salary

#     def show_all_details(self):
#         print("\n===== TEACHING ASSISTANT DETAILS =====")

#         self.show_person_details()
#         self.show_student_details()
#         self.show_employee_details()


# # Creating Object
# ta = TeachingAssistant(
#     "Rahul",
#     24,
#     101,
#     "Python Programming",
#     "EMP501",
#     25000
# )

# # Displaying Details
# ta.show_all_details()


# parent class:
#class Person:/



# class Animal:

#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):

#     # Override the parent's sound method.
#     def sound(self):
#         super().sound()  
#         print("Dog barks")


# class Cat(Animal):

#     # Override the parent's sound method.
#     def sound(self):
#         print("Cat meows")


# # a1 = Animal()
# d1 = Dog()
# c1 = Cat()

# # a1.sound()
# d1.sound()
# c1.sound()


#method overriding example



        

























































































