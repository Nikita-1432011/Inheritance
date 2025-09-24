class Person :

    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

    
class empolyee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post

        Person.__init__(self,name,idnumber)
a = empolyee('nita',23456,200000,"Intern")
a.display()
        
        