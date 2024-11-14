"""
Агрегация — это специальный вид ассоциации, когда один объект выступает "целым", а другие — его "частями". 
Однако, в отличие от композиции, "части" могут существовать независимо от "целого". 
Обычно это отражает более тесную связь, чем ассоциация, но не до степени "жизненной зависимости".

Пример: Университет и Студенты. Университет "состоит" из студентов, но студенты могут существовать независимо, 
вне зависимости от того, существует ли университет или нет. Это "часть-целое", но оно не столь жёсткое, как в композиции.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name} {self.age}"

class Univers:
    def __init__(self, name):
        self.name = name
        self.stud = []

    def add_studenta(self, sudent: Student):
        self.stud.append(sudent)

    def print_all_stud(self):
        for stud in self.stud:
            print(stud)


un = Univers('Подзалупянск')

st1 = Student('Чорт', 20)
st2 = Student('Голубь', 21)
st2 = Student('Гусь благородный', 22)

un.add_studenta(st1)
un.add_studenta(st2)
un.add_studenta(st2)

un.print_all_stud()

# Student: Чорт 20
# Student: Гусь благородный 22
# Student: Гусь благородный 22



