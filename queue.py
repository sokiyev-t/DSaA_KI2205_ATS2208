class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_head = Node(val)

        new_head.set_next(self.head)

        if self.head is not None:
            self.head.set_prev(new_head)

        self.head = new_head
        if self.tail is None:
            self.tail=self.head

    def pop(self):
        if not self.is_empty():
            data = self.tail.get_data()
            self.tail=self.tail.get_prev()
            return data
        return None

    def is_empty(self):
        return self.tail is None


s = Queue()
s.push(2)
s.push(5)
s.push(15)
print("Start of programm: ")
while not s.is_empty():
    v = s.pop()
    print(v)
