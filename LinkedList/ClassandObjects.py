class person:
    name = "Humayoon"
    rrn = 43
    networth = 10
    def info(self): #Self is reference to current instance of class used to access variables which belongs to that class
        print(f"My Name Is {self.name} and my RRN is {self.rrn} and Networth is {self.networth}")
obj = person()
print(obj.name) #If i want to separately access any variable in class. just use the object of that class
obj.info()

#class is the template/ blueprint which contains all the properties and the methods of the object in it. Lets
# take an example of railway registration form which contains the name to be filled, which train to board, from which
# station etc all these are the methods which the object is going to have in the class
    
# Object is the instance/entity of that class which has its own methods/properties 
# If we have same example of railway form the object will have different name, different train to board, etc thus it
# will be filling the same railway form but its methods will be different from others

#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________



#Constructor is a special method in c class used to create and initialize an object of a class.
#Constructor  gets automatically called without creating any method of that class

#Constructor is of two types default construtor and parameterised constructor. 

#Default Constructor
class person:
    def __init__(self):
        name = "Humayoon"
        rrn = "43"
        print(f"My name is {name} and RRN is {rrn}")
obj = person()


#Parameterised Constructor

class person:
    def __init__(self,name,rrn):
        # name = "Humayoon"
        # rrn = "43"
        print("Hello i'm a developer")
        print(f"My name is {name} and RRN is {rrn}")
obj = person("Humayoon",'43')

#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________

#Inheritance which allows to inhert the properties of another class

#Single Inheritance 1 base class 1 derived class
class father:
    def fun1(self): #We use self as python automatically passes an argument over,so that is why we keep self
        print("hello i'm the father here")
class child(father):
    def fun2(self):
        print("Hello i'm his child")
obj = child()
obj.fun1()
obj.fun2()

#Multiple Inheritance --> more than 1 base class and 1 derived class

class mother:
    def fun1(self):
        print("Hello im the mother")
class father:
    def fun2(self):
        print("Hello im the father")
class child(mother,father):
    def fun3(self):
        print("Hello im the child")
obj1 = child()
obj1.fun1()
obj1.fun2()
obj1.fun3()

#Multilevel Inheritance --> 1 base and then its derived and then derived's derived .. so on
class mother:
    def fun1(self):
        print("Hello im the mother")
class father(mother):
    def fun2(self):
        print("Hello im the father")
class child(father):
    def fun3(self):
        print("Hello im the child")
obj1 = child()
obj1.fun1()
obj1.fun2()
obj1.fun3()

#Hierarchal Inheritance --> 1 base class and more than 1 derived class
class mother:
    def fun1(self):
        print("Hello im the mother")
class child1(mother):
    def fun2(self):
        print("Hello im the father")
class child2(child1):
    def fun3(self):
        print("Hello im the child")
obj1 = child1()
obj2 = child2()
obj1.fun1()
obj1.fun2()
obj2.fun1()
obj2.fun2()
obj2.fun3()

#Hybrid Inheritance  --> containing all 4 types of inheritance
class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()

