"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # #1. check if there is no root,
        #     # we can check this by checking if self is None
        # if self is None:
        #     #if there isn't, create the node and park it there
        #     self = BSTNode(value)
        # #2. Otherwise, there is a root
        # else:
            #compare the value to the root's value to determine which direction
            #we're gonna go in
            #if the value < root's value
        if value < self.value:
            #go left
            #how do we go left
            #we have to check if there is another node on the left side
            if self.left:
                #then self.left is a Node
                #moved the root from (self.left )and the .insert(value)- adds new value from the new root (self.left)
                self.left.insert(value)
            else:
                #then we can park the value here
                self.left = BSTNode(value)
        #else te value >= root's value
        else:
            #go right 
            #how do we go right
            #we have to check if there is another node on the right side
            if self.right:
                #then self.right is a Node
                self.right.insert(value)
            else:
                    #then we can park the value here
                self.right = BSTNode(value)



    # Return True if the tree contains the value
    # False if it does not
    # def contains(self, target):

    #     #If tree contains target value, return True
    #     if self.value == target:
    #         return True

    #     # figure out which direction we need to go 
    #     else: 
    #        #if target is lower than value
    #         if target < self.value:
    #         #if the target value is going to be on the left as a child node
    #             if not self.left:
    #                 return False
    #             if self.left.value == target:
    #                 return True
    #             else:
    #                 self.left.contains(target)
    #         # if target is >= than the value from the tree(self.value)        
    #         else:
    #             #is there any child node on the right?
    #             if not self.right:
    #                 return False
    #             #if the right child node is our target than return True
    #             if self.right.value == target:
    #                 return True
    #             else:
    #                 self.right.contains(target)

    def contains(self, target):
        #base case?
        #we find the target in the tree node
        if self.value == target:
            return True
        #figure out which direction we need to go in
        if target < self.value:
            #we go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        #or, we get a spot where the node should be, but nothing is there
        else: 
            #we go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        #how do we move towards the base case?
                

    # Return the maximum value found in the tree
    #used recursion - function that calls itself
    #run time O (log n)
    def get_max(self):
        #check to the right side of the tree
        #since left (self.left.value) side of the tree will always be smaller than the root

        #if the right side of the tree is empty that just return the tree
        if not self.right:
            return self.value
        #if right side of the tree is not empty. Then get the right child node with the max value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node

    #example of a tree traversal. Want to traverse through every tree node
    #recursion
    #doesn't actually return anything 
    def for_each(self, fn):
       #call the function `fn` on self.value
       fn(self.value)
        #go to right child nodes if any exists
       if self.right:
           self.right.for_each(fn)
       #go to the left child nodes if any exists
       if self.left:
           self.left.for_each(fn)
    
    def iter_depth_first_for_each(self,fn):
        #with depth-first traversal, there's a certain order to when we visit nodes
        #what's that order? LIFO
        #use a stack to get that order
        #initialize a stack to keep track of the nodes we visited
        stack = []
        #add the first node (root) to our stack
        stack.append(self)
        #continue traversing until our stack is empty
        while len(stack) > 0:
            #pop off the stack
            current_node = stack.pop()
            #add its children to the stack
            #add the right first and left child second
            # to ensure that left is popped off the stack first
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            #call the fn function on self.value
            fn(self.value)

    def breadth_first_for_each(self,fn):
         #breadth first traversal follows FIFO ordering of its nodes
         #init a deque
         q = deque()
          # add first node to our q  
         q.append(self)

         while len(q) > 0:
             current_node = q.popleft()
             if current_node.left:
                 q.append(current_node.left)
             if current_node.right:
                q.append(current_node.right)
                fn(self.value)
    
        


    from collections import deque   

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    #uses a queue
    def bft_print(self, node):
        #init a queue
        queue = self.deque()
        #add first node to our queue
        queue.append(node)
        #breadth first traversal, working by layers
        #if queue is not empty
        while len(queue) > 0:
            current_node = queue.popleft()
            print(current_node.value) 
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []

        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)
        # print (node.value)
        # if node.left:
        #     node.left.dft_print(node.left)
        # if node.right:
        #     node.right.dft_print(node.right)
    
    

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # print(node.value)
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)