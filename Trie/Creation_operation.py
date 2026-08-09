'''
Trie is ds where information is organized in the form of hierarchy

Properties
1. It is typically used to store and search strings in a space and time efficient way
2. Any node in trie can store non-repetitive multiple characters
3. Every node stores link of the next character of the string
4. Every node keeps the track of "end of string"
'''

class TrieNode:
    def __init__(self):
        self.children = {} #Dictionary
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


newTrie = Trie()

#Creation of Trie
#Time complexity => O(1)
#Space complexity => o(1)

