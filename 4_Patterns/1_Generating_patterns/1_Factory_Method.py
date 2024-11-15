"""
Фабричный метод — это порождающий паттерн проектирования, который определяет общий интерфейс для
создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

https://www.youtube.com/watch?v=Ni26lYMVM6k
https://www.youtube.com/watch?v=b87VdVrGQXc
https://www.youtube.com/watch?v=5LIoa4jbAVg
https://www.youtube.com/watch?v=FONWO-xdqYo
https://www.youtube.com/watch?v=ZAh3NQ9WiSg
* https://www.youtube.com/watch?v=EcFVTgRHJLM

Основная задумка которуя я понял, логика фибричного метода заключаеться в слудующем:
в определенный момоент програмы может произойти события, и мы должны создать обькт или обьекты
и мы заранее не знаем что мы будем создавать, создание обьекта может зависить от уровня, сложности игры 
или других параметров

У нас есть фабричный метод который отвечает за создание обьектов, если у нас к примеру базовая сложность
мы сотим создавать по 3 припятстия для пользщователя, причем как то рандомно создавать одно из трех препядствиий
если у нас повышеный уровень сложности мы хотим создавать 4 обьекта препятствия. Поэтому мы делегируем создания
обьектов в какой то фабричный метод, который будет возвращать уже готовые обьекты для использования

"""
import random
from abc import ABC, abstractmethod

class Obstacle(ABC):
    """Интерфейс препятствия"""
    @abstractmethod
    def update_poz(self):
        pass

    @abstractmethod
    def info(self):
        pass
    
class Cometa(Obstacle):
    """Комета, реализует интерфейс препятствия"""
    def __init__(self, x, y):
        """Координаты кометы"""
        self.x = x
        self.y = y
        self.dx = 5

    def update_poz(self):
        """Обновить позицыю кометы"""
        self.y += self.dx
    
    def info(self):
        """Получить информацию о положении для записи в файл для тестирования"""
        return f"Комета: X: {self.x} Y: {self.y}"
    
class Meteorit(Obstacle):
    """Метеорит, реализует интерфейс препятствия"""
    def __init__(self, x, y):
        """Координаты кометы"""
        self.x = x
        self.y = y
        self.dx = 10

    def update_poz(self):
        """Обновить позицыю Метеорита"""
        self.y += self.dx
        self.x += 1

    def info(self):
        """Получить информацию о положении для записи в файл для тестирования"""
        return f"Метеорит: X: {self.x} Y: {self.y}"
    
class ObstacleFactory(ABC):
    """Интерфейс фабрика препятствий"""
    @abstractmethod
    def create_obstacle(self):
        pass

class MeteoriteFactory(ObstacleFactory):
    """Создание метеорита, реализует интерфейс Фабрика препятствий"""
    @classmethod
    def create_obstacle(self):
        """Координаты Метеорита создаються рандом от 10 до 90 и от 10 до 20"""
        x = random.randint(10, 90)
        y = random.randint(10, 20)
        return [Meteorit(x, y)]
    
class CometaFactory(ObstacleFactory):
    """Создание комметы, реализует интерфейс Фабрика препятствий"""
    @classmethod
    def create_obstacle(self):
        """Координаты кометы создаються рандом от 40 до 60 и от 10 до 20"""
        x = random.randint(40, 60)
        y = random.randint(10, 20)
        return [Cometa(x, y)]
    
class GroupFactory(ObstacleFactory):
    """Создание группы обьектов, реализует интерфейс Фабрика препятствий"""
    @classmethod
    def create_obstacle(self):
        obstacles = []
        # Создание от 2 до 5 препятствий с рандомными координатами
        for _ in range(random.randint(2, 6)):
            if random.choice([True, False]):
                obstacles.append(Cometa(random.randint(40, 60), random.randint(10, 20)))
            else:
                obstacles.append(Meteorit(random.randint(10, 90), random.randint(10, 20)))
        return obstacles

def save(text):
    """Запись в файл для тестирования и проверки"""
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')

def main_loop():
    obstacles = MeteoriteFactory.create_obstacle()
    save(f"-- Установка начальной фаблики (MeteoriteFactory) перед запуском цыкла -- ")

    for tick in range(50):
        # (1) Логика обновления фабрики
        if tick == 10:
            obstacles = CometaFactory.create_obstacle()
            save(f"-- Обновления фаблики (CometaFactory) на 10-м тике -- ")
        elif tick == 20:
            save(f"-- Обновления фаблики (GroupFactory) на 30-м тике -- ")
            obstacles = GroupFactory.create_obstacle()
        # (2) Логика обновления позицыии обьектов
        for obstacle in obstacles:
            obstacle: Obstacle
            obstacle.update_poz()
            save(f"#{tick}: {obstacle.info()}")

        print(tick, obstacles)


main_loop()

"""
Описание програмы

Obstacle - Интерфейс, для препятствий
- Cometa - перпятствие в виде кометы
- Meteorit - Препятствие в виде метеорита

ObstacleFactory - интерфейс фабричного метода
- MeteoriteFactory - фабрика которая создает метеорит
- CometaFactory - фабрика которая создает кометры
- GroupFactory - фабрика которая аоздает рандомную группу из метеоритов и коммет

main_loop - запускает игровой цынк на 50 тиков
- в начеле запускаеться фабрика метеоритов
- на 10-м тике обновляеться фабрика уже на фабрику комет
- на 30-м тике, обновляеться фабрика и уже запускаеться фабрика комет

1. Можно добавить новое препятствие в виде корабля (Реализовав интерфейс Obstacle)
2. Можно создать новую генерацию препятствий реализовав новую фабрику (Реализовал интерфейс ObstacleFactory)
3. В гравном цыкле можно настроить логику, когда будет запускаться новая генерация препятсвтий (При каком условии)
"""
