"""
Абстрактная фабрика (Abstract Factory) — это порождающий паттерн проектирования, который 
предоставляет интерфейс для создания семейств взаимосвязанных или взаимозависимых 
объектов, не уточняя их конкретные классы. 

Основная идея паттерна
Фабричный метод создает объекты одного типа, а Абстрактная фабрика создает целые семейства 
объектов, которые должны работать вместе.
Все объекты, созданные одной фабрикой, совместимы друг с другом.

https://www.youtube.com/watch?v=v-GiuMmsXj4
"""

"""
Есть игровое поле которые состоит из трех частей, шапка, поле, подвал
Эти 3 поля могут быть в разных состояниях (Стандартное, Опасность, Скорость)
Разача будет реализована с помощю абстрактной фабрики, будет 3 интерфейса для трех чатей
и для каждого интерфейса будет создано по 3 класса реализации, для каждого состояния
Бдует создана абстрактаня фабрика для состояния с тремя методами, получания одного из трех полей
также будет создано 3 реализации для трех состояний
Схема:
- Класс: ИнтерфейсФабрикиСостояния
- Класс: Состояние Стандарное (внутри 3 метода)
- Класс: Состояние Опасность (внутри 3 метода)
- Класс: Состояние Скорость (внутри 3 метода)
- Класс: ИнтрефейсПоляШапка
- Класс: ИнтрефейсПоляПоле
- Класс: ИнтрефейсПоляПодвал
- Класс: ШапкаСтандартная
- Класс: ШапкаОпасная
- Класс: ШапкаСкорость
- Класс: ПолеСтандартная
- Класс: ПолеОпасная
- Класс: ПолеСкорость
- Класс: ПодвалСтандартная
- Класс: ПодвалОпасная
- Класс: ПодвалСкорость
"""

from abc import ABC, abstractmethod

# ------------------------------------------------------------------------------- Интерфейсы
# Интерфес для каждого продукта (Шапка, Поле, Подвал)
# Интерфейс фабрики создания продуктов 
class IntHead(ABC):
    """Интерфейс шапри приложения"""
    @abstractmethod
    def render():
        """Рендер шапки приложения"""
        pass

class IntBody(ABC):
    """Интерфейс Поля приложения"""
    @abstractmethod
    def render():
        """Рендер Поля приложения"""
        pass

class IntBasement(ABC):
    """Интерфейс Подвала приложения"""
    @abstractmethod
    def render():
        """Рендер Подвала приложения"""
        pass

class IntStateFactory(ABC):
    """Интерфейс фабрики которая возращает компонены игрового поля"""
    @abstractmethod
    def create_head() -> IntHead:
        """Возвращает шапку приложения"""
        pass

    @abstractmethod
    def create_body() -> IntBody:
        """Возвращает поле приложения"""
        pass
    
    @abstractmethod
    def create_basement() -> IntBasement:
        """Возвращает подвал приложения"""
        pass

# ------------------------------------------------------------------------------- реализация продуктов
# -------------------------------- Шапка (Стандартная, Опасная, Скорсоть) 
class HeadStandart(IntHead):
    def render(self):
        return 'HeadStandart-render'
    
class HeadDanger(IntHead):
    def render(self):
        return 'HeadDanger-render'
    
class HeadSpeed(IntHead):
    def render(self):
        return 'HeadSpeed-render'

# -------------------------------- Поле (Стандартная, Опасная, Скорсоть) 
class BodyStandart(IntBody):
    def render(self):
        return 'BodyStandart-render'
    
class BodyDanger(IntBody):
    def render(self):
        return 'BodyDanger-render'
    
class BodySpeed(IntBody):
    def render(self):
        return 'BodySpeed-render'
    
# -------------------------------- Подвал (Стандартная, Опасная, Скорсоть) 
class BasementStandart(IntBasement):
    def render(self):
        return 'BasementStandart-render'
    
class BasementDanger(IntBasement):
    def render(self):
        return 'BasementDanger-render'
    
class BasementSpeed(IntBasement):
    def render(self):
        return 'BasementSpeed-render'
    
# ------------------------------------------------------------------------------- реализация Фабрик
class StandartFactory(IntStateFactory):
    def create_head(self) -> IntHead:
        return HeadStandart()
    
    def create_body(self) -> IntBody:
        return BodyStandart()
    
    def create_basement(self) -> IntBasement:
        return BasementStandart()
    
