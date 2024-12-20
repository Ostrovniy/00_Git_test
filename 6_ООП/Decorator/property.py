"""
@property - это декорато который позволяет согдавать Геттеры и сеттеры и делитерры
для атрибутов класса, это добавляет логику при доступе к атрибуту, изменении удалении

Зачем нужен
-- Контроль доступа к атрибутам: например проверка значения перед установкой
-- Инкапсуляция: скрывает реализацию за интерфейсом, предоставляя доступ через свойство
-- Сохранения совместимости, если атрибут становиться сложным для вычисления, можно перключиться на метод 
"""

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """Возвращает значения"""
        if not hasattr(self, '_value'):
            raise AttributeError('Атрибут _value был удален, нужно указать значения еще раз test1.value = 557')
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Устанавливает значения"""
        self._value = new_value

    @value.deleter
    def value(self):
        """Удаляет значения"""
        del self._value

test1 = MyClass(5)
print(test1.value)
test1.value = 55
print(test1.value)
del test1.value
#print(test1.value)


# (2) Прямоугольник
class Rectangle:
    def __init__(self, w, h):
        self._w = w
        self._h = h

    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, new_w):
        if new_w < 0:
            raise ValueError('Ширина не может быть отрицательной')
        self._w = new_w

    @property
    def h(self):
        return self._h
    
    @h.setter
    def h(self, new_h):
        if new_h < 0:
            raise ValueError('Высота не может быть отрицательной')
        self._h = new_h

    @property
    def area(self):
        """Обратить внимания, атрибут который не создавался и его можно только прочиать"""
        return self._h * self._w
    

figura = Rectangle(5, 10)
figura.w = 20
figura.h = 100
print(figura.area)


# (3) Кеширования, как я понял задумку, пока к атрибуту не обращаться значения не будет расчинато
# Тоесть расчет значения происходит только в момент обращения к нему

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print('(0) Момет вычисления...')
            self._area = self.radius ** 2 * 3.14
        print('(1) Возвращения результата')
        return self._area
    
fig2 = Circle(10)
print(fig2.area)
print(fig2.area)


# Примеры использования атрибутов для чтения, без возможности установки
"""
from datetime import datetime

dt = datetime.now()
print(dt.year)  # 2024
print(dt.month) # 12
print(dt.day)   # 20
"""

"""
from pathlib import Path

p = Path("/some/file.txt")
print(p.name)       # file.txt
print(p.stem)       # file
print(p.suffix)     # .txt
"""