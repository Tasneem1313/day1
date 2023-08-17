class Person:
    #constructor to creat objects
    #initialize instance varibles   
    def __init__(self, name, age=20, salary):       
        self.name=name
        self.age=age
        self.salary=salary
    def say_hi(self):
        return f"hello {self.name} as person"
   
        
        #use term of encapsualtion
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
        #setter/muotur methods
    def set_name(self,newName):
        self.name=newName
    def set_age(self,newAge):
        self.age=newAge
    def run(self):
        print(self.name, "is running")
    def descrip(self):
        return f"Person name is {self.name} is {self.age} years old"
    def laugh(self):
        print(self.name, "hahaha")            
    def bounce(self):        
        b=self.salary *0.005
        return b