# https://www.pythontutorial.net/tkinter/tkinter-mvc/
import re
import tkinter as tk
from tkinter import ttk

# (1) Если я нажымаю кнопку, и эта кнопка меняет цвет фона, измененяи цвета фона должно быть вызвано через Представления или КОнтроллер
# (1) В представлении должна быть функция изменения цвета, а вызывает ее контроллер
# (2) Методы которые определы в Модели, они должны или выполнять какое то действие внутри себя или выполнять его и верзвращать результат который будет принимать контроллре, при этом запуск метода происходит в контроллере ?
# (2) Да

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


#test = Model('test@list.ru') # (1) Сохздания
#print(test.email) # (2) геттер
#test.email = 'seb@list.ru' # (3) сеттер
#print(test.email) # (4) геттер

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label - Заголовок для поля ввода
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        # email entry - Поле ввода почты
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button - Кнопка сохранить
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message - Текст валидации
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # Поумолчанию контроллер пустой
        self.controller = None

    def set_controller(self, controller):
        """Установка контроллера для Представления"""
        self.controller = controller

    def save_button_clicked(self):
        """Обработка нажатия на кнопку"""
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """Ситуация когда ввели не валидный текст"""
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        #self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """Ситуация когда ввели валидный текст"""
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """Очистить поле ввода"""
        self.message_label['text'] = ''

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        try:
            # Плпытка утановить email с валидацией + сохранения в БД
            self.model.email = email
            self.model.save()

            # Обращаемся к представлению и меняем Стиль текста на успешный
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # Обращаемся к представлению и меняем Стиль текста на ошибку
            self.view.show_error(error)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # (1) Создание модели
        model = Model('hello@pythontutorial.net')

        # (2) Создания представления
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # (3) Создания контроллера
        controller = Controller(model, view)

        # (4) Установка контроллера
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()