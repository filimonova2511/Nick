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
        print(f'Выделилось {sweat_ml} мл пота')


class Limbs:
    arms = 2
    feet = 2
    def dance(self):
        dancing = 'Бог танца, Мигель отдыхает!' if random.randint(0, 1) else 'Ножками потопали, ручками похлопали!'
        print(dancing)


class Drive():
    def drive(self):
        driving = "Прекрасное вождение- уровень 'Шумахер'" if random.randint(0, 1) else 'Опять лишили прав'
        print(driving)


class Walk():
    def walk(self):
        walking = random.randint(1, 12)
        print(f'Прошел {walking} км')


count = list()
def Summator_Immunity(*args):
    count.append(args)
    if len(count)==4:
        sum_all = 0
        for i in count:
            for j in i:
                sum_all += j
        print('Отличный иммунитет' if sum_all==0 else 'Пониженный иммунитет')
    return count

class Immunity():
    def smok(self):
        s = random.randint(0, 1)
        smoking = 'Не курит' if s==0 else 'Курит'
        print(smoking)
        sum = Summator_Immunity(s)
        return sum

    def weight(self):
        w = random.randint(0, 1)
        overweight = 'В идеальной форме' if w==0 else 'Необходимо придеждиваться диеты'
        print(overweight)
        sum = Summator_Immunity(w)
        return sum

    def alcohol(self):
        a = random.randint(0, 1)
        drinking_alcohol = 'Нет проблем с алкоголем' if a==0 else 'Ограничьте употребление алкоголя'
        print(drinking_alcohol)
        sum = Summator_Immunity(a)
        return sum

    def chronic_diseases(self):
        ch = random.randint(0, 1)
        diseases = 'Нет хронических заболеваний' if ch==0 else 'Есть хронические заболевания'
        print(diseases)
        sum = Summator_Immunity(ch)
        return sum

class Human(Head, Body, Limbs, Drive, Walk, Immunity):
    pass


nick = Human()
nick.brush_teeth()
nick.eat()
nick.sweat()
nick.dance()
nick.drive()
nick.walk()
nick.smok()
nick.weight()
nick.alcohol()
nick.chronic_diseases()
