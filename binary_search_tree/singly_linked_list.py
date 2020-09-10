class Node:
    """
    Stores two peices of data, the Value, and the pointer to next
    1. The Value
    2. The Next Node

    Methods/Behavior/Operations
    1. Get value
    2. Set value
    3. Get next
    4. Set next
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    """
    Data:
    1. A reference to the head Node
    2. A reference to the tail Node 

    Behavior/Methods
    1. Append (Add a new node to the Node referenced by the Tail)
    2. Prepend (Add a new node and point that Node's next_node at the old Head; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        if self.head.get_next() is None:
            head = self.head

            self.head = None

            self.tail = None

            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        # def search(node):
        #     if node.get_value() == value:
        #         return True
        #     if not node.get_next():
        #         return False
        #     return search(self.head)

        current = self.head

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()

        return False

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()

        current = self.head.get_next()

        while current:

            if current.get_value() > max_value:

                max_value = current.get_value()

            current = current.get_next()

        return max_value