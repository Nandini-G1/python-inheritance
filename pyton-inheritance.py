class Card:
    def __init__ (self, receiverName):
        self.receiverName = receiverName

    def mssg (self):
        print("Hello "+ self.receiverName)

class Birthday_Card(Card):
    def __init__ (self, receiverName):
        super().__init__(receiverName)

    def mssg (self):
        print("Happy Birthday "+self.receiverName+"!!!")

class Christmas_Card(Card):
    def __init__ (self, receiverName):
        super().__init__(receiverName)

    def mssg (self):
        print("Merry Christmas "+self.receiverName+"!!!")
        
class Valentine_Card(Card):
    def __init__(self,receiverName):
        super().__init__(receiverName)

    def mssg(self):
        vmssg = f"Happy Valentine's {self.receiverName}!!!"
        print(vmssg)

class Custom_Card(Card):
    def __init__(self,receiverName):
        super().__init__(receiverName)
        self.cmssg = input("Please enter the custom message: ")
        
    def mssg(self):
        custom_mssg = f"{self.cmssg} {self.receiverName}!!!"
        print(custom_mssg)


c1 = Christmas_Card("Sam")
c1.mssg()
b1 = Birthday_Card("Sam")
b1.mssg()
v1 = valentine_Card("Sam")
v1.mssg()

