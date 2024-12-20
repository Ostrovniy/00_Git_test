"""
Прокси - это по сути обертка для какогото обьекта, предположым что у нас есть класс для упарвелния 
таблицей в Бд, записи файла или получения файла, мы создаем класс прокси который может делать 
все тоже самое что и основной класс, но теперь мы можем перед запросов выполнить определенные дейсвтия
к примеру провреить уровен доступа и решыть предоставлять доступ к таблице или нет. или можем делать логитрования 
и таким образом у нас логирования все будет в прокси слассе а основной клсасс будт чистый 
+ для прокси и основного класс лучше создать общий интерфейс
"""

from abc import ABC, abstractmethod

# Интерфейс для управления таблице и прокси
class Interface(ABC):
    @abstractmethod
    def get(self):
        pass
    @abstractmethod
    def _set(self):
        pass

# Упавления таблицей, тут мы не хотим на пярмую давать доступ
class Tableusers(Interface):
    def get(self):
        print('Tableusers.get')

    def _set(self):
        print('Tableusers.get')

# прокси создает таблицу и делает такой же функциона
# + Добавляет свой функционал
class ProxytableUser(Interface):
    def __init__(self):
        # можно как передать ссылку на Tableusers
        # можно и создать внутри
        self.table = Tableusers()

    def get(self):
        print('ProxytableUser.get')
        self.table.get()

    def _set(self):
        print('ProxytableUser._set')
        self.table._set()


proxymanager = ProxytableUser()
proxymanager.get()
print('----------------')
proxymanager._set()
