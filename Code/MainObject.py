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
          self.hp = int(stat)
     def gethp(self):
          return self.hp

     def setattack(self, stat):
          self.attack = int(stat)
     def getattack(self):
          temp = self.attack
          if self.status == "Burn":
               temp = temp/2
          if self.item == "Choice Band":
               temp = temp * 1.5
          if self.item == "Life Orb":
               temp = temp * 1.3
          return round(temp)


     def setdefense(self, stat):
          self.defense = int(stat)
     def getdefense(self):
          return self.defense

     def setspatk(self, stat):
          self.spatk = int(stat)
     def getspatk(self):
          temp = self.spatk
          if self.item == "Choice Specs":
               temp = temp * 1.5
          if self.item == "Life Orb":
               temp = temp * 1.3
          return round(temp)

     def setspdef(self, stat):
          self.spdef = int(stat)
     def getspdef(self):
          return self.spdef

     def setspeed(self, stat):
          self.speed = int(stat)
     def getspeed(self):
          temp = self.speed
          if self.status == "Paralysis":
               temp = temp/2
          if self.item == "Choice Scarf":
               temp = temp * 1.5
          return round(temp)

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
          if self.currenthp == "Max":
               return self.hp
          else:
               return self.currenthp