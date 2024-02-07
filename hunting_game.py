import random

class Gun:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Animal:
    def __init__(self, name, points):
        self.name = name
        self.points = points

class Game:
    def __init__(self):
        self.guns = [Gun("Pistol", 10), Gun("Shotgun", 20), Gun("Rifle", 30)]
        self.animals = [Animal("Deer", 20), Animal("Rabbit", 10), Animal("Bear", 50)]
        self.points = 0

    def select_gun(self):
        print("Select your gun:")
        for i, gun in enumerate(self.guns):
            print(f"{i + 1}. {gun.name} ({gun.power} power)")
        choice = int(input("Enter your choice: ")) - 1
        return self.guns[choice]

    def shoot_animal(self, gun):
        animal = random.choice(self.animals)
        print(f"You've encountered a {animal.name}!")
        shoot = input("Do you want to shoot? (yes/no): ").lower()
        if shoot == 'yes':
            self.points += animal.points * gun.power
            print(f"You shot the {animal.name} and earned {animal.points * gun.power} points!")
        else:
            print("You didn't shoot.")

    def play(self):
        print("Welcome to the Hunting Game!")
        selected_gun = self.select_gun()
        while True:
            self.shoot_animal(selected_gun)
            play_again = input("Do you want to continue hunting? (yes/no): ").lower()
            if play_again != 'yes':
                break
        print(f"Game Over! You earned {self.points} points.")

if __name__ == "__main__":
    game = Game()
    game.play()
