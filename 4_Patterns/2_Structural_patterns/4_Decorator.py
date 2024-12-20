"""
Декоратор - предположым что есть класс, и мы не хотим менять его, но нам нужно изменить данные которые в него поступают
или данные которые класс возвращает, что бы решыть эту проблему используеться декоратор, по простому это обертка, мы создаем класс 
декоратора который принимает основной класс через ссылку, и вызывает методы основного класса только можно уже контролировать
что будет нв выходе и что будет задавать на входе
"""

from abc import ABC, abstractmethod

class InCoffe(ABC):
    """Интерфейс продукта"""
    @abstractmethod
    def get_desc(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass
    

class Late(InCoffe):
    """Лате, наследуем интерфейс и определяем методы"""
    def get_desc(self):
        return 'Лате '
    
    def cost(self):
        return 24
    
# Есть интерфейс продукта и продукт
cof = Late()
print('Коффе:', cof.get_desc())
print('Стоимость:', cof.cost())

# Теперь мы хотим рассышить функционал не меняя код выше
class InDecorator(InCoffe):
    """Интерфейс для декоратора"""
    def __init__(self, coffe: InCoffe):
        self.coffe = coffe

    def get_desc(self):
        return self.coffe.get_desc()

    def cost(self):
        return self.coffe.cost()
    
class MilkDecorator(InDecorator):
    """Декораток которые изменяет"""
    def __init__(self, coffe: InCoffe):
        self.coffe = coffe

    def get_desc(self):
        return self.coffe.get_desc() + 'с молоком '
    
    def cost(self):
        return self.coffe.cost() + 5
    
cof = Late()
milk = MilkDecorator(cof)
print('Стоимость', milk.get_desc())
print('Коффе:', milk.cost())

# Добавим еще один декоратор
class NotSugarDecorator(InDecorator):
    def __init__(self, coffe):
        self.coffe = coffe

    def get_desc(self):
        return self.coffe.get_desc() + 'Без сахара'
    
    def cost(self):
        return self.coffe.cost() + 1

# Применяем еще один декоратор
notsugar = NotSugarDecorator(milk)
print('Стоимость', notsugar.get_desc())
print('Коффе:', notsugar.cost())

"""
Коффе: Лате
Стоимость 24 

-- +1-й Декторатор
Стоимость Лате с молоком
Коффе: 29

-- +2-й Декторатор
Стоимость Лате с молоком Без сахара
Коффе: 30


"""
