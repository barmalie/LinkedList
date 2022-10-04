class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first !=None:
            current_node  = self.first
            out ='LinkedList [\n' +str(current_node.value) +'\n'
            while current_node.next !=None:
                current_node = current_node.next
                out += str(current_node.value) +'\n'
            return out +']'
        return'LinkedList[]'

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first == None:
            self.last = self.first = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

L = LinkedList()
L.add(1)
add = L.add(2)
L.add(3)
print(L)