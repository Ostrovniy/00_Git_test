"""
Инкапсуляция — это концепция в объектно-ориентированном программировании (ООП), которая позволяет объединить данные и методы, 
работающие с этими данными, внутри одного объекта и скрыть детали реализации от внешнего мира. 
Основная цель инкапсуляции — защитить данные от некорректного или нежелательного доступа и изменения, обеспечивая интерфейсы для работы с объектом.
"""

# Первый пример: топорная реализация
class Person:
    def __init__(self, name, start_balans):
        self.name = name # Публичное поле
        self._balans = start_balans # Приватное поле

    # Аналог Геттреа, возвращаем баланс через метод
    def get_balans(self):
        return self._balans
    
    # Аналог сеттер, только работает как инкримент
    def add_value_to_balans(self, value):
        if value < 0:
            print('Нельзя добавить 0 или минусовое число')
        else:
            self._balans += value

# Второй пример: Реализовано так как задумано в Пайтон
class PersonPro:
    def __init__(self, name, start_balans):
        self.name = name # Публичное поле
        self._balans = start_balans # Приватное поле

    # Обращаемся для получения баланса obj.balans
    @property
    def balans(self):
        return self._balans
    
    # Обращаемся для устновления баланса obj.balans = 100
    @balans.setter
    def balans(self, value):
        self._balans = value

# Пример использования
pers = PersonPro('Yura', 100)
print(pers.balans) # 100
pers.balans = 200
print(pers.balans) # 200