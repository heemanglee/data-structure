class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # 다음 Node를 가리키는 링크

# 단일 연결 리스트
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 삽입 소요 시간: O(1)
    # 각 노드에 포인터가 존재하고, 새로운 노드는 tail 노드의 포인터에 연결하면 됨.
    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # 탐색 소요 시간: O(N)
    # head 노드부터 순차적으로 탐색해야하므로 원하는 요소를 찾는데 걸리는 시간은 O(N)
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next

        return None # 찾고자 하는 요소가 없으면 None 반환

linked_list = SingleLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

find_value = 4
find_node = linked_list.find(find_value)
print(f"{find_value} 값이 LinkedList에 존재하는가? => {find_node != None}")

find_value = 3
find_node = linked_list.find(find_value)
print(f"{find_value} 값이 LinkedList에 존재하는가? => {find_node != None}")



