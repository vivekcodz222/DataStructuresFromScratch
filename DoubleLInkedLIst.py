class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLinkList:
    def __init__(self):
        self.head = None

    def atBeginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def atEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        if current.next is not None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    # def insertAtPrev(self, data, index):
    #     new_node = Node(data)
    #     if index == 0:
    #         new_node.next = self.head
    #         self.head.prev = new_node
    #         self.head = new_node
    #     else:
    #         current = self.head
    #         for i in range(index):
    #             if current is None:
    #                 raise IndexError("Index out of range")
    #             current = current.next
    #         new_node.prev = current.prev
    #         new_node.next = current
    #         current.prev.next = new_node
    #         current.prev = new_node
    #
    # def insertAtNext(self, data, index):
    #     new_node = Node(data)
    #     if index == 0:
    #         if self.head:
    #             new_node.next = self.head.next
    #             self.head.next = new_node
    #             new_node.prev = self.head
    #             if new_node.next:
    #                 new_node.next.prev = new_node
    #         else:
    #             self.head = new_node
    #     else:
    #         current = self.head
    #         for i in range(index):
    #             if current is None:
    #                 raise IndexError("Index out of range")
    #             current = current.next
    #         new_node.prev = current
    #         new_node.next = current.next
    #         if current.next:
    #             current.next.prev = new_node
    #         current.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

list = DLinkList()
list.atEnd(54)
list.atEnd(64)
list.atEnd(74)
list.atBeginning(23)
list.printList()