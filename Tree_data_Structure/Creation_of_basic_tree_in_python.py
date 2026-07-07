#Creation of the basic tree in python
#Using python list

class TreeNode:
    def __init__(self, data, children):
        self.data = data
        self.children = children

    #Str method to print the tree
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    #Decalring a addCHild method
    def addChild(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode("Drinks", []) #making the children empty
cold = TreeNode("Colddrinks", [])
hot = TreeNode("tree", [])

tree.addChild(cold)
tree.addChild(hot)
print(tree)

