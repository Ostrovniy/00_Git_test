"""
Декораторы для классов — это функции, которые принимают класс как аргумент и возвращают 
модифицированный или новый класс. Они позволяют добавлять, изменять или расширять 
функциональность класса без изменения его исходного кода.

"""

# Декторатор для проверки прав доступа

def require_permission(permissions):
    """Декторатор для проверки прав доступа"""
    def decorator(cls): #cls - это класс в котором применяеться декоратор
        # Создаем словарь в котором будет названия метода и ссылка на его
        # Что бы в cls.__dict__.items() выбрать методы нужно воспользоваться функцией callable она вернет True есть method  "вызываемый"
        # Пример заипси, названия и значения в словаре
        # name: __init__, method: <function Test.__init__ at 0x000001960B4D1080>, callable -> True
        # name: methodone, method: <function Test.methodone at 0x000001960B4D1120>, callable -> True
        # name: value3, method: <property object at 0x000001960B4C3E20>, callable -> False
        original_methods = {name: method for name, method in cls.__dict__.items() if callable(method)}

        # Проходим по всем методам
        for name, method in original_methods.items():
            # Оборачиваем каждый метод в новую функцию, которая выполняет проверку прав
            # original_method=method штука против замыкания, тут не сильно понял
            # Походе на проброс ссылки
            def wrapped_method(self, original_method=method, *args, **kwargs):
                # Проверяем есть ли обьекта атрибут permission 
                # Проверяем что self.permissions совпадает с аргументом который передаеться в декоратор premission
                # Пример: начальная точка откуда беруться переменные для сравннеия obj.permissions = ["admin"] // @require_permission("admin")
                if not hasattr(self, 'permissions') or permissions not in self.permissions:
                    raise(f"Access denied: Missing permission '{permissions}'")
                
                # Если права достпа совпадают возвращаем оригинальный метод
                return original_method(self, *args, **kwargs)
            
            # Заменяем стандартны метод класса на метод с оберткой
            # Ссылка на класс, названия атрибута (метода) и ссылка на метод который будет установлен
            setattr(cls, name, wrapped_method)
        
        return cls # Возвращаем модифицированный класс
    return decorator # Возвращаем сам декоратор


# Использования декторатора и класс будет доступен только для Амина
@require_permission(permissions='admin')
class ToDo:
    permissions = [] # По умолчанию нету никаких прав доступа

    def add(self):
        print(f'Добавления новой задачи')

    def delet(self):
        print(f'Удаления задачи:')


yura = ToDo()
# Если обратиться к методу без прав доступа будет ошибка 
# yura.add() #  raise(f"Access denied: Missing permission '{premission}'")

# Установления доступа Админ, такой же доступ указан в декораторе
yura.permissions = ['admin']

# Полсе установки доступа, можно вызывать методы
yura.add() # Добавления новой задачи
yura.delet() # Удаления задачи:



