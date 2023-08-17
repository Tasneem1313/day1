from Person import Person
from teacher import teacher
def main():
    p1=Person('Ahmed', 25, 1500)
    t1=teacher('Ali', 25, 1500)
    print(p1.descrip())
    print(p1.bounce())
    print(t1.descrip())
    print(t1.bounce())
main()