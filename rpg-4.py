"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Warrior:
    def __init__(self, name,health, power):
        self.name = name
        self.health = health
        self.power = power

    def status(self):
        return "%s has %d health and %d power" % (self.name, self.health, self.power)

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.power
        print("%s did %d damage to %s" % (self.name, self.power, enemy.name))

class Hero(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

class Goblin(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

hiro = Hero("Hiro", 10, 5)
spike = Goblin("Spike", 6, 2)

def main():
 while spike.health > 0 and hiro.health > 0:
        print(hiro.status())
        print(spike.status())
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hiro.attack(spike) 
            if spike.is_alive() == False:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if spike.health > 0:
            # Goblin attacks hero
            spike.attack(hiro)
            if hiro.is_alive == False:
                print("You are dead.")

main()
