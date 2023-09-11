class Employee:
    def __init__(self, id, name, desig, mobile,email, salary):
        self.i=id
        self.n=name
        self.d=desig
        self.m=mobile
        self.e=email
        self.s=salary

    def setid(self,id):
        self.i=id

    def getid(self):
        return self.i
    
    def setname(self,name):
        self.n=name

    def getname(self):
        return self.n
    def setdesig(self,desig):
        self.d=desig
    def getdesig(self):
        return self.d
    def setmobile(self,mobile):
        self.m=mobile
    def getmobile(self):
        return self.m
    def setemail(self,email):
        self.e=email
    def getemail(self):
        return self.e
    def setsalary(self,salary):
        self.s= salary
    def getsalary(self):
        return self.s
    def string(self):
        return "id:",self.i,"name:",self.n,"desig:",self.d,"mobile:",self.m,"email:",self.e,"salary:",self.s
emp1=Employee(101, "Sandeep", "Developer", 9890987890, "sandeep@gmail.com","56000")
print(emp1.string())
emp1.setname("Jayesh")
print(emp1.string())