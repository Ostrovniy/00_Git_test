"""
Команда - немного запутання структура, как по мне, задумка такая, у нас есть интерфейс команды
в которого есть метод execute это метод выполнения команды, далее мы наследуемся и создаем 
определенную команду где реализуем метод execute. Также есть Invoker который получает 
определенную команду и выполняет ее. Клиент в данной ситуации Создает обьек Получатель
это обьект которым будут манипулировать также создает с помощю Invoker запускат нужные команды
"""

# Получатель (Receiver) — объект, который выполняет действия, связанные с командой.
class Lamp:
    def on(self):
        print('Свет включен')

    def off(self):
        print('Свет выключен')


# Команда (Command) — интерфейс или абстрактный класс, который определяет метод execute, выполняющий команду.
class Command:
    def execute(self):
        pass
    
# Конкретная команда (ConcreteCommand) — реализует метод execute и содержит ссылку на объект-получатель, который выполняет команду.
class CommandOn(Command):
    # Передаем ссылку обьект который будет управляться
    def __init__(self, lamp: Lamp):
        self.lamp = lamp

    def execute(self):
        self.lamp.on()

class CommandOff(Command):
    def __init__(self, lamp: Lamp):
        self.lamp = lamp
    
    def execute(self):
        self.lamp.off()


# Отправитель (Invoker) — объект, который вызывает выполнение команды.
class Invoker:
    @staticmethod
    def done_comand(command: Command):
        command.execute()

# Клиент (Client) — объект, который создает и настраивает команды.
class Client:
    @staticmethod
    def start():
        lamp = Lamp()
        Invoker.done_comand(CommandOn(lamp))
        Invoker.done_comand(CommandOff(lamp))



Client.start()