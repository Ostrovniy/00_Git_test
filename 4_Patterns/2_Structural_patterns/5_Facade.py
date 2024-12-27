"""

Паттерн проектирования "Фасад" помогает упростить доступ к сложной системе, предоставляя унифицированный интерфейс для работы с ней.
Представь, ты заказываешь пиццу. Ты не занимаешься готовкой: не замешиваешь тесто, не готовишь соус и не режешь ингредиенты. 
Вместо этого ты просто звонишь в пиццерию, которая берет на себя все эти задачи.
Фасад — это пиццерия, которая предоставляет тебе простой интерфейс для сложного процесса приготовления пиццы.
"""


class VideoFile:
    def __init__(self, name):
        self.name = name
        print(f"Открытие фидео файда: {self.name}")

class CodecFactory:
    def decode(self):
        print('Декодирования файла...')

class AutoMixer:
    def mixser(self):
        print('Микширования айдио дорожки...')

class ConvertFile:
    def convert(self):
        print('КОнвертация видео формате...')

class SaveFile:
    def save(seld):
        print('Сохранения файла...')

# Это интерфейс для взаимодействия со всеми классами что указаны выше
class MainFacade:
    def __init__(self, name):
        VideoFile(name)
        codec = CodecFactory()
        codec.decode()
        automix = AutoMixer()
        automix.mixser()
        convertfile = ConvertFile()
        convertfile.convert()
        savefiel = SaveFile()
        savefiel.save()

myfacade = MainFacade('video')