from uuid import uuid1


__all__ = ['Forest','Wasteland','Desert']
class Biome:
    pass


class Forest(Biome):
    def __init__(self):
        self.uname = 'forest_biome'
        self.uuid = uuid1()
        
        

class Wasteland(Biome):
    def __init__(self):
        self.uname = 'wasteland_biome'
        self.uuid = uuid1()
        
class Desert(Biome):
    def __init__(self):
        self.uname = 'desert_biome'
        self.uuid = uuid1()
        