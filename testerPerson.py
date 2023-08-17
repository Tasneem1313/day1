from Person import Person
from Student import Student
from teacher import teacher
def main():
    tasneem = Person('tasneem',23)
    Person2=Person("anas",20)
    
    std1=Student("nawras", 18,2021)
    std2=Student("baylasan", 1, 2022)
    
    t1=teacher("Ms", 33,2019)
    print(Person2.descrip())
    
    print(tasneem.get_name())
    tasneem.set_name("ansam")
    
    print(tasneem.get_name())
    print(tasneem.descrip())
    tasneem.run()
    tasneem.laugh()
    Person2.laugh()
    
    print(std1.say_hi())
    print(Student.say_hi(std2))
    
    print(t1.say_hi())
    t1.laugh()
    print(Person2.say_hi())
#   return f"hi {self.name} as Teacher"

main()