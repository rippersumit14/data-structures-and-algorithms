#Creating the binary Tree using the python list
#Iniatialize empty python list
#First cell empty
#Root node to the second cell

#declaring the bt class
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0 #skip the zero index
        self.maxSize = size

newBT = BinaryTree(0)

#Time complexity -> o(1)
#space complexity -> o(n)

