"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            #have this node's previous point to this node's next
            self.prev.next = self.next
        if self.next:
            #have this node's next point to this node's previous
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #create a new node
        new_node = ListNode(value, None, None)
        #ListNode(value, None,self.head) also works

        #check to see if list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1
    
    

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #check to see if there is no node then,
        if not self.head:
            return None 
        #return none 

        # get node head value
        value = self.head.value
        #if there is 1 node set to None
        if self.head ==self.tail:
            self.head = None
            self.tail = None
        #else if there is more than 1 node
        else:
            self.delete(self.head)
        self.length -=1
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        #new node
        new_node = ListNode(value, None, None)
        #ListNode(value,self.tail,None) also works

        #check to see if doubly linked list is empty
        if not self.tail:
            self.head = new_node
        else:
            #the node already existing on the list, the next reference will point to the new node
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

        #2nd method fixed error in else statement
        # if not self.head and not self.tail:
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     new_node.prev = self.tail
        #     self.tail.next = new_node
        # self.tail = new_node
        # self.length +=1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #if there is no node, then return None
        if not self.tail:
            return None
        value = self.tail.value
        # if there is 1 node then set to None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if there is more than 1 node. Need to have more than more otherwise the list the empty
        else:
            self.delete(self.tail)
        self.length-=1
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #get the node value
        value = node.value
        #have to remove the current node before we can move it to its new position
        self.delete(node)
        self.add_to_head(value)
        
        #2nd method
        # if node.prev == None:
        #     pass
        # elif node.next == None:
        #     node.prev.next = None
        #     self.tail = node.prev
        # else:
        #     node.prev.next = node.next
        #     node.next.prev = node.prev




    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # if node.next == None:
        #     pass
        # elif node.prev ==None:
        #     node.next.prev == None
        #     self.head = node.next
        # else:
        #     node.prev.next= node.next
        #     node.next.prev = node.prev

        # self.tail.next = node
        # node.prev = self.tail
        # node.next = None
        # self.tail = node

        #2nd method
        # if node == self.tail:
        #     return
        # value = node
        # if node == self.head:
        #     self.remove_from_head()
        #     self.add_to_tail(value)
        # else:
        #     node.delete()
        #     self.length -=1
        #     self.add_to_tail(value)


        #3rd method
        #get the node value
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

        #4th method
        # if node is self.head:
        #     return
        # else:
        #     value = node.value
        #     self.delete(node)
        #     self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # if self.length ==1:
        #     self.head = None
        #     self.tail = None
        # elif node.prev == None:
        #     node.next.prev = None
        #     self.head = node.next
        # elif node.next == None:
        #     node.prev.next = None
        #     self.tail = node.prev
        # else:
        #     node.prev.next = node.next
        #     node.next.prev = node.prev
        # self.length -=1
        

        #check is list is empty
        if not self.head:
            return None   
        #if there is 1 node  
        if self.head == self.tail:
            self.head = None
            self.tail = None
        #if node is the head. Set the new head to become the next node in line. After the first head node has been deleted
        if node == self.head:
            self.head = node.next
            node.delete()
        #if node is the tail. Need to set the previous node to become the new tail. After the old tail node has been removed
        if node == self.tail:
            self.tail = node.prev
            node.delete()
        #if node is somewhere in the middle of the list.don't have to re-assign new tail or head    
        else:
            node.delete()
        self.length -=1

        #3rd method
        # if not self.head:
        #     return None
        
        # self.length -=1

        # if self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        
        # if node == self.head:
        #     self.head = node.next
        #     self.head.prev = None

        # if node == self.tail:
        #     self.tail = node.prev
        #     self.tail.next = None
        # else:
        #     node.delete()
      
        
    """Returns the highest value currently in the list"""
    def get_max(self):

        max = 0
        current_node = self.head
        
        #traverse/loop through the entire list
        while current_node is not None:
            if current_node.value > max:
                max = current_node.value
            #update the current node to become the next node in the list
            current_node = current_node.next

        return max

        # max_value = self.head.value
        # current = self.head

        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.next
        # return max_value



