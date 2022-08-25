class _Node:
    def __init__(self, valor):
        self.value = valor
        self.left = None
        self.right = None

    def __str__(self):
        print(str(self.value))


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = _Node(value)
        if self.root is None:
            self.root = node
        else:
            perc = self.root
            while True:
                if value < perc.value:
                    if perc.left:
                        perc = perc.left
                    else:
                        perc.left = node
                        return
                else:
                    if perc.right:
                        perc = perc.right
                    else:
                        perc.right = node
                        return

    def find_value(self, value):
        if self.root.value == value:
            return True
        else:
            perc = self.root
            while perc:
                if perc.value == value:
                    return True
                if value < perc.value:
                    perc = perc.left
                    print('avançou p/ esquerda')
                else:
                    perc = perc.right
                    print('avançou p/ direita')
            raise ValueError('Value not found in the binary tree')


tree = BinaryTree()
tree.add(10)
tree.add(20)
tree.add(30)
tree.add(40)
tree.add(25)
print(tree.find_value(25))
