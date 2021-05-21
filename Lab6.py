class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node  # set parent
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None: return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        if node is None or self.find(node.value) is None:
            print("Node to be deleted not found in the tree!")
            return None

        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0
            if n.left_child is not None: num_children += 1
            if n.right_child is not None: num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)

        if node_children == 0:

            if node_parent is not None:
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        if node_children == 1:

            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent is not None:
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right_child)

            node.value = successor.value

            self.delete_node(successor)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)
        return False

    def treeToArr(self):
        nodes = []
        if self.root is not None:
            self._treeToArr(self.root, nodes)

        return nodes

    def _treeToArr(self, cur_node, nodes):
        if cur_node is not None:
            self._treeToArr(cur_node.left_child, nodes)
            nodes.append(cur_node.value)
            self._treeToArr(cur_node.right_child, nodes)


def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2

    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr[:mid])

    root.right = sortedArrayToBST(arr[mid + 1:])
    return root


def preorder(root):
    if root is None:
        return

    print(root.value, end=' ')
    preorder(root.left)
    preorder(root.right)


tree = BinarySearchTree()
tree.insert(20)
tree.insert(15)
tree.insert(25)
tree.insert(10)
tree.insert(17)
tree.insert(16)
tree.insert(18)
tree.insert(11)
tree.insert(3)
qq = tree.treeToArr()
root = sortedArrayToBST(qq)
preorder(root)
