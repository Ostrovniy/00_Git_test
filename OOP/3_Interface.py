"""
Интерфейс, по сути, это “чистый контракт”, содержащий только сигнатуры методов, но не их реализацию. 
Он описывает функциональность, которую должен поддерживать класс, но не говорит, как это должно быть реализовано. 
Например, интерфейс может содержать только название метода и его параметры, без какого-либо кода.

Когда использовать интерфейс, а когда абстрактный класс?
    Интерфейс: Если нужно только определить набор обязательных методов, и вы не хотите давать никакой базовой реализации.
    Абстрактный класс: Если требуется задать методы, которые нужно реализовать, и при этом нужно создать некоторую общую 
    функциональность для классов-наследников.

как я понял, в Абстрактный клас можно задать методы которые можно как то определить, а в Интерфейсе ничего определять нельзя
только класс с методами которые нужно определить в наслудуемом классе
"""

# 1. Подключения библиотек для работы с абстракцией
from abc import ABC, abstractmethod

# 2. Создание абстрактного(ИНТЕРФЕЙСА) класса
class RectangleInterface(ABC):
    # 3. Создание абстрактного метода
    @abstractmethod
    def area(self):
        pass

# 3. Наследуемся от RectangleInterface
class Rectangle(RectangleInterface):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 4. Обязательно нужно определить area метод, иначе будет ошибка
    def area(self):
        return self.width * self.height


print(Rectangle(5, 10).area()) # 50
