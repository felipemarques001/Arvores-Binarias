class _Node:
    def __init__(self, valor):
        self.value = valor
        self.left = None
        self.right = None

    def __str__(self):
        print(str(self.value))


# AQUI ESTÁ AS FUNÇÕES RECURSIVAAAAAASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

class BinaryTree:
    def __init__(self):
        self.root = None

    def _add(self, perc, value):
        if value >= perc.value:
            if perc.right:
                return self._add(perc.right, value)
            else:
                perc.right = _Node(value)
        else:
            if perc.left:
                return self._add(perc.left, value)
            else:
                perc.left = _Node(value)
        return

    def add(self, value):
        node = _Node(value)
        if self.root is None:
            self.root = node
        else:
            self._add(self.root, value)

    def _find_value(self, perc, value):
        if perc is None:
            raise ValueError('Value not found in the binary tree')

        if perc.value == value:
            return True
        if value < perc.value:
            print('avançou p/ esquerda')
            return self._find_value(perc.left, value)
        else:
            print('avançou p/ direita')
            return self._find_value(perc.right, value)

    def find_value(self, value):
        if self.root.value == value:
            print('Este valor é a raiz da árvore')
            return True
        else:
            result = self._find_value(self.root, value)
            return result


tree = BinaryTree()
tree.add(10)
tree.add(20)
tree.add(30)
tree.add(40)
tree.add(9)
tree.add(7)
tree.add(25)
tree.add(8)
print(tree.find_value(8))

