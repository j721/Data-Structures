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
    def contains(self, target):

        #If tree contains target value, return True
        if self.value == target:
            return True

        # if tree does not contain target value. 
        #value != target
        else: 
           #if target is lower than value
            if target < self.value:
            #if the target value is going to be on the left as a child node
                if not self.left:
                    return False
                if self.left.value == target:
                    return True
                else:
                    self.left.contains(target)
            # if target is >= than the value from the tree(self.value)        
            else:
                #is there any child node on the right?
                if not self.right:
                    return False
                #if the right child node is our target than return True
                if self.right.value == target:
                    return True
                else:
                    self.right.contains(target)

                

    # Return the maximum value found in the tree
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
    def for_each(self, fn):
       #call the function `fn`
       fn(self.value)
        #go to right child nodes if any
       if self.right:
           self.right.for_each(fn)
       #go to the left child nodes if any
       if self.left:
           self.left.for_each(fn)
    
        
        
       

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
