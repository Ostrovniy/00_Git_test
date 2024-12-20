"""
@classmethod - используеться для определения метода, который пренадлежыт самому классу, а не конкректному
экземпляру этого класса

Часть используеться для создания фабричных методов, ниже примеры
-- User.parse_obj(data)
-- np.frombuffer(data, dtype=np.uint8)
-- DatabaseSession.initialize("sqlite:///example.db")
-- Path.cwd()
-- Path.home()

"""

# (1) Счетчик
class Counter:
    # Если екземпляр класса сделает obj._count = 5
    # В этот момент в него будет свой адритуб _count
    _count = 0

    @classmethod
    def increment(cls):
        cls._count += 1

    @classmethod
    def get_count(cls):
        print(f'Текущий счет: {cls._count}')

# Текущий счет: 1
Counter.increment()
Counter.get_count()
# Текущий счет: 2
Counter.increment()
Counter.get_count()
# Текущий счет: 3
Counter.increment()
Counter.get_count()

# (2) Фабричный метод, create_by_str создает obj User
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @classmethod
    def create_by_str(cls, string: str) -> 'User':
        """'Valera, 25'"""
        name, age = string.split(',')
        return cls(name, int(age))
    
    @classmethod
    def create_by_dict(cls, dict_data: dict) -> 'User':
        """Ex: {'name': 'Vasia', 'age': 12}"""
        return cls(dict_data['name'], dict_data['age'])
    
    @classmethod
    def create_by_list(cls, data_list: list) -> 'User':
        """Ex: {'name': 'Vasia', 'age': 12}"""
        return cls(data_list[0], data_list[1])
    
    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}'

user1 = User('Anton', 22)
user2 = User.create_by_str('Valera, 25')
user3 = User.create_by_dict({'name': 'Vasia', 'age': 12})
user4 = User.create_by_list(['Marina', 54])

print(user1) # Name: Anton, Age: 22
print(user2) # Name: Valera, Age: 25
print(user3) # Name: Vasia, Age: 12
print(user4) # Name: Marina, Age: 54



