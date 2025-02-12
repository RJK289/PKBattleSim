import random

class Move:
    def __init__(self, name, power, accuracy):
        self.name = name
        self.power = power
        self.accuracy = accuracy

    def calculate_damage(self, attacker, defender):
        base_damage = (attacker.attack / defender.defense) * self.power
        return int(base_damage)
    
class Monster:
    def __init__(self, name, hp, attack, defense, speed, moves):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves

    def is_fainted(self):
        return self.hp <= 0

    def take_damage(self, damage):
        self.hp = max(self.hp - damage, 0)

    def choose_move(self):
        return random.choice(self.moves)

def take_turn(attacker, defender):
    chosen_move = attacker.choose_move()
    hit_chance = random.random()
    if hit_chance <= chosen_move.accuracy:
        damage = chosen_move.calculate_damage(attacker, defender)
        defender.take_damage(damage)
        print(f"{attacker.name} used {chosen_move.name}!")
        print(f"It dealt {damage} damage to {defender.name}!")
    else:
        print(f"{attacker.name} tried to use {chosen_move.name}, but it missed!")
    if defender.is_fainted():
        print(f"{defender.name} has fainted!")

def battle(monster1, monster2):
    print(f"A wild battle has begun between {monster1.name} and {monster2.name}!")
    
    while not monster1.is_fainted() and not monster2.is_fainted():
        # Determine who goes first based on Speed
        if monster1.speed >= monster2.speed:
            take_turn(monster1, monster2)
            if monster2.is_fainted():
                break
            take_turn(monster2, monster1)
        else:
            take_turn(monster2, monster1)
            if monster1.is_fainted():
                break
            take_turn(monster1, monster2)

    if monster1.is_fainted() and monster2.is_fainted():
        print("It's a tie—both monsters fainted!")
    elif monster1.is_fainted():
        print(f"{monster1.name} fainted. {monster2.name} is the winner!")
    else:
        print(f"{monster2.name} fainted. {monster1.name} is the winner!")  

def main():
    # Moves
    tackle = Move(name="Tackle", power=40, accuracy=0.95)
    water_gun = Move(name="Water Gun", power=40, accuracy=1.0)

    # Monsters
    creature = Monster(
        name="Creature1",
        hp=45,
        attack=49,
        defense=49,
        speed=45,
        moves=[tackle]
    )

    creature2 = Monster(
        name="Creature2",
        hp=44,
        attack=48,
        defense=65,
        speed=43,
        moves=[tackle, water_gun]
    )

    battle(creature, creature2)

if __name__ == "__main__":
    main()
