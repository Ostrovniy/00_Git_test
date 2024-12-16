"""
Компоновщик - используеться когда нужно рабоать с иерахической структорой данных
как с одном обьектом

Идея компоновщика, представьте что есть дерево, которое состоит из
узлов и листев. Узлы это слоэные обьекты которые содержат другие обьекты 
листя это простые обьект которые не содержать дальнейшых узлов, как конечная точка
Компоновщик, позволяет создать такую структура 

https://www.youtube.com/watch?v=EWDmWbJ4wRA&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=14

"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Интерфейс
class HTMLElement(ABC):
    @abstractmethod
    def render(self, index: int = 0) -> str:
        pass

class HTMLTeg(HTMLElement):
    def __init__(self, teg_name, content, attr: dict = {}):
        self.teg_name = teg_name
        self.content = content
        self.attr = attr

    def render(self, index = 0):
        space = ' ' * index
        if self.attr:
            text_attr = ''
            for key, value in self.attr.items():
                text_attr += f'{key}="{value}" '
            return f'{space}<{self.teg_name} {text_attr}>{self.content}</{self.teg_name}>\n'
        return f'{space}<{self.teg_name}>{self.content}</{self.teg_name}>\n'

class HTMLContainer(HTMLElement):
    def __init__(self, tag_name, attr: dict = {}):
        self.tag_name = tag_name
        self.attr = attr
        self.children = []

    def add(self, teg: HTMLElement):
        self.children.append(teg)

    def render(self, index = 0):
        space = ' ' * index
        if self.attr:
            text_attr = ''
            for key, value in self.attr.items():
                text_attr += f'{key}="{value}" '

            html = f'{space}<{self.tag_name} {text_attr}>\n'
            for teg in self.children:
                html += teg.render(index + 2)
            html += f'{space}</{self.tag_name}>\n'

            return html

        html = f'{space}<{self.tag_name}>\n'
        for teg in self.children:
            html += teg.render(index + 2)
        html += f'{space}</{self.tag_name}>\n'

        return html



htmlmain = HTMLContainer('html')
header = HTMLContainer('heaer')
body = HTMLContainer('body')

htmlmain.add(header)
htmlmain.add(body)

div1 = HTMLContainer('div', {'class': 'username', 'id': 'indef'})
body.add(div1)

p1 = HTMLTeg('p', 'Добро пожаловать', {'class': 'btn btn-warring'})
p2 = HTMLTeg('p', 'мы все Вас ждали')

div1.add(p1)
div1.add(p2)

res = htmlmain.render()
print(res)

"""
<html>
  <heaer>
  </heaer>
  <body>
    <div>
      <p>Добро пожаловать</p>
      <p>мы все Вас ждали</p>
    </div>
  </body>
</html>
"""

# Второй пример, папки и файлы
class Interface(ABC):
    @abstractmethod
    def get_shema(self, index: int = 0) -> str:
        pass

class File(Interface):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def get_shema(self, index = 0):
        space = ' ' * index
        return f"{space}{self.name}.{self.type}\n"
    
class Folder(Interface):
    def __init__(self, name: str):
        self.name = name
        self.files = []

    def add(self, file_or_folder: Interface):
        self.files.append(file_or_folder)

    def get_shema(self, index = 0):
        space = ' ' * index
        shema = f"{space}{self.name}\n"
        for i in self.files:
            i:Interface
            shema += i.get_shema(index + 2)
        return shema
    
# Создание папок
folder1 = Folder('Проекты')
folder2 = Folder('Фото')
folder3 = Folder('Видео')
folder4 = Folder('Документы')
folder5 = Folder('Прочее')

# Создание файлов
file1 = File('home', 'jpeg')
file2 = File('table', 'png')
file3 = File('worcout', 'mp4')
file4 = File('инструкция', 'doc')
file5 = File('shema', 'shem')

# В папку "Проекты" добавляем все папки и один файл
folder1.add(folder2)
folder1.add(folder3)
folder1.add(folder4)
folder1.add(folder5)
folder1.add(file5)

# В папку "Фото" добавляем два обьекта фото
folder2.add(file1)
folder2.add(file2)

folder3.add(file3)

folder4.add(file4)

folder5.add(file5)

res = folder1.get_shema()
print(res)

"""
Проекты
  Фото
    home.jpeg
    table.png
  Видео
    worcout.mp4
  Документы
    инструкция.doc
  Прочее
    shema.shem
  shema.shem

"""