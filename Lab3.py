class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
        self.nref = None
        self.pref = None


class LinkedList:
    def __init__(self):
        self.start = None

    def traverse_list(self):
        if self.start is None:
            print("List has no element")
            return
        else:
            n = self.start
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_start(self, data):
        node = Node(data)
        node.ref = self.start
        self.start = node

    def insert_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        n = self.start
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_after(self, x, data):
        n = self.start
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_start(self):
        if self.start is None:
            print("The list has no element to delete")
            return
        self.start = self.start.ref

    def delete_end(self):
        if self.start is None:
            print("The list has no element to delete")
            return

        n = self.start
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_by_value(self, x):
        if self.start is None:
            print("The list has no element to delete")
            return

        # Deleting first node
        if self.start.item == x:
            self.start = self.start.ref
            return

        n = self.start
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref


class DoublyLinkedList:
    def __init__(self):
        self.start_prev = None
        self.start = None

    def insert_in_emptylist(self, data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
        else:
            print("list is not empty")

    def insert_start(self, data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start
        self.start.pref = new_node
        self.start = new_node

    def insert_end(self, data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
            return
        n = self.start
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after(self, x, data):
        if self.start is None:
            print("List is empty")
            return
        else:
            n = self.start
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def traverse_list(self):
        if self.start is None:
            print("List has no element")
            return
        else:
            n = self.start
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def delete_start(self):
        if self.start is None:
            print("The list has no element to delete")
            return
        if self.start.nref is None:
            self.start = None
            return
        self.start = self.start.nref

    def delete_end(self):
        if self.start is None:
            print("The list has no element to delete")
            return
        if self.start.nref is None:
            self.start = None
            return
        n = self.start
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_by_value(self, x):
        if self.start is None:
            print("The list has no element to delete")
            return
        if self.start.nref is None:
            if self.start.item == x:
                self.start = None
            else:
                print("Item not found")
            return

        if self.start.item == x:
            self.start = self.start.nref
            self.start.pref = None
            return

        n = self.start
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")


print('========= LinkedList =========')
print(' ')
linked_list = LinkedList()

linked_list.insert_start(10)
linked_list.insert_end(20)
linked_list.insert_end(30)

linked_list.insert_start(21)
linked_list.insert_after(21, 69)

linked_list.delete_start()
linked_list.delete_end()
linked_list.delete_by_value(20)

linked_list.traverse_list()

print(' ')
print('========= DoubleLinkedList =========')
print(' ')
d_linked_list = DoublyLinkedList()

d_linked_list.insert_in_emptylist(10)
d_linked_list.insert_end(20)
d_linked_list.insert_end(30)

d_linked_list.insert_start(21)
d_linked_list.insert_after(21, 69)

d_linked_list.delete_start()
d_linked_list.delete_end()

d_linked_list.delete_by_value(20)

d_linked_list.traverse_list()
