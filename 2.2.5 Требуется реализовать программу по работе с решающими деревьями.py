class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        l=x[:]
        obj = root
        z = len(x)
        j = 0
        for index , value in enumerate(l):
            if value == 1 and index == j:
                obj = obj.left
                j = obj.indx
            elif value == 0 and obj.indx == j:
                obj = obj.right
                j = obj.indx
            if obj.indx < 0:
                return (obj.value)

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if obj.indx == 0:
            cls.head = obj
        elif left == True:
            node.left = obj
        elif left == False:
            node.right = obj
        return obj




class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, var):
        self.__left = var

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, var):
        self.__right = var


assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree, 'predict'), "в классе DecisionTree должны быть методы add_obj и predict"

assert type(TreeObj.left) == property and type(TreeObj.right) == property, "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

# print(DecisionTree.predict(root, [1, 1, 0]))
assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
# print(DecisionTree.predict(root, [0, 1, 0]))
assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
# print(DecisionTree.predict(root, [0, 1, 1]))
assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"
