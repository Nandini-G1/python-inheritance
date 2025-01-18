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


c1 = Christmas_Card("Chaitu")
c1.mssg()
b1 = Birthday_Card("Siva")
b1.mssg()

