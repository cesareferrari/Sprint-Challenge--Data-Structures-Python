class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next_node

    def reverse_list(self, node, prev):
        # my code doesn't quite work
        # if node:
        #     if node.next_node is None:
        #         return node
        #     else:
        #         self.reverse_list(node.next_node, node)
        #         node.next_node = prev

        if node is None:
            return
        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
        else:
            self.reverse_list(node.next_node, node)
            node.next_node = prev



if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add_to_head("a")
    my_list.add_to_head("b")
    my_list.add_to_head("c")
    my_list.add_to_head("d")
    my_list.add_to_head("e")

    my_list.print_list()

    my_list.reverse_list(my_list.head, None)

    my_list.print_list()
