class Organizm:
    """1) Базовый класс Организвом, есть только метод инфо"""
    def __init__(self):
        pass

    def core_info(self):
        print('Organizm')

class Animal(Organizm):
    """2) Жывотные, наслудуеться от арганизмов, запускаем иницыализацию super().__init__()"""
    def __init__(self, name, sex, age, weight, color):
        super().__init__()
        # Поля которые есть у всех жывотных
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.color = color

    # Методы которые есть у всех жывотных
    def breathe(self):
        print('Animal breathe')

    def eat(self, food=''):
        print(f'Animal eat {food}')

    def run(self, destination=''):
        print(f'Animal run {destination}')

    def sleep(self, hour=''):
        print(f'Animal run {hour}')

class Cat(Animal):
    """3) Класс кота, которые наслудует все от жывотного"""
    def __init__(self, name, sex, age, weight, color, isNasty):
        # Прокидываем парамеры в родительский класс
        super().__init__(name, sex, age, weight, color)
        # Приватное поле чисто поле кота
        self._isNasty = isNasty

    # Геттер и Сеттер для поря isNasty
    @property
    def isNasty(self):
        return self._isNasty

    @isNasty.setter
    def isNasty(self, value):
        self._isNasty = value
    
    # Метод чисто класса КОта
    def meow(self):
        print('Cat meow')

class Dog(Animal):
    """4) Класс Собака, которые наслудует все от жывотного"""
    def __init__(self, name, sex, age, weight, color, bestfriend):
        # Прокидываем парамеры в родительский класс
        super().__init__(name, sex, age, weight, color)
        # Приватное поле чисто поле собаки
        self._bestfriend = bestfriend

    # Геттер и Сеттер для поря isNasty
    @property
    def bestfriend(self):
        return self._bestfriend
    
    @bestfriend.setter
    def bestfriend(self, value):
        self._bestfriend = value

    # Метод число класса собаки
    def bark(self):
        print('Dog bark')


# Создание екземпларов класса
cat = Cat('murka', 'g', 18, 2, 'red', False)
dog = Dog('muxtar', 'm', 12, 45, 'black', 'Anton')

# Вызов методов которые унаследовали
cat.eat('55')
dog.eat('55')

# Методы которые есть только у текущих классов
cat.meow()
dog.bark()

# Проверка работы Сеттера и геттре
cat.isNasty = True
print(cat.isNasty)

# Проверка работы Сеттера и геттре
dog.bestfriend = 'Lilia'
print(dog.bestfriend)

# Метод которы есть только в самого вышшего класса, Двойная прокидка
cat.core_info()