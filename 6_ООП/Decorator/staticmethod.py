"""
@staticmethod - Используеться для создания метода, который не пренадлежыт ни Класса ни
Екземпляру класса, это просто метод который находиться внутри класса. Метод можно 
вызывать как через екземпляр класса так и через класс. Такой метод не принимат self, cls

Особенности
-- Не имеет доступа к атрибутам класса или экземпляра
-- Часто используеться как вспомагательная функция, которая логически принадлежыит к классу но не зависит от его данных
-- Можно вызвать через класса и через экземпляр

"""
import random

class Randomazer:
    @staticmethod
    def get_random():
        return random.randint(0, 10)
    
    @staticmethod
    def get_randrange():
        return random.randrange(start=-4, stop=345, step=5)
    
    @staticmethod
    def get_ramdom_char(string):
        return string[random.randint(0, len(string))]
        
# Вызываем через класс
print(Randomazer.get_random())
print(Randomazer.get_randrange())
print(Randomazer.get_ramdom_char('sdfdsfsdfsdfdsfsdf'))

# Вызываем через экземпляр класса
my_random = Randomazer()
print(my_random.get_random())
print(my_random.get_randrange())
print(my_random.get_ramdom_char('sdfdsfsdfsdfdsfsdf'))



