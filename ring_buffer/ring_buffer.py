from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # use linked list as storage
        self.storage = DoublyLinkedList()
        self.size = 0
        self.oldest = None

    # add the given element to the buffer
    def append(self, item):
        # when buffer is less than capacity
        if self.size < self.capacity:
            # add to the tail
            self.storage.add_to_tail(item)
            # oldest item is always the head when buffer < capacity
            self.oldest = self.storage.head
            # increment the size
            self.size += 1

        # when buffer reaches capacity
        elif self.size == self.capacity:
            # overwrite the oldest item with the new item
            self.oldest.value = item

            # set the oldest item to the following one if there is one,
            # if there is no next item, we are at the tail
            # so we set the oldest item back to the head
            if self.oldest.next:
                self.oldest = self.oldest.next
            else:
                self.oldest = self.storage.head


    def get(self):
        # initialize list
        elements = []

        # start at the head
        node = self.storage.head

        # append all nodes to the list
        while node is not None:
            elements.append(node.value)
            node = node.next

        return elements


if __name__ == '__main__':

    buffer3 = RingBuffer(3)
    print("Capacity:", buffer3.capacity)
    print(buffer3.get())

    buffer3.append('a')
    print(buffer3.get())
    print("oldest:", buffer3.oldest.value)

    buffer3.append('b')
    print(buffer3.get())
    print("oldest:", buffer3.oldest.value)

    buffer3.append('c')
    print(buffer3.get())
    print("oldest:", buffer3.oldest.value)

    buffer3.append('d')
    print(buffer3.get())
    print("oldest:", buffer3.oldest.value)

    buffer3.append('e')
    print(buffer3.get())
    print("oldest:", buffer3.oldest.value)

    buffer3.append('f')
    print(buffer3.get())
    print("oldest:", buffer3.oldest.value)

    buffer3.append('g')
    print(buffer3.get())
    print("oldest:", buffer3.oldest.value)

    print("dll now contains:")
    buffer3.storage.print_nodes()

