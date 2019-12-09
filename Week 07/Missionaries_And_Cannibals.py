class Bank:
    def __init__(self,name, m, c, hasBoat, empty):
        #M for the number of Missionaries, c for the number of Cannibals,
        #hasBoat for if the boat is there, name for the name to display when viewing
        #empty tells us is the bank can be made empty(does not prevent from starting empty)
        self.DisplayName = name
        self.Missionaries = m
        self.Cannibals = c
        self.Boat = hasBoat
        self.CanBeEmptied = empty
    
    def CanRecieveCannibals(self, num):
        return (self.Missionaries == 0) or (self.Missionaries >= (self.Cannibals + num))
    
    def CanSendCannibals(self, num):
        notEmpty = True
        if not self.CanBeEmptied:
            notEmpty = self.Missionaries + (self.Cannibals - num) > 0
        return self.Cannibals - num >= 0 and notEmpty
    
    def CanRecieveMissionaries(self, num):
        return self.Missionaries + num >= self.Cannibals
    
    def CanSendMissionaries(self, num):
        notEmpty = True
        if not self.CanBeEmptied:
            notEmpty = (self.Missionaries - num) + self.Cannibals > 0
        return self.Missionaries - num >= 0 and (self.Missionaries - num >= self.Cannibals or self.Missionaries - num == 0) and notEmpty
    
    def CanSendPair(self):
        notEmpty = True
        if not self.CanBeEmptied:
            notEmpty = (self.Missionaries -1) + (self.Cannibals - 1) > 0
        return self.Missionaries -1 >= self.Cannibals - 1 and notEmpty
    
    def CanRecievePair(self):
        return self.Missionaries + 1 >= self.Cannibals + 1 
    
    def HasBoat(self):
        return self.Boat
    
    def DockBoat(self, mission, cann):
        self.Boat = True
        self.Missionaries = self.Missionaries + mission
        self.Cannibals = self.Cannibals + cann
    
    def SendBoat(self, mission, cann, bank):
        if mission > 0 or cann > 0:
            self.Missionaries = self.Missionaries - mission
            self.Cannibals = self.Cannibals - cann
            bank.DockBoat(mission, cann)
            self.Boat = False
    
    def Output(self):
        outputString = "{0}:{1} Missionaries, {2} Cannibals".format(self.DisplayName, self.Missionaries, self.Cannibals)
        if self.HasBoat():
            outputString = outputString + ", Boat Docked"
        return outputString
#fromBank is the bank we start on this pass, to is where we're going this pass, dest is where we want to end up, start is where we first started
def findPassengers(toBank, fromBank, destBank, startBank):
    sendM = 0
    sendC = 0
    if startBank.Missionaries + startBank.Cannibals == 1:
        sendC = 1
    elif toBank.CanRecieveCannibals(2) and fromBank.CanSendCannibals(2) and destBank.Cannibals != 3:
            sendC = 2
    elif toBank.CanRecieveMissionaries(2) and fromBank.CanSendMissionaries(2) and startBank != toBank:
        sendM = 2
    elif toBank.CanRecieveCannibals(1) and fromBank.CanSendCannibals(1):
        sendC = 1
        if toBank.CanRecieveMissionaries(1) and fromBank.CanSendMissionaries(1):
            sendM = 1
    elif toBank.CanRecieveMissionaries(1) and fromBank.CanSendMissionaries(1):
        sendM = 1
    elif toBank.CanRecievePair() and fromBank.CanSendPair():
        sendM = 1
        sendC = 1
    if sendM > 0 or sendC > 0:
        fromBank.SendBoat(sendM, sendC, toBank)

def main():
    leftBank = Bank("Left Bank",3,3,True, True)
    rightBank = Bank("Right Bank",0,0,False, False)
    while(not (rightBank.Missionaries == 3 and rightBank.Cannibals == 3)):
        print(leftBank.Output())
        print(rightBank.Output())
        if leftBank.HasBoat():
            findPassengers(rightBank, leftBank, rightBank, leftBank)
        else:
            findPassengers(leftBank, rightBank, rightBank, leftBank)
    print(leftBank.Output())
    print(rightBank.Output())

main()