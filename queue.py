class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class Queue:
    def __init__(self, head=None):
        self.head = head
        self.tail=None

    def push(self, val):
        new_head = Node(val)
        new_head.set_next(self.head)
        self.head = new_head
        # self.count+=1

    def pop(self):
        if not self.is_empty():
            data = self.head.get_data()
            self.head = self.head.get_next()
            return data
        return None

        # if self.count>0:
        #     data=self.head.get_data()
        #     self.head=self.head.get_next()
        #     self.count-=1
        #     return data
        # return None

    def is_empty(self):
        return self.head is None


s = Queue()
s.push(2)
s.push(5)
s.push(15)
print("Start of programm: ")
while not s.is_empty():
    v = s.pop()
    print(v)
