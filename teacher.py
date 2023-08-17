from Person import Person
class teacher(Person):
    def __init__(self, tname, tage, year,salary):
        super().__init__(tname, tage,salary)
        self.exp_year=year
        
    def say_hi(self):
        return f"hello {self.name} as teacher"

    def bounce(self):
        b=super().bounce() * 2
        return b