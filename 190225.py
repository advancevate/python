class Personage:
    def __init__(self, name, hero_class, lvl, hp, weapon, dmg):
        self.name = name
        self.hero_class = hero_class
        self.lvl = lvl
        self.hp = hp
        self.weapon = weapon
        self.dmg = dmg

    def info_pers(self):
        print(f'name: {self.name} | class: {self.hero_class} | level: {self.lvl}\n'
              f'health: {self.hp}\n'
              f'weapon: {self.weapon} damage: {self.dmg}')

class Warrior(Personage):
    def __init__(self, name, hero_class, lvl, hp, weapon, dmg, armor):
        super().__init__(name, hero_class, lvl, hp, weapon, dmg)
        self.armor = armor

    def __calculate_hp(self):
        return self.hp + (self.armor * 0.5)  # test

    def info_pers(self):
        effective_hp = self.__calculate_hp()
        super().info_pers()
        print(f'armor: {self.armor}')
        print(f"effective hp: {effective_hp}")

    def warrior_attack(self):
        if self.hp > 50 and self.armor != 0:
            print(f"{self.name} attacks\n")
        else:
            print(f"{self.name}: low hp\n")

class Mage(Personage):
    def __init__(self, name, hero_class, lvl, hp, weapon, dmg, mana):
        super().__init__(name, hero_class, lvl, hp, weapon, dmg)
        self.mana = mana

    def cast_spell(self):
        if self.mana > 20:
            print(f"{self.name} casts a powerful spell!\n")
            self.mana -= 20
        else:
            print(f"{self.name}: not enough mana\n")

    def info_pers(self):
        super().info_pers()
        print(f'mana: {self.mana}')

class Archer(Personage):
    def __init__(self, name, hero_class, lvl, hp, weapon, dmg, accuracy):
        super().__init__(name, hero_class, lvl, hp, weapon, dmg)
        self.accuracy = accuracy

    def shoot_arrow(self):
        if self.accuracy > 70:
            print(f"{self.name} shoots a precise arrow!\n")
        else:
            print(f"{self.name} misses the target\n")

    def info_pers(self):
        super().info_pers()
        print(f'accuracy: {self.accuracy}')

class Healer(Personage):
    def __init__(self, name, hero_class, lvl, hp, weapon, dmg, healing_power):
        super().__init__(name, hero_class, lvl, hp, weapon, dmg)
        self.healing_power = healing_power

    def heal(self):
        if self.healing_power > 30:
            print(f"{self.name} heals the party!\n")
            self.hp += self.healing_power
        else:
            print(f"{self.name}: not enough healing power\n")

    def info_pers(self):
        super().info_pers()
        print(f'healing power: {self.healing_power}')

class Rogue(Personage):
    def __init__(self, name, hero_class, lvl, hp, weapon, dmg, stealth):
        super().__init__(name, hero_class, lvl, hp, weapon, dmg)
        self.stealth = stealth

    def sneak_attack(self):
        if self.stealth > 50:
            print(f"{self.name} performs a sneak attack!\n")
        else:
            print(f"{self.name} is too clumsy to sneak\n")

    def info_pers(self):
        super().info_pers()
        print(f'stealth: {self.stealth}')

class OnHike:
    def __init__(self):
        self.list_hero = []

    def add_hero(self, hero):
        self.list_hero.append(hero)

    def print_heroes_hike(self):
        print("heroes on hike:")
        for x in self.list_hero:
            print(f" - {x.name}")

#создание объектов персонажей
warrior = Warrior('Oleg', 'warrior', 19, 130.5, 'two-handed sword', 35, 50)
mage = Mage('Elena', 'mage', 15, 90, 'staff', 25, 100)
archer = Archer('Ivan', 'archer', 18, 110, 'bow', 30, 80)
healer = Healer('Anna', 'healer', 14, 100, 'wand', 15, 40)
rogue = Rogue('Dmitry', 'rogue', 20, 120, 'dagger', 40, 60)

#создание объекта похода и добавление героев
hike = OnHike()
hike.add_hero(warrior)
hike.add_hero(mage)
hike.add_hero(archer)
hike.add_hero(healer)
hike.add_hero(rogue)

#вывод информации о персонажах
warrior.info_pers()
warrior.warrior_attack()

mage.info_pers()
mage.cast_spell()

archer.info_pers()
archer.shoot_arrow()

healer.info_pers()
healer.heal()

rogue.info_pers()
rogue.sneak_attack()

#вывод списка героев в походе
hike.print_heroes_hike() 
