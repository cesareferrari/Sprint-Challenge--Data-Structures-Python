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
        # Create a new node
        node = BSTNode(value)

        # if value is more or equal than self.value, go to the right
        if value >= self.value:
            # if there is nothing at the right, insert the new node
            if self.right is None:
                self.right = node 
            else:
                # if there is a right node already, try again recursively
                # until you find None as the right node.
                # At that point, the previous branch is run and the 
                # node is inserted to the right.
                self.right.insert(value)

        # if value is less than current node value, insert to the left.
        # same logic as above
        if value < self.value:
            if self.left is None:
                self.left = node 
            else:
                self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if current node value is the target, return true
        if self.value == target:
            return True

        # if current node value is less than the target
        # target must be on the right
        if self.value < target:
            # if there's nothing on the right, we didn't find the target,
            # return false
            if self.right is None:
                return False
            else:
                # if there's something on the right, keep searching recursively
                # until the value is found, 
                # and returns True (self.value == target see line 48)
                return self.right.contains(target)

        # same code as previous branch, but looking left
        if self.value >= target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # larger values are on the right, so we only look at the right side

        # if there is nothing at the right of the current node,
        # this is the largest value
        if self.right is None:
            return self.value
        else:
            # recursively look at the right until we get to the point
            # where self.right is None
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on the first node
        fn(self.value)

        # if the node has a left node, call the function recursively on left
        # node
        if self.left:
            self.left.for_each(fn)

        # same thing if it has a right node
        if self.right:
            self.right.for_each(fn)


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(self.left)

        print(node.value)

        if self.right is not None:
            self.right.in_order_print(self.right)


if __name__ == "__main__":

    bst = BSTNode(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(2)

    bst.dft_print(bst)
    bst.bft_print(bst)
