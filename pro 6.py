class Bank:
    def setMoney(self, honey):
        self.m=honey

    def getMoney(self):
        return self.m
    


obj=Bank()
obj.setMoney(10000)


print("Bank has money :  ",obj.m)