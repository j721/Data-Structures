
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
"""

#array as underlying storage structure 
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size +=1
        return self.storage.append(value)

    def pop(self):
        if self.size !=0:
            self.size -= 1
            return self.storage.pop()



#Linked list as underlying storage structure 

# from singly_linked_list import LinkedList

# import sys
# sys.path.append('../singly_linked_list')
# from singly_linked_list import singly_linked_list

# class Stack():
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?

#     def __len__(self):
#         pass

#     def push(self, value):
#         pass

#     def pop(self):
#         pass
