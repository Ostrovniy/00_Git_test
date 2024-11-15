"""
Принцип подстановки Лисков (Liskov Substitution Principle, LSP) — это третий принцип SOLID, который гласит, 
что объекты подклассов должны быть заменяемыми объектами их базового класса, без нарушения ожидаемой работы 
программы. То есть, если у нас есть класс-наследник, он должен вести себя так, чтобы его можно было 
использовать вместо родительского класса, и программа при этом работала корректно.

Этот принцип помогает проектировать иерархию классов так, чтобы наследование было логичным и функционально 
правильным. В противном случае, при подстановке дочернего класса вместо базового могут возникать ошибки и 
нежелательное поведение.
"""

# Не соблюдения принцыпа LSP
class Rectangle:
    """Прямоугольник, где можно изменить высоту и длину"""
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def set_w(self, w):
        """Устновить ширину"""
        self.w = w
    
    def set_h(self, h):
        """Устновить высоту"""
        self.h = h

    def get_area(self):
        """Вернуть прощадь"""
        return self.h * self.w


class Square(Rectangle):
    """Квадрат это частный случай прямоугольника
    Конструктор и расчет площади переопределять не нужно"""
    def set_w(self, w):
        """Устновить ширину"""
        self.w = w
        self.h = w
    
    def set_h(self, h):
        """Устновить высоту"""
        self.h = h
        self.w = h

# Тестирований плохой ситуации
def test(rectangle):
    rectangle.set_w(5)
    rectangle.set_h(10)
    print(rectangle.get_area())


one = Rectangle(1, 1)
test(one) # 50

too = Square(1, 1)
test(too) # 100

"""Ответ 100 из за того что квадрат сначала было 5 на 5 и потом стал 10 на 10 и уже была расчитана площать квадрата
но выглядет конечно да, не очень логично с точти кзерния читаимости """

# соблюдения принцыпа LSP
class Bird:
    def eat(self):
        print('Bird eat')
    
    def fly(self):
        print('Bird fly')

class Sparrow(Bird):
    def fly(self):
        print('Sparrow fly')

class Eagle(Bird):
    def fly(self):
        print('Eagle fly')

# Добавляем подкласс для нелетающих птиц
class FlightlessBird(Bird):
    def fly(self):
        raise NotImplementedError('Cant fly')

class Penguin(FlightlessBird):
    def swim(self):
        print('Penguin swim')


def let_fly(bird: Bird):
    try:
        bird.fly()
    except NotImplementedError as e:
        print(e)

# Использование
sparrow = Sparrow()
eagle = Eagle()
penguin = Penguin()

let_fly(sparrow)   # Выведет: Sparrow fly
let_fly(eagle)     # Выведет: Eagle fly
let_fly(penguin)   # Выведет: Cant fly

"""Мы можем передать любой клсс который наслудует Bird и все корректно будет работать"""