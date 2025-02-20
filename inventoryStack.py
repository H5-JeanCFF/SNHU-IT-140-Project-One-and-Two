# Jean Carlos Farfan Fallu
# 02/23/2025

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None # points to another Node or None

class LinkedStack:
    def __init__(self, capacity=3):
        self.top = None # The topmost node of the stack
        self.size = 0 # How many items currently
        self.capacity = capacity

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.size >= self.capacity

    # Push a new item onto the top of the stack, if not full, and returns True if success, False if the stack is full
    def push(self, item):

        if self.is_full():
            return False

        new_node = StackNode(item)
        # new node's next points to the current top
        new_node.next = self.top
        # update the top pointer
        self.top = new_node
        self.size += 1
        return True

    # Return (without removing) the top item. Returns None if empty.
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    # Return a list of all items from top to bottom.
    def get_items(self):
        items = []
        current = self.top
        while current is not None:
            items.append(current.data)
            current = current.next
        return items
