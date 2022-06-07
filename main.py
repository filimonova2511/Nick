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

class Limbs:   # добавить функции
    arms = 2
    feet = 2

class Human(Head, Body, Limbs):   # можно добавить танцевать, гулять (сколько км прошел),ходить на свидание или в бар
    def drive(self):
        driving = "Прекрасное вождение- уровень 'Шумахер'" if random.randint(0, 1) else 'Опять лишили прав'
        print(driving)




nick = Human()
