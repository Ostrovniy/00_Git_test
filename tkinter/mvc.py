# https://www.pythontutorial.net/tkinter/tkinter-mvc/
import re

class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        """
        Здесь метод email с декоратором @property выполняет роль геттера. 
        При вызове self.email он возвращает значение скрытого атрибута self.__email. 
        Этот подход позволяет использовать метод как обычный атрибут (model.email вместо model.email())
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Декоратор @<property_name>.setter используется для создания сеттера — метода, который управляет изменением значения атрибута. Он позволяет:
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')


test = Model('test@list.ru')
print(test.email)
test.email = 'seb@list.ru'
print(test.email)