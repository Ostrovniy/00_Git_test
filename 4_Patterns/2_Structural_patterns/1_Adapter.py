"""
Адаптер как я понял, это сиуации когда пользователь работает с определенным интерфейсом
(Тоесть у него есть класс и методы которые он знает и может работать с ними )
а также мы создали новый класс и хотим что бы пользователь с ним работать тоже, и нам нужно сделать 
так что бы интерфейсы взаимодействия были одинаковые. 

Пример: пользователь получает данные через json у него есть определенные методы для работы
Со временем мы добавили новый класс который работает уже с XML и мы хотим что бы пользователь 
абстрагировался от json или xml и у него был какой то общий интерфейс для работы "с данными" 

изначально не всегда получаеться создать какой то общий интерфейс, а в процессе рыботы появляеться 
новый источник данных и нам нужно подобгать его под существ4ующий интерфейс и эта подгонка происходит 
через класс "Адаптер" который решает эту проблему

1. Клиент (Client) - использует целевой интерфейс (Target)
2. Целефой интерфейс (Target) - определяет интерфейс который одыжает клиент
3. Адаптируемый класс (Adaptee) - класс, который нужно адаптировать к целевому интерфейсу
4. Адаптер (Adapter) - Класс, который адаптирует адаптируемый класс к целевому интерфейсу 
"""

# Вариатн 1: Композицыя
from abc import ABC, abstractmethod

class TargetInterface(ABC):
    """ Интерфейс через который будет взаимойдествоть пользователь """
    @abstractmethod
    def request(self):
        pass

# Нужно создать, потому что нельзя создать обьект TargetInterface
# Потому что используеться ABC
# Бзе ABC можно было бы напрямую создавать TargetInterface в этой точке a = Target()
class Target(TargetInterface):
    """Класс с которым будет работать пользователь"""
    def request(self):
        return 'Какой то текст класса Target'

class Adaptee:
    """ Адаптируемый класс с несовместимым интерфейсом """
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"
    
class Adapter(TargetInterface):
    """Адаптер, который преобразует интерфейс Adaptee в интерфейс Target"""
    def __init__(self):
        # Создаем обьект класса что бы адаптировать его
        # Можно также передать его по ссылке
        self.adaptee = Adaptee()

    def request(self):
        """метод который есть в интерфейсе и который нужно обьвить и переопределить что бы адаптироать результат"""
        return f'Адаптируемый результат: {self.adaptee.specific_request()[::-1]}'
    

# Функция которая будет тестировать интерфейс Target
# И она должна обработать Adapter и Target
def test_target(data: TargetInterface):
    print(data.request())

# Обычная работа с использованием класса Target который подчиняеться интерфейсу TargetInterface
a = Target()
test_target(a)

# Внутри наслудуемся от TargetInterface и переопределяем ожыдаемый метод request
# Внутри конструктора создаеться екземпляр Adaptee, от него получаем данные и даптируем для TargetInterface
b = Adapter()
test_target(b)

# Вариант 2: наследование
"""
Вместо self.adaptee = Adaptee() 
Можно использовать логику наследования 

"""