"""
Прототип - порождающий патерн проектирования, позволяет копировать обьект не вдаваясь в подробности
реализации класса. Как я понял, если нам нужно создать еще один обьект такой же, то проще настроить 
просто метод клонирования который будет создавать копию самого себя, чем создавать обьек в ручную

что бы метод Клон, был точно определен, то создан Интерфейс

https://refactoring.guru/ru/design-patterns/prototype/python/example
Код который здесь пока что сложный для понимания

"""

from abc import ABC, abstractmethod

"""Интерфейс для клонирования"""
class Prototype(ABC):
    @abstractmethod
    def clone():
        pass


class Product(Prototype):
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def clone(self):
        """Создаем копию самого себя и возвращаем"""
        # Возможные какие то сложности, не все так просто
        return Product(self.name, self.age, self.status)
    
    def __str__(self):
        return f'{self.name} {self.age} {self.status}'

# Создания обьекта
test1 = Product('Yura', 20, 'wiwk')
# Копирования обьекта
test2 = test1.clone()

# Изменения первого обоекда
test1.name = 'Yura2'
test1.age = 21
test1.status = 'WIWK'

print(test1) # Yura2 21 WIWK
print(test2) # Yura 20 wiwk

