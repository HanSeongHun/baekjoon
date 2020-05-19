class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    def is_alive(self) -> bool:
        if self.health <= 0:
            return False
        else:
            return True

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

def fight(unit_1, unit_2) -> bool:
    while True:
        unit_2.health -= unit_1.attack
        if(unit_2.is_alive() == False):
            return True
        unit_1.health -= unit_2.attack
        if(unit_1.is_alive() == False):
            return False


class Army():
    def __init__(self):
        self.soldiers =[]
    def add_units(self,member,i):
        for _ in range(i):
            self.soldiers.append(member())
    def is_alive(self):
        return self.soldiers !=[]
    def fighter(self):
        return self.soldiers[0]
    def pop(self):
        self.soldiers.pop(0)


class Battle():
    def fight(self,army_1,army_2):
        while(army_1.is_alive and army_2.is_alive):
            if fight(army_1.fighter,army_2.fighter):
                army_2.pop
            else:
                army_1.pop




chuck = Warrior()
bruce = Knight()
print(fight(bruce,chuck))
