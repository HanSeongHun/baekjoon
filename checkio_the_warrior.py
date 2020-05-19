class Warrior:
    health = 50
    attack = 5
    is_alive = True


class Knight():
    health = 50
    attack = 7
    is_alive = True


def fight(unit_1, unit_2):
    while True :
        unit_2.health -= unit_1.attack
        print(unit_2.health)
        if(unit_2.health <= 0):
            unit_2.is_alive = False
            break
        unit_1.health -= unit_2.attack
        if(unit_1.health <= 0):
            unit_1.is_alive = False
            break
    if(unit_1.is_alive==True):
        return True
    else:
        return  False

chuck = Warrior()
bruce = Warrior()

print(fight(chuck,bruce))
