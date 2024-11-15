"""
Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)

Модули верхнего уровня не должны зависеть от модулей нижнего уровня. Оба должны зависеть от абстракций. 
Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
"""

# Нарушение принципа DIP
class Email_sender:
    def send_email(self, text):
        print(f'Отправка Email {text}')

class Notification:
    def __init__(self):
        self.email_sender = Email_sender()

    def notify(self, text):
        self.email_sender.send_email(text)

notif = Notification()
notif.notify('Мой текст') # Отправка Email Мой текст

"""Проблема, как только появиться уведомления через смс, то сразу прийдеться переделывать Notification"""

# Без нарушения принцыпа
from abc import ABC, abstractmethod

class Sender(ABC):
    """Интерфейс для отправки сообщения"""
    @abstractmethod
    def send(self, text):
        pass

class Email_sender(Sender):
    """Отправка смс через почту"""
    def send(self, text):
        print(f'Отправка Email_sender: {text}')

class Sms_sender(Sender):
    """Отправка смс через смс"""
    def send(self, text):
        print(f'Отправка Sms_sender: {text}')

class Notification:
    def __init__(self, sender: Sender):
        self.sender = sender

    def notify(self, messege):
        self.sender.send(messege)

email = Email_sender()
sms = Sms_sender()

notif1 = Notification(email)
notif2 = Notification(sms)

notif1.notify('email текст')    # Отправка Email_sender: email текст
notif2.notify('sms текст')      # Отправка Sms_sender: sms текст

"""В текущий момент можно создать новый клалас, унаследовать интерфейс Sender и класс Notification сможет
принимать новый способ отправки уведомления
"""
