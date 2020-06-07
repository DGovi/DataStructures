class Node():

    def __init__(self, name):
        self.name = name

        print("node \"" + self.name + "\" created\n")
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        string = "Node name: " + self.name + "\n"

        if self.parent is None:
            string += "parent: None\n"
        else:
            string += "parent:" + self.parent.name + "\n"

        if self.left is None:
            string += "Left Node: None\n"
        else:
            string += "left Node: " + self.left.name + "\n"

        if self.right is None:
            string += "Roght node: None\n"
        else:
            string += "RightNode: " + self.right.name + "\n"

        return string
        # "Parent:  " + self.parent.name + "\n Left leaf: " + self.left.name + "right tree: " + self.right.name

class BinaryTree():

    def __init__(self, node):
        self.root = node
        print("bin tree created\n")

    def search_node(self, node_name):
        pass


nodeA = Node("people")

bin_tree = BinaryTree(nodeA)
nodeA.right = Node("sausage")
print(nodeA)
