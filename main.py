import random


class Head:
    eyes = 2
    ears = 2
    mouth = 1
    teeth = 32
    def brush_teeth(self):
        print('Зубы почистил' if random.randint(0, 1) else 'Зубы не почистил, зажевал жвачку')

    def eat(self):
        taste = 'Вкусно' if random.randint(0, 1) else 'не вкусно'
        print(taste)


class Body:
    heart = 1
    def sweat(self):
        sweat_ml = random.randint(10, 1000)
        print(f'выделилось {sweat_ml} мл пота')

class Limbs:
    arms = 2
    feet = 2
    def dance(self):
        dancing = 'Бог танца, Мигель отдыхает!' if random.randint(0, 1) else 'Ножками потопали, ручками похлопали!'
        print(dancing)

class Human(Head, Body, Limbs):
    def drive(self):
        driving = "Прекрасное вождение- уровень 'Шумахер'" if random.randint(0, 1) else 'Опять лишили прав'
        print(driving)
    def walk(self):
        walking = random.randint(1, 12)
        print(f'Прошел {walking} км')


nick = Human()
nick.brush_teeth()
nick.eat()
nick.dance()
nick.drive()
nick.walk()