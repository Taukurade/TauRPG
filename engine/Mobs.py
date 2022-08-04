import random
from uuid import uuid1

__all__ = ["Pig","Scorpion","Spider"]
class Mob:
    
    def attack_player(self,Player):
        if self.can_attack and random.random() > 0.85:
            Player.receive_damage(random.randint(self.damage,self.damage+5))
            return self.uname
        



class Pig(Mob):
    def __init__(self):
        self.uname = "pig"
        self.uuid = uuid1()
        self.weight = 0.3
        self.damage = 1
        self.can_attack = False

class Scorpion(Mob):
    def __init__(self):
        self.uname = "scorpion"
        self.uuid = uuid1()
        self.weight = 0.1
        self.damage = 20
        self.can_attack = True

class Spider(Mob):
    def __init__(self):
        self.uname = "spider"
        self.uuid = uuid1()
        self.weight = 0.1
        self.damage = 20
        self.can_attack = True

