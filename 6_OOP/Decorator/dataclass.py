"""
dataclass - это встроенные дкторатор в Патон, который используеться для упрощения создания классов.
Предназначеный для хранения данных. Он автоматически добавляет методы, такие как __init__, __repr__,
__eq__ , и другие, избавляет от необходимости ручной реализации этих методов

Основные преимущества
1.Автоматическая генерация методов
    __init__: Создает и иницыализирует обькт
    __repr__: Удобное строковое представления обьекта
    __eq__: Сравнения обьектов по их атрибутам
    __hash__: (опцыонально) Гернерация хеш кода для обьекта
2. Упрощеия работы с данными: Лаконичный и чидаемый код для классов, которые в основном предназначены
для хранения данных
3. Допольнительный функции
    Установка значений по умолчанию
    Поля с определенными свойствами через field()
"""

from dataclasses import dataclass, field, asdict, astuple, replace

@dataclass(order=True, frozen=True)
class Product:
    # Поля класса
    id: int                 # Уникальный индификатор товара
    name: str               # Название товара
    price: float = 0.0      # Цена по умолчанию
    stock: int = field(default=0, init=False, repr=False) # Поле исключено из __init__ и __repr__
    category: str = field(default='General', compare=False) # Игнорируется при сравнении объектов

    # Метод класса
    def calculate_discounted_price(self, discount: float) -> float:
        """Вернуть цену с учетом скидки"""
        return self.price * (1 - discount / 100 )
    
product1 = Product(id=1, name='laptop', price=1200.0)
product2 = Product(id=2, name='Smartphone', price=800.0)
product3 = Product(id=3, name='LapTop', price=1200.00)

# Использование автоматического сравнения
print(product1 == product3)  # True (сравнение по всем полям, кроме category)
print(product1 < product2)   # False (сравнение по цене, так как order=True)

# Использование замороженного объекта
# product1.price = 1000  # Ошибка: невозможно изменить поле, так как frozen=True

# Использование методов
print(product1.calculate_discounted_price(10))  # 1080.0 (цена со скидкой 10%)

# Преобразование объекта в словарь
print(asdict(product1))  
# {'id': 1, 'name': 'Laptop', 'price': 1200.0, 'category': 'General'}

# Преобразование объекта в кортеж
print(astuple(product1))  
# (1, 'Laptop', 1200.0, 'General')

# Создание копии с изменением некоторых полей
product4 = replace(product1, price=1000.0)
print(product4)  # Product(id=1, name='Laptop', price=1000.0, category='General')

# Исключение поля из repr и init
print(product1)  # Поле stock не отображается в __repr__


"""
Как по мне сложноватая штука, но полезная
"""

"""
Что здесь показано:
    frozen=True: Объект становится неизменяемым. Поля нельзя изменить после создания объекта.
    order=True: Объекты можно сравнивать (<, >, <=, >=) на основе их полей.

Значения по умолчанию: Для price и category.
    field:
        default=0: Устанавливает значение по умолчанию.
        init=False: Поле исключено из конструктора (__init__).
        repr=False: Поле исключено из строкового представления (__repr__).
        compare=False: Поле игнорируется при сравнении объектов.

Методы модуля dataclasses:
    asdict: Преобразование объекта в словарь.
    astuple: Преобразование объекта в кортеж.
    replace: Создание нового объекта с изменёнными значениями полей.
    
Метод класса: Пример метода для бизнес-логики.
"""