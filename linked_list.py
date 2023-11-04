import sys


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


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        # self.count = 0

    def insert(self, data):
        """
        Create a new node at the Head of the Linked List
        """
        # create a new node to hold the data
        new_node = Node(data)

        # set the next of the new node to the current head
        new_node.set_next(self.head)

        # set the head of the Linked List to the new head
        self.head = new_node

        # add 1 to the count
        # self.count += 1

    def find(self, val):
        """
        Search for item in Linked List with data = val

        Time complexity is O(n) as in worst case scenario
        have to iterate over whole Linked List
        """
        # start with the first item in the Linked List
        item = self.head
        # then iterate over the next nodes
        # but if item = None then end search
        while item != None:

            # if the data in item matched val
            # then return item
            if item.get_data() == val:
                return item

            # otherwise we get the next item in the list
            else:
                item = item.get_next()

        # if while loop breaks with None then nothing found
        # so we return None
        return None

    def remove(self, item):
        """
        Remove Node with value equal to item
        Time complexity is O(n) as in the worst case we have to
        iterate over the whole linked list
        """

        # set the current node starting with the head
        current = self.head
        # create a previous node to hold the one before
        # the node we want to remove
        previous = None

        # while current is note None then we can search for it
        while current is not None:
            # if current equals to item then we can break
            if current.data == item:
                break
            # otherwise we set previous to current and
            # current to the next item in list
            previous = current
            current = current.get_next()

        # if the current is None then item, not in the list
        if current is None:
            raise ValueError(f"{item} is not in the list")
        # if previous None then the item is at the head
        if previous is None:
            self.head = current.next
            # self.count -= 1
        # otherwise then we remove that node from the list
        else:
            previous.set_next(current.get_next())
            # self.count -= 1

    def get_count(self):
        count = 0
        h = self.head
        while h:
            h = h.get_next()
            print(f"Finding count: {count}")
            count += 1
        return count

        """
        Return the length of the Linked List
        Time complexity O(1) as only returning a single value
        """
        # return self.count

    def is_empty(self):
        """
        Returns whether the Linked List is empty or not
        Time complexity O(1) as only returns True or False
        """
        # we only have to check the head if is None or not
        return self.head == None


l = LinkedList()
l.insert(12)
l.insert(23)
l.insert(45)
v = l.head.get_next().get_next().get_data()
c = l.get_count()
s = sys.getsizeof(l)

print(f"Size of list is {s} count is: {c} value of header: {v}")
