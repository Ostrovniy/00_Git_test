"""
Принцип разделения интерфейса (Interface Segregation Principle, ISP)
Это означает, что интерфейсы (или базовые классы) должны быть узконаправленными и 
определять только те методы, которые действительно нужны для их использования.

Если интерфейсы или базовые классы слишком широкие, то классы-наследники или 
реализации вынуждены будут "перегружаться" лишней функциональностью. Это усложняет 
разработку, тестирование и сопровождаемость кода.
"""

from abc import ABC, abstractmethod

# Базовый интерфейс любого обьвления
class InterfaceAnnouncementsCore(ABC):
    @abstractmethod
    def set_price(self, price):
        pass 
    
# Интерфейс обьвлений для портала пром
class InterfaceAnnouncementsProm(ABC):
    @abstractmethod
    def get_url_site(self, price):
        pass 

# Интерфейс обьвлений для портала Розетка
class InterfaceAnnouncementsRozetka(ABC):
    @abstractmethod
    def get_rating(self):
        pass 

# Класс упарелениями обьвлений товаров на сайте Пром
class AnnouncementsProm(InterfaceAnnouncementsProm, InterfaceAnnouncementsCore):
    def set_price(self, price=0):
        """Цена есть у любого обьвления"""
        print('Установка цены интерфейсом InterfaceAnnouncementsCore')

    def get_url_site(self):
        """Ссылка на сайт есть только у Пром"""
        print('Получение ссылки на сайт интерфейсом get_url_site')

# Класс упарелениями обьвлений товаров на сайте Розетка
class AnnouncementsRozetka(InterfaceAnnouncementsCore, InterfaceAnnouncementsRozetka):
    def set_price(self, price=0):
        """Цена есть у любого обьвления"""
        print('Установка цены интерфейсом InterfaceAnnouncementsCore')

    def get_rating(self):
        """Рейтинг есть только у Резотки"""
        print('Получения рейтинга обьвления для розетки')


site_my_prom = AnnouncementsProm()
site_my_rozetka = AnnouncementsRozetka()

site_my_prom.set_price()        # Установка цены интерфейсом InterfaceAnnouncementsCore
site_my_rozetka.set_price()     # Установка цены интерфейсом InterfaceAnnouncementsCore

site_my_prom.get_url_site()     # Получение ссылки на сайт интерфейсом get_url_site 
site_my_rozetka.get_rating()    # Получения рейтинга обьвления для розетки
