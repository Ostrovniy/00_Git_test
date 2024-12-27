"""
Цепочка запросов - это ситуация когда у нас есть много проверок, причем проверки до первого вхождения
К примеру нужно проверить что. пользоватлеь авторизовался, прошла аунтификаци, есть доспук к странице
Отрисовка страницы, в этой цепочки есть логическая последовательность. если какое то услвия выполнилось
нету аутификации тогда дальше проверку можно остановить

Патерн логически очень понятен, реализация сложноватая для понимания. Есть один общий Хендрел, в котором
прописаны методы установлниея следующего обработчика по цепочки и метод заготовка для обработки условий проверки
Дальшее есть классы которые наслудуют базовый Обработчик и реализуют метод обработки условия, и они или обрабатывают условия
или передают дальше по цепочки
"""

# Основной обработчик, структура
class Handler:
    def __init__(self):
        # Слудующий хендлер по цепочки
        self.next_handler = None

    # Установить слудующий хендлер
    def set_handler(self, new_handler):
        self.next_handler = new_handler
        return new_handler

    def handler(self, request):
        if self.next_handler:
            self.next_handler.handler(request)

# Конкретный обработчик 1
class Login(Handler):
    def handler(self, request):
        if request == 'Login':
            print('Обработка: Login')
        elif self.next_handler:
            print('Пропуск: Login')
            self.next_handler.handler(request)

# Конкретный обработчик 2
class Autnif(Handler):
    def handler(self, request):
        if request == 'Autnif':
            print('Обработка: Autnif')
        elif self.next_handler:
            print('Пропуск: Autnif')
            self.next_handler.handler(request)

# Конкретный обработчик 3
class Poot(Handler):
    def handler(self, request):
        if request == 'Poot':
            print('Обработка: Poot')
        elif self.next_handler:
            print('Пропуск: Poot')
            self.next_handler.handler(request)

# Конкретный обработчик 4
class Page(Handler):
    def handler(self, request):
        if request == 'Page':
            print('Обработка: Page')
        elif self.next_handler:
            print('Пропуск: Page')
            self.next_handler.handler(request)


class Client:
    # Создания всех обработчиков
    hend1 = Login()
    hend2 = Autnif()
    hend3 = Poot()
    hend4 = Page()

    # Настройка цепочки
    hend1.set_handler(hend2).set_handler(hend3).set_handler(hend4)


Client.hend1.handler('Page')


# Идеии по оптимизации 
# 1. В кадом классе повторяеться уловия для запуска слудующего обрбаотчика по цепочки, было бы хорошо это инкапсулировать
# 2. Создания обработчиков было бы хорошо сделать через @property и Кеширования или как то по другому, задумка такая, что
#    создавать обьек обработчки только когда подошла его очерень и не создавать сразу все
# 3. Создания цеочки условий, было бы хорошо сдедалть "Строитель" или как то по другому, что бы выглядело как то по нормальному
#    и можно было задавать удобно цепочки обработки
#
#
#