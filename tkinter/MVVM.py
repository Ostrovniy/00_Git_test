import tkinter as tk
from tkinter import ttk

# Модель (Model) - хранит данные и бизнес-логику
class TextModel:
    def __init__(self):
        self._text = ""

    @property
    def text(self):
        """Получение текста геттер"""
        return self._text

    @text.setter
    def text(self, value):
        """Установка текста с проверкой и обработкой сеттер"""
        if isinstance(value, str):
            self._text = value
        else:
            raise ValueError("Текст должен быть строкой")

# ViewModel - управляет логикой данных между View и Model
class TextViewModel:
    def __init__(self, model):
        self.model = model
        self.display_text = tk.StringVar()  # Связка для отображаемого текста

    def set_text(self, value):
        """Устанавливает текст в модели и обновляет связанный текст"""
        try:
            self.model.text = value  # Устанавливаем текст в модель
            self.update_display_text()  # Обновляем связанный текст
        except ValueError as e:
            print(f"Ошибка: {e}")

    def update_display_text(self):
        """Обновляет отображаемый текст из модели"""
        self.display_text.set(self.model.text)

# Представление (View) - отображает интерфейс и взаимодействует с ViewModel
class TextView:
    def __init__(self, root, view_model):
        self.view_model = view_model

        # Поле ввода текста
        self.entry = ttk.Entry(root)
        self.entry.pack(pady=10)

        # Кнопка обновления текста
        self.button = ttk.Button(root, text="Обновить текст", command=self.update_text)
        self.button.pack(pady=5)

        # Метка для отображения текста
        self.label = ttk.Label(root, textvariable=self.view_model.display_text)
        self.label.pack(pady=10)

    def update_text(self):
        """Метод вызывается при нажатии кнопки для обновления текста в ViewModel"""
        new_text = self.entry.get()
        self.view_model.set_text(new_text)

# Основная часть для создания приложения
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Приложение с архитектурой MVVM")
    root.geometry("300x200")

    # Создаем компоненты Model, ViewModel и View
    model = TextModel()                # Модель данных
    view_model = TextViewModel(model)   # ViewModel для управления моделью
    view = TextView(root, view_model)   # Представление с интерфейсом

    root.mainloop()
