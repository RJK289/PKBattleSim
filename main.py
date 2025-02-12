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
  
    #The attacker chooses a move
    chosen_move = attacker.choose_move()

    #Check if the move hits
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
        #Determine who goes first based on Speed
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