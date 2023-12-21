class SuperHero:#саздаем сласс СуперГерой
    people = 'people'#Свойства класса

    def __init__(self, name, nikname, superPower, health_points, catchphrase):
        self.name = name #'SpiderMan'
        self.nikname = nikname #'Spider'
        self.superPower = superPower #'Shoot webs','climb the wall'
        self.health_points = health_points #100
        self.catchphrase = catchphrase #'Увы, я могу десять раз спасти мир, но когда я в беде никто не протянет руку.'

    """Вывод имя Героя"""
    def name1(self):
        return self.name

    """Умножение здоровья на 2"""
    def point(self):
        return self.health_points * 2

    """Вывод прозвище, способность и здаровье героя"""
    def __str__(self):
        return f'{self.nikname}, {self.superPower}, {self.health_points}'

    """Длина каронной фразы"""
    def __len__(self):
        return len(self.catchphrase)

    def apply_super_power(self):
        self.health_points **= 2
        self.fly = True

    def show_true_phrase(self):
        return "True in the True_phrase"

spiderman = SuperHero('SpiderMan', 'Spider', 'Shoot webs', 100, 'Увы, я могу десять раз спасти мир, но когда я в беде никто не протянет руку.')

print(spiderman.name1())  # Вывод: SpiderMan
print(spiderman.point())  # Вывод: 200
print(str(spiderman))  # Вывод: Spider Shoot webs 100
print(len(spiderman))  # Вывод: Длина строки
print("")
class AirHero(SuperHero):
    def __init__(self, name, nikname, superPowers, health_points, catchphrase, altitude, damage):
        super().__init__(name, nikname, superPowers, health_points, catchphrase)
        self.altitude = altitude
        self.damage = damage
        self.fly = False  # Новое свойство

    def apply_super_power(self):
        super().apply_super_power()

class EarthHero(SuperHero):
    def __init__(self, name, nikname, superPowers, health_points, catchphrase, strength, damage):
        super().__init__(name, nikname, superPowers, health_points, catchphrase)
        self.strength = strength
        self.damage = damage
        self.fly = False  # Новое свойство

    def apply_super_power(self):
        super().apply_super_power()

class CosmicHero(SuperHero):
    def __init__(self, name, nikname, superPowers, health_points, catchphrase, cosmic_power, damage):
        super().__init__(name, nikname, superPowers, health_points, catchphrase)
        self.cosmic_power = cosmic_power
        self.damage = damage
        self.fly = False  # Новое свойство

    def apply_super_power(self):
        super().apply_super_power()

class Villain(CosmicHero):  # Наследуем от CosmicHero
    people = 'monster'

    def gen_x(self):
        pass  # Пока ничего не делаем

    def crit(self):
        # Возвести урон в квадрат (просто для примера)
        self.damage **= 2

# Создание объектов
air_hero = AirHero('AirMan', 'Air', ['Fly', 'Super Speed'], 80, 'Бесканечность не предел!', 3000, 20)
earth_hero = EarthHero('EarthMan', 'Earth', ['Super Strength', 'Earth Manipulation'], 90, 'Герой — это самая короткая профессия на свете.!', 100, 15)
cosmic_hero = CosmicHero('CosmicMan', 'Cosmic', ['Teleportation', 'Energy Manipulation'], 120, 'Вы можете утратить веру в нас, но только не в самих себя.!', 'Star Blast', 25)
villain = Villain('EvilEntity', 'Evil', ['Dark Powers'], 150, 'Лучше прожить один день жизнью льва, чем сто лет жизнью овцы.', 'Dark Energy', 30)

# Применение методов
air_hero.apply_super_power()
print(air_hero.fly)  # Вывод: True
print(air_hero.show_true_phrase())  # Вывод: True in the True_phrase
print(air_hero.point())
print(air_hero.catchphrase)
print(air_hero.nikname)
print("")

earth_hero.apply_super_power()
print(earth_hero.fly)  # Вывод: True
print(earth_hero.show_true_phrase())  # Вывод: True in the True_phrase
print(earth_hero.catchphrase)
print(earth_hero.point())
print(earth_hero.nikname)
print("")

cosmic_hero.apply_super_power()
print(cosmic_hero.fly)  # Вывод: True
print(cosmic_hero.show_true_phrase())  # Вывод: True in the True_phrase
print(cosmic_hero.catchphrase)
print(cosmic_hero.point())
print(cosmic_hero.nikname)
print("")

villain.apply_super_power()
print(villain.fly)  # Вывод: True
print(villain.people)  # Вывод: monster
print(villain.catchphrase)
print(villain.point())
villain.crit()
print(villain.damage)  # Вывод: 900 (30^2)