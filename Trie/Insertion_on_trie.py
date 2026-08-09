'''
There are 4 cases for the insertion of the string in Trie

CASE 1 => A trie is blank

CASE 2 => New string's Prefix is common to another strings Prefix

CASE 3 => New Strings's Prefix is already present as complete String

CASE 4 => String to be inserted is already present in Trie
'''

# -----------------------------------------------------
# Trie Data Structure
# -----------------------------------------------------

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


# -----------------------------------------------------
# Creating Trie
# -----------------------------------------------------

newTrie = Trie()#Creation of Trie
#Time complexity => O(1)
#Space complexity => o(1)



# -----------------------------------------------------
# Inserting Words
# -----------------------------------------------------

newTrie.insertString("APP")
newTrie.insertString("APPLE")
newTrie.insertString("API")
newTrie.insertString("BAT")
#Time-complexity---> o(m) #len of the word
#space-complexity---> o(m)
