from .Biomes import *
from .Mobs import *
from .World import *
from .Translation import *

class Main:
    def __init__(self,Player,Registry,World,Cell):
        self.ply = Player
        self.reg = Registry
        self.world = World
        self.cell = Cell

    def startGame(self):
        while True:
            pass









class Registry:
    def __init__(self):
        self.mobs = dict()
        self.biomes = dict()

        self.mob_list = list()
        self.biome_list = list()
    
    def commitRegistry(self):
        self.mob_list = list(self.mobs.items())
        self.biome_list = list(self.biomes.items())
    
    def regNewMob(self,mob):
        self.mobs[mob.uname] = mob
    
    def regNewBiome(self,biome):
        self.biomes[biome.uname] = biome