class Node:
    def __init__(self, data:str):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self, root):
        self.root = root


    def print_binary_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._recursive_print(self.root, level=0)


    def _recursive_print(self, node, level):
        if node is not None:
            self._recursive_print(node.right, level + 1)
            print("   " * level + f"- {node.data}")
            self._recursive_print(node.left, level + 1)

#creation of nodes
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")

#building the tree
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

#printing the tree, I was not able to print it horizontally
new_binary_tree = Binary_Tree(node_a)
new_binary_tree.print_binary_tree()

