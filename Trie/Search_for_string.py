'''
Case 1 => String does not exist in Trie

Case 2 => String does exist in Trie

Case 3 => String is prefix of another string, but does not exist in a trie



'''



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

    #Search for string method
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

    #Time-complexity => o(m)
    #Space-complexity => o(1)





# -----------------------------------------------------
# Creating Trie
# -----------------------------------------------------

newTrie = Trie()#Creation of Trie
#Time complexity => O(1)
#Space complexity => o(1)