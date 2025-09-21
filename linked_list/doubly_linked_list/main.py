class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 삽입 소요 시간: O(1)
    # 노드에 next 포인터가 존재하므로 새로운 노드는 tail 노드의 next 포인터에 연결하면 됨.
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    # 삽입 소요 시간: O(1)
    # 노드에 prev 포인터가 존재하므로 새로운 노드는 head 노드의 prev 포인터에 연결하면 됨.
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            old_head.prev = new_node
            new_node.next = old_head
            self.head = new_node
        self.size += 1

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next

        return None

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)

find_value = 0
find_node = linked_list.find(find_value)
print(f"{find_value} 값이 LinkedList에 존재하는가? => {find_node is not None}")

find_value = 4
find_node = linked_list.find(find_value)
print(f"{find_value} 값이 LinkedList에 존재하는가? => {find_node is not None}")