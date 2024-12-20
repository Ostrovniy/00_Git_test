"""
Легковес - немного непонятный в реализации но задумка понятная, идея слудующая
у нас есть обьект, в обьекте есть определенные поля и может возникнуть такая сиутация когда
некоторые поля повторяються и их можно групировать и второй момент, эти поля занимают много памяти
к примеру текстуры или картиныки

что бы оптимизировать ситуациию, обьект разбиваеться на два, первы хранит ткие параметры как координаты
и прочее, а второй обьек хранить список уникальных полей. Пример есть к примеру летающие корабли
каждый корабль имеет координаты и текстуру, предположым что у кораблей есть определенные типы, начальный
продвинутый и сложный и внешний вид корабля меняеться в зависимости от сложнойти.

мы групируем тяжеллые данные такие как текступы по типам и хранит в каком то списке. а корабли у нас
храняться в другом списке и корабль ссылаеться уже на созданную структура и тамким образом у нас может 
быть 100 кораблей которые будут использовать 10 типов. и мы можем отдельно в оперативную парять 
загрузить 10 типов и при создании 100 кораблей использовать один из 10 типов. 

Все остальное это уже нюансы, добавления новых типов, получения типов и прочее

"""

# легковес
class TypeTree:
    def __init__(self, id, name, color, texture):
        self.id = id
        self.name = name
        self.color = color
        self.texture = texture

    def drow(self):
        return f"Тип: {self.id} ({self.name},{self.color},{self.texture})"


# Список легковесов, для управления
class FactoryTreeType:
    _tree_types = {}

    @staticmethod
    def get_tree_type(id, name, color, texture):
        if id not in FactoryTreeType._tree_types.keys():
            FactoryTreeType._tree_types[id] = TypeTree(id, name, color, texture)

        return FactoryTreeType._tree_types[id]

# Добавляем типы деревьяв, информация для "Легковеса"
# не обязательно, это момент когда мы загружаем типы до создания деревьем
FactoryTreeType.get_tree_type(1, 'Дуб', 'Темный', 'Текстура 1')
FactoryTreeType.get_tree_type(2, 'Темный туб', 'Темный', 'Текстура 2')
FactoryTreeType.get_tree_type(3, 'Сосна', 'Светлая', 'Текстура 3')
FactoryTreeType.get_tree_type(4, 'Береза', 'Светлая', 'Текстура 4')

# дерево с координатами и ссылкйо на тип, которы храниться в FactoryTreeType
class Tree:
    def __init__(self, x, y, typetree: TypeTree):
        self.x = x
        self.y = y
        self.typetree = typetree

    def drow(self):
        text_treetype = self.typetree.drow()
        print(f'Отрисовка: x={self.x} y={self.y} {text_treetype}')


# Испольузем готовые тиып
tree1 = Tree(10, 5, FactoryTreeType.get_tree_type(1, 'Дуб', 'Темный', 'Текстура 1'))
tree2 = Tree(10, 50, FactoryTreeType.get_tree_type(2, 'Темный туб', 'Темный', 'Текстура 2'))
tree4 = Tree(45, 32, FactoryTreeType.get_tree_type(3, 'Сосна', 'Светлая', 'Текстура 3'))
# будет создан новый тип
tree5 = Tree(0, 0, FactoryTreeType.get_tree_type(8, 'Катомное', 'Светлая', 'Текстура 30'))

tree1.drow()
tree2.drow()
tree4.drow()
tree5.drow()
