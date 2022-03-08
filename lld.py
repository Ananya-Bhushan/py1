#Class parkingfloor is created 
import random 
class parkingFloor():
    #class is instantiated 
    def __init__(self,name):
        self.name = name
        self.spotTotal = {'compact':0,'large':0,'bike':0,'electric':0}

        self.spotTaken = {'compact':0,'large':0,'bike':0,'electric':0}

        self.freeSpot = {'compact':set(),'large':set(),'bike':set(),'electric':set()}
        self.takenSpot = {'compact':{},'large':{},'bike':{},'electric':{}}
# Class parkingfloor has a assignSpot method to assign a vechile a spot
    def assignSpot(self,ticket):
        if self.spotTaken[ticket.veh.type] >= self.spotTotal[ticket.veh.type]:
            return False
        for s in self.freeSpot[ticket.veh.type]:
            if s.id not in self.takenSpot[ticket.veh.type]:
                self.takenSpot[ticket.veh.type][s.id] = ticket
            self.spotTaken[ticket.veh.type]+=1
            self.freeSpot[ticket.veh.type].remove(s)
            ticket.allocateSpot(s)
            return True
        return False
#addSpot method to add a type of vehicle to a spot 
    def addSpot(self,type,v):
        for i in range(v):
            s = spot(type)
            self.freeSpot[type].add(s)
        self.spotTotal[type] += v
#enterPanel class 
class entryPanel():
    def __init__(self,id):
        self.id = id
#printTicket method to print vehicle id,sopt id,ticket id,time
    def printTicket(self,ticket):
        print('Vehicle ID ',ticket.veh.id)
        print('Spot ID ',ticket.spot.id)
        print('Ticket ID ',ticket.id)
        print('Time',ticket.Time)

    def display(self,message):
        print(message)


class vehicle():
    def __init__(self,id,vehType):
        self.id = id
        self.type = vehType

#generates random spot number
class spot():
    def __init__(self,spotType):
        def generateId():
            # some mechanism to generate spot id
            spot=random.randint(1,500)
            return spot
        self.id = generateId()
        self.type = spotType

class ticket():
    def __init__(self,v1):
        self.id = self.generateId()
        self.veh = v1

        self.spot = None
        self.Time = self.getTime()
        self.amount = 0
        self.status = 'Active'
        self.payment = None

    def getTime(self):
        time = '12:34'
        return time

    def generateId(self):
        # some mechanism to generate new ticket id
        new_ticket  = random.randint(1,1000)
        return new_ticket

    def allocateSpot(self,spot):
        self.spot = spot

    def addPayment(self,pay):
        self.status = 'Complete'
        self.payment = pay

class parkingLot():
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.level = []
#to add floors in parking lot
    def addLevel(self,floor):
        self.level.append(floor)

    def processEntry(self,t1,gate):
        for l in self.level:
            if l.assignSpot(t1):
                gate.printTicket(t1)
                return
        gate.display('No Spot Empty')
        

    def processExit(self,ticket,gate):
        def getTime():
            # Gives the current time
            return 3
        currTime = getTime()
        print('Processing fare',ticket.veh.type,ticket.spot.id)
        amountCalculated=random.randint(10,30) 
        ticket.addPayment(Payment(amountCalculated))
        gate.display('Payment Successful')
        gate.display(amountCalculated)
    

class Payment():
    def __init__(self,amount):
        self.id = 'paymentid'
        self.type = 'credit' # debit
        self.time = 'paymet time'

class displayBoard():
    def show(self,p):
        for l in p.level:
            print(l.name)
            for k in l.spotTotal.keys():
                print(k, l.spotTotal[k] - l.spotTaken[k])


P = parkingLot('Savita','Address')
floor1 = parkingFloor('floor1')
floor2 = parkingFloor('floor2')
P.addLevel(floor1)
P.addLevel(floor2)
floor1.addSpot('bike',1)
floor2.addSpot('large',1)

board = displayBoard()
board.show(P)

entryPanel1 = entryPanel('1')
entryPanel2 = entryPanel('2')

v1 = vehicle(9,'bike')
t1 = ticket(v1)
v2 = vehicle(10,'large')
t2 = ticket(v2)
   

P.processEntry(t1,entryPanel1)
P.processExit(t1,entryPanel1)
P.processEntry(t2,entryPanel2)
P.processExit(t2,entryPanel2)