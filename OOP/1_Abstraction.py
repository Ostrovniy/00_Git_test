"""
Абстра́кция в объектно-ориентированном программировании — это использование только определения характеристик объекта, 
без описания их конкретных/детальных реализаций. Основная идея состоит в том, чтобы представить объект обладающим 
набором методов и при этом не предоставлять конкретную логику этих методов.

https://metanit.com/python/tutorial/7.8.php

"""

# -- Shere нельза создавать обьект, только наследоваться
# -- area должен быть обязательно определен в классе где идет наследование иначе будет ошибка

# 1. Подключения библиотек для работы с абстракцией
from abc import ABC, abstractmethod

# 2. Создание абстрактного класса
class Shere(ABC):
    # 3. Создание абстрактного метода
    @abstractmethod
    def area(self):
        pass

    def info(self):
        print('Класс Shere являеться абстрактным')

# 3. Наследуемся от Shere
class Rectangle(Shere):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 4. Обязательно нужно определить area метод, иначе будет ошибка
    def area(self):
        return self.width * self.height

# 5. Повторояем все тоже самое для нового класса
class Circle(Shere):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14



print(Rectangle(5, 10).area()) # 50
print(Circle(5).area()) # 78.5

r = Circle(5) 
print(r.info()) # Класс Shere являеться абстрактным
# None - не понял почему это печатаеться