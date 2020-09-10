"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_previous(self):
        return self.prev

    def set_previous(self, new_prev):
        self.prev = new_prev

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        elif((self.head != None) and (self.tail == None)):
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
            self.tail = next_node
            self.tail.prev = self.head
            self.length = self.length + 1
        else:
            node_after_next = self.head.next
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
            next_node.prev = self.head
            next_node.next = node_after_next
            self.length = self.length + 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if(self.head == None):
            return None
        elif(self.head.get_next() == None):
            head = self.head

            self.head = None
            self.tail = None

            self.length = 0

            return head.get_value()
        else:
            # (34) <--> (54) <--> (4) -> None
            new_head = self.head.next
            head = self.head
            self.head = new_head
            self.length = self.length - 1

            return head.get_value()



            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # (34) <--> (54) <--> (4) <--> (99) -> None
        new_node = ListNode(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.length = self.length + 1
        else:
            
            new_tail_prev = self.tail

            self.tail.next = new_node # (99)

            self.tail = new_node

            self.tail.prev = new_tail_prev
            
            self.length = self.length + 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # (34) <--> (54) <--> (4) <--> (99) -> None
        if(self.head == None):
            return None
        if(self.head == self.tail):
            value = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return value.get_value()
        else:
            value = self.tail
            new_tail = self.tail.prev
            
            self.tail = new_tail
            self.tail.next = None
            self.length = self.length - 1
            return value
            

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # (34) <--> (54) <--> (4) <--> (99) -> None
        if(self.head == None):
            return None
        elif(node == self.head):
            return f"The node is already {self.head}"
            
        elif(self.head == self.tail):
            print("???")
            return self.head.get_value()

        current = self.head
        
        while(current):

            if current.get_value() == node.value:
                
                if(current.next):
                    current.next.prev = current.prev
                if(current.prev):
                    current.prev.next = current.next
                self.length = self.length - 1
                self.add_to_head(current.get_value())
                return current.value
            else:
                current = current.get_next()


        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
            # (34) <--> (54) <--> (4) <--> (99) -> None
        if(self.head == None):
            return None
        elif((node.value == self.head.get_value()) and (node.value != self.tail.get_value())):
            temp = self.tail
            self.tail = self.head
            self.head = temp
            self.head.next = self.tail
            self.tail.prev = self.head
            return "tail and head swapped"
        current = self.head
        
        while(current):

            if current.get_value() == node.value:
                if(current.next):
                    current.next.prev = current.prev
                if(current.prev):
                    current.prev.next = current.next
                self.length = self.length - 1
                self.add_to_tail(current.get_value())

                return current.value
            else:
                current = current.get_next()

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return

        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        elif self.head == node:
            self.head = node.next
            node.delete()

        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_val:
                max_val = current_node.value

            current_node = current_node.next
        
        return max_val