class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

class Linkedlist:

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def get(self):
        current = self.tail
        while current:
            val = current
            current = current.next
            yield val

    def push(self,after,data):
        node = Node(data)
        after = [x for x in self.get() if x.data == after]
        node.next = after[0].next
        after[0].next = node
        self.size += 1

    def begin(self,data):
        node = Node(data)
        node.next = self.tail
        self.tail = node
        self.size += 1

    def delete(self, key):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == key:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                    current = None
                self.size -= 1
                return
            prev = current
            current = current.next

node1 = Linkedlist()
node1.append("party1")
node1.append("party2")
node1.append("party3")
node1.append("party4")
node1.push("party3","party5")
node1.begin("partyx")
node1.delete("partyx")
node1.delete("party1")
print(node1.size)
[print(x) for x in node1.get()]
