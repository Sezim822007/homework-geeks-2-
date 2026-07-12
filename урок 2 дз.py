import random


# Родительский класс
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет! Я {self.name}, мой уровень {self.level}.")

    def attack(self):
        print(f"{self.name} атакует!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает. Здоровье теперь: {self.health}")


# Дочерний класс Warrior
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин атакует мечом!")


# Дочерний класс Mage
class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание!")


# Дочерний класс Assassin
class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")


# Создаем объекты
warrior = Warrior("Warrior", 10, 100, 20, 50)
mage = Mage("Mage", 10, 80, 25, 100)
assassin = Assassin("Assassin", 10, 90, 30, 80)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

print("Выберите героя:")
print("Warrior / Mage / Assassin")

choice = input("Ваш выбор: ").lower()

if choice not in heroes:
    print("Неверный выбор!")
else:
    player = heroes[choice]

    # Выбираем случайного противника
    opponents = [hero for key, hero in heroes.items() if key != choice]
    enemy = random.choice(opponents)

    print(f"\nВы выбрали: {player.name}")
    print(f"Противник: {enemy.name}\n")

    player.attack()
    enemy.attack()

    # Правила игры
    wins = {
        "Warrior": "Assassin",
        "Assassin": "Mage",
        "Mage": "Warrior"
    }

    if wins[player.name] == enemy.name:
        print(f"\n{player.name} победил!")
    else:
        print(f"\n{enemy.name} победил!")