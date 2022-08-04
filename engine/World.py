
import random

__all__ = ['Cell','World']

class Cell:
    def __init__(self,x,y,biomes):
        self.x = x
        self.y = y
        self.pos = (x,y)
        self.mobs = list()
        self.attacks = list()
        self.biome = random.choice(biomes)
        self.spawn_mobs()

    def rejoin(self,Player):
        self.spawn_mobs()
        
        self.attacks = list()
        self.attacks = [m.attack_player(Player) for m in self.mobs]
    
    def spawn_mobs(self,mobs):
        
        if len(self.mobs) >= 20:
            return self.mobs
        
        elif len(self.mobs) >= 5 or len(self.mobs) <= 19:
            self.mobs += random.choices(mobs, weights=[m.weight for m in mobs], k=random.randint(0,2))
            
        else:
            self.mobs += random.choices(mobs, weights=[m.weight for m in mobs], k=random.randint(2,8))

    def get_save_data(self):
        return {
                "biome":self.biome.uname,
                "mobs":[m.uname for m in self.mobs],
                "pos":[self.x,self.y]
            }

class World:
    def __init__(self,size = 32):
        self.size = size
        self.cells = list()