class DangerFactory(IntStateFactory):
    def create_head(self) -> IntHead:
        return HeadDanger()
    
    def create_body(self) -> IntBody:
        return BodyDanger()
    
    def create_basement(self) -> IntBasement:
        return BasementDanger()
    
class SpeedFactory(IntStateFactory):
    def create_head(self) -> IntHead:
        return HeadSpeed()
    
    def create_body(self) -> IntBody:
        return BodySpeed()
    
    def create_basement(self) -> IntBasement:
        return BasementSpeed()
    
# --------------------------------------------------------------------------- Тестирования кода
def save(text):
    """Запись в файл для тестирования и проверки"""
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')

def main_loop():
    # начальная фабрика и 3 компонена
    gui_factory = StandartFactory()
    head = gui_factory.create_head()
    body = gui_factory.create_body()
    basement = gui_factory.create_basement()

    for tick in range(50):
        # Запись в текстовый документ
        save(f"{tick}: Обновления - {head.render()}")
        save(f"{tick}: Обновления - {body.render()}")
        save(f"{tick}: Обновления - {basement.render()}")
        save('-'*35)

        if tick == 10:
            # Обновления фабрики и комонентов Danger
            gui_factory = DangerFactory()
            head = gui_factory.create_head()
            body = gui_factory.create_body()
            basement = gui_factory.create_basement()

        elif tick == 30:
            # Обновления фабрики и комонентов Speed
            gui_factory = SpeedFactory()
            head = gui_factory.create_head()
            body = gui_factory.create_body()
            basement = gui_factory.create_basement()

        print(tick)


main_loop()

"""
Описание програмы

- IntHead - Интекфейс для шапки приложения
- IntBody - Интерфейс для поля приложения
- IntBasement - Интерфейс для подвала приложения

- IntStateFactory - Интерфейс фабрики, который будет создавать обьекты (IntHead, IntBody, IntBasement)
-- Метод: create_head: Создает обьект интерфейса IntHead
-- Метод: create_body: Создает обьект интерфейса IntBody
-- Метод: create_basement: Создает обьект интерфейса IntBasement
** При добавлении нового компонента, нужно создать для него интерфейс и добавить метод в фабрику

# Было задумано 3 стиля для трех компонентов, классы определяют обьекты на основе интрфейсов
- HeadStandart, HeadDanger, HeadSpeed: Реализация интерфейса IntHead
- BodyStandart, BodyDanger, BodySpeed: Реализация интерфейса IntBody
- BasementStandart, BasementDanger, BasementSpeed: Реализация интерфейса IntBasement
** При добавлении нового стиля, нужно создать и определить компонены на основе интерфейсов

# реализация трех фабрик для трех стилей на основе интерфейса IntStateFactory
- StandartFactory - реализация трех методов которые возвращают (create_head:HeadStandart, create_body:BodyStandart, create_basement:BasementStandart)
- DangerFactory - реализация трех методов которые возвращают (create_head:HeadDanger, create_body:BodyDanger, create_basement:BasementDanger)
- SpeedFactory - реализация трех методов которые возвращают (create_head:HeadSpeed, create_body:BodySpeed, create_basement:BasementSpeed)

main_loop - обновляет фабрику (StandartFactory на DangerFactory на SpeedFactory)
Таким образом мы всегда получаем обьекты интерфейса IntHead, IntBody, IntBasement но определенной реализации
Определенного стиля Standart, Danger, Speed

** Код ниже: Думаю это не лучшая реализация обновления фабрики, но для примера пусть будет
gui_factory = DangerFactory()
head = gui_factory.create_head()
body = gui_factory.create_body()
basement = gui_factory.create_basement()

1. Для добавления нового компонента нужно, 
-- реализовать его интерфейс, 
-- добавить метод в интрфейс фабрики, 
-- реализовать интерфейс для трех стилей (Создать 3 класса)
-- Обновить каждую фабрику, реализовать метод который был создан

2. для добавления новго стиля
-- Реализовать группу компонентов (3 штуки) (Создать 3 класса) и стилизовть их
-- Создать класс новой фабрики и реализовать его
-- Можно использовать новый класс фабрики

"""


