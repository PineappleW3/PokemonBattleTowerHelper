class Pokemon:
    def __init__(self, name2):
        self.name = name2
        self.type1 = "Blank"
        self.type2 = "Blank"
        self.item = "Blank"
        self.ability = "Blank"
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.spatk = 0
        self.spdef = 0
        self.speed = 0
        self.moves = ["Blank","Blank","Blank","Blank"]
        self.status = "None"
        self.currenthp = "Max"
    
    def setname(self, name2):
        self.name = name2
    def getname(self):
            return self.name
    
    def settype1(self, type):
        self.type1 = type
    def gettype1(self):
        return self.type1
    
    def settype2(self, type):
        self.type2 = type
    def gettype2(self):
        return self.type2
    
    def setitem(self, item2):
         self.item = item2
    def getitem(self):
         return self.item
    
    def setability(self, ability2):
         self.ability = ability2
    def getability(self):
         return self.ability
    
    def sethp(self, stat):
         self.hp = str(stat)
    def gethp(self):
         return self.hp
    
    def setattack(self, stat):
         self.attack = str(stat)
    def getattack(self):
         return self.attack
    
    def setdefense(self, stat):
         self.defense = str(stat)
    def getdefense(self):
         return self.defense
    
    def setspatk(self, stat):
         self.spatk = str(stat)
    def getspatk(self):
         return self.spatk
    
    def setspdef(self, stat):
         self.spdef = str(stat)
    def getspdef(self):
         return self.spdef
    
    def setspeed(self, stat):
         self.speed = str(stat)
    def getspeed(self):
         return self.speed
    
    def setmoves(self, moves2):
         self.moves = moves2
    def getmoves(self):
         return self.moves
    
    def setstatus(self, status2):
         self.status = status2
    def getstatus(self):
         return self.status
    
    def setcurrenthp(self, hp):
         self.currenthp = hp
    def getcurrenthp(self):
         return self.currenthp