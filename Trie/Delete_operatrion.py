# Trie Node
class TrieNode:

    def __init__(self):
        # Stores child characters and their TrieNode
        self.children = {}

        # True if a complete word ends at this node
        self.endOfString = False


# -----------------------------------------------------
# Trie
# -----------------------------------------------------

class Trie:

    def __init__(self):
        # Every Trie starts with an empty root node
        self.root = TrieNode()

    # -------------------------------------------------
    # Insert String into Trie
    # -------------------------------------------------

    def insertString(self, word):

        # Start traversal from the root
        current = self.root

        # Traverse every character of the word
        for ch in word:

            # Check if character already exists
            node = current.children.get(ch)

            # If character does not exist,
            # create a new TrieNode
            if node is None:
                node = TrieNode()

                # Add character -> TrieNode
                current.children[ch] = node

            # Move current pointer to the child node
            current = node

        # Mark the last character as the end of a word
        current.endOfString = True

        print("Successfully Inserted")

    # Search for string method
    def search(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False

    # Time-complexity => o(m)
    # Space-complexity => o(1)

    '''
    Deletion have 4 cases
    #########===> Deletion in a trie always start from the leaf node and goes to the parent node 
    Case1 - Some other prefix of string is same as the one that we want to delete.
    Case2 - The string is a prefix of another string.
    Case3 - Other string is a prefix of this string.
    Case4 - Not any node depends on this String
    '''

#delete method
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1) #recursively
        return False
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    #last condition
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False






# -----------------------------------------------------
# Creating Trie
# -----------------------------------------------------

newTrie = Trie()  # Creation of Trie
# Time complexity => O(1)
# Space complexity => o(1)