
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.

3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   An array you simply have to call the push() and pop() methods to add a new element onto the array.
   Whereas, a linked list we have to change the tail reference from previous last element in 
   the list, to our newly added element that will 
   become the new tail end of the list, to correctly add/delete the last element in our linked list. 


"""

#array as underlying storage structure 

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size +=1
#         return self.storage.append(value)

#     def pop(self):
#         if self.size !=0:
#             self.size -= 1
#             return self.storage.pop()



#Linked list as underlying storage structure 

from singly_linked_list import LinkedList
from singly_linked_list import Node
# import sys
# sys.path.append('../singly_linked_list')
# from singly_linked_list import singly_linked_list

class Stack():
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size +=1
        return self.storage.add_to_tail(value)

    # def pop(self):
    #     if self.size !=0:
    #         self.size -=1
    #         return self.storage.remove_tail()

    #2nd pop method works
    def pop(self):
            if self.size == 0:
                return None
            else:
                self.size -= 1
                return self.storage.remove_tail()