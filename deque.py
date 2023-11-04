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


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, val):
        new_head = Node(val)
        new_head.set_next(self.head)
        if self.head is not None:
            self.head.set_prev(new_head)
        self.head = new_head
        if self.tail is None:
            self.tail=self.head

    def pop_front(self):
        if not self.is_empty():
            data = self.tail.get_data()
            self.tail=self.tail.get_prev()
            if self.tail is not None:
                self.tail.set_next(None)
            return data
        return None

    def push_back(self, val):
        new_tail = Node(val)
        new_tail.set_prev(self.tail)

        if self.tail is not None:
            self.tail.set_next(new_tail)

        self.tail = new_tail
        if self.head is None:
            self.head = self.tail

    def pop_back(self):
        if not self.is_empty():
            data = self.head.get_data()
            self.head = self.head.get_next()
            if self.head is not None:
                self.head.set_prev(None)
            return data
        return None

    def is_empty(self):
        return self.tail is None or self.head is None

print("Test push front: ")
s = Deque()
s.push_front(2)
s.push_front(5)
s.push_front(15)
while not s.is_empty():
    v = s.pop_front()
    print(v)

print("Test push back: ")
s = Deque()
s.push_back(2)
s.push_back(5)
s.push_back(15)

while not s.is_empty():
    v = s.pop_back()
    print(v)