class Employee:
    def __init__(self, id, name, desig, mobile,email, salary):
        

    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id
    
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name
    
    def setDesig(self,desig):
        self.desig=desig

    def getDesig(self):
        return self.desig
    
    def setMobile(self,mobile):
        self.mobile=mobile

    def getMobile(self):
        return self.mobile
    
    def setSalary(self,salary):
        self.salary=salary

    def getSalary(self):
        return self.salary

    def setEmail(self,email):
        self.email=email

    def getEmail(self):
        return self.email
    
    def toString(self):
        return "Id : ",self.id,"  Name :",self.name
    
emp1=Employee(101, "Sandeep", "Developer", "9890987890", "sandeep@gmail.com","56000")

print(emp1.toString())

emp1.setName("Jayesh")
print(emp1.toString())