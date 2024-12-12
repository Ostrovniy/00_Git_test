"""
Одиночка, екземпляр класса можно создать только один раз, реализация чуть сложная для меня, реализовано все так
есть класс Singleton он являеться МетаКлассов, тоесть класс для управления другими классами. _instansens это словрь который
хранить в этом класса в формает  {<class '__main__.DataBase'>: <__main__.DataBase object at 0x000002135A79E690>}
Тоесть названия класса и его екземляр (это две ссылки как я понял)

def __call__ это переопределнеия вызова, вызов это когда ClassName() - скодки это момент вызова и запускаеться метод call который
как я понял запускает __init__ внутри себя (ну это не точно) далее, мы проверяем что Класс <class '__main__.DataBase'> не находиться 
в словаре в виде ключа. если это так, то мы создаем <class '__main__.DataBase'> через вызов call и добавляем его в словарь 
ключ это ссылка на класс а значения это обьек класса

Для понимания: 
self подставляем ссылку на обьект <__main__.DataBase object at 0x000002135A79E690>
cls подставляет ссылку на класс <class '__main__.DataBase'>


"""

# Класс одиночка реализован через мета класс (Класс для управления классами)
# Наивный одиночка, без учета многопоточности приложения
class Singleton(type):
    # Словарь в котором будет созданный обьект
    # {<class '__main__.DataBase'>: <__main__.DataBase object at 0x000002135A79E690>}
    _instansens = {}

    # Переопределяем оператор выхова класса
    def __call__(cls, *args, **kwards):
        # Если класс Singleton нету в словаре
        if cls not in cls._instansens:
            # Создаем обьект и сохраняем его в переменную instance 
            instance = super().__call__(*args, **kwards)
            # Помещаем созданный обьект в словарь класса
            cls._instansens[cls] = instance

        # Возвращаем обьект который создали, или который уже был создан
        return cls._instansens[cls]
    

class DataBase(metaclass=Singleton):
    def __init__(self, host, port, password, logon):
        self.list_data = []
        self.list_data.append(host)
        self.list_data.append(port)
        self.list_data.append(password)
        self.list_data.append(logon)

    def __str__(self):
        return f'{self.list_data}'
    
# Момент создания обьекта
db = DataBase('local', 1998, '1111', 'lox')
print(db, id(db))

# Это просто не сработает, второй раз просто идет игнорирование
db2 = DataBase('local2', 19982, '11112', 'lox2')
print(db2, id(db2))


# ['local', 1998, '1111', 'lox'] 2184190748160
# ['local', 1998, '1111', 'lox'] 2184190748160


"""
Создания одиночки для ситуаии многопоточности, что бы случайно не создавть два раза
все тоже самое только используеться. _lock: Lock = Lock() и with cls._lock:
также запуск происходит через Thread тут я мало что понимаю, просто по примеру сделал
"""

# Одиночка при условии что есть многопоточность
from threading import Lock, Thread

class SingletonMeta(type):
    _instansens = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwds):
        with cls._lock:
            if cls not in cls._instansens:
                instansen = super().__call__(*args, **kwds)
                cls._instansens[cls] = instansen
            return cls._instansens[cls]
    

class DataBase2(metaclass=Singleton):
    def __init__(self, host, port, password, logon):
        self.list_data = []
        self.list_data.append(host)
        self.list_data.append(port)
        self.list_data.append(password)
        self.list_data.append(logon)

    def __str__(self):
        return f'{self.list_data}'
    


# Запуск в двух процессах, тут ничего не шарю просто пример переделал для запуска
def test_singleton() -> None:
    singleton = DataBase2('local2', 19982, '11112', 'lox2')
    print(singleton)

def test_singleton2() -> None:
    singleton = DataBase2('ваыпыавп', 5647645, 'выапаыв', 'прпа')
    print(singleton)

process1 = Thread(target=test_singleton)
process2 = Thread(target=test_singleton2)

process1.start()
process2.start()

# ['local2', 19982, '11112', 'lox2']
# ['local2', 19982, '11112', 'lox2']