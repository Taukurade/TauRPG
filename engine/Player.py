
inv_dict={
    "weapon":None,
    "tool":None,
    "shield":None,
    "items":[]
}

class Player:
    def __init__(self,nick,x = 0, y = 0, health = 100, dead = False, inventory = inv_dict):
        self.x = x
        self.y = y
        self.health = health
        self.nick = nick
        self.dead = dead
        self.inventory = inventory


    def receive_damage(self,amount):
        if self.inventory["shield"] is None:
            if self.health < amount:
                self.dead = True
                self.death()
            else:
                self.health -= amount
        else:
            
    
    def get_save_data(self):
        return {
                "nick":self.nick,
                "health":self.health,
                "dead":self.dead,
                "inventory":self.inventory,
                "x":self.x,
                "y":self.y
            }

    def death(self):
        return "{player.death}"

    def move(self):
        pass