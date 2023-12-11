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

spiderman = SuperHero('SpiderMan', 'Spider', 'Shoot webs', 100, 'Увы, я могу десять раз спасти мир, но когда я в беде никто не протянет руку.')

print(spiderman.name1())  # Вывод: SpiderMan
print(spiderman.point())  # Вывод: 200
print(str(spiderman))  # Вывод: Spider Shoot webs 100
print(len(spiderman))  # Вывод: Длина строки
