'''
Input: 0->1->2
Output: 3
Explanation: The list has a total of 3 nodes, thus the length of the list is 3.

Input: 12->5->8->7
Output: 4
Explanation: The list has a total of 4 nodes, thus the length of the list is 4.
'''
from requests import head


#Decalaring the linked list class
#Creating all the classes that are necessary for the questions

#inserting the element in the middle of the linked list or something like that

#defining the node class
class Node:
    def __init__(self, value): #declaring the value and next address
        self.value = value
        self.next = None

#defining the linkedlist class
class LinkedList:
    def __init__(self):
            self.head = None
            self.tail = None
            self.length = 0

            # printing the linked list

    def __str__(self):
        temp = self.head
        result = ""

        while temp:
            result += str(temp.value)

            if temp.next:
                result += " -> "

            temp = temp.next  # IMPORTANT: move to next node

        return result

    #creating for end of the linkedlist
    def append(self, value):
        new_node = Node(value)

        # check if linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    #declaring the new method for the insertion of the element using the insert method
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    #creating the traversal method for the traversal of the linked list
    def traversal(self):
        current = self.head #starts from the head of the linked list which will be the first element
        leny = 0
        while current is not None:
            print(current.value)
            current = current.next
            leny += 1

        return leny

    #Striver question








newlinkedlist = LinkedList()

newlinkedlist.append(1)
newlinkedlist.append(2)
newlinkedlist.append(3)
newlinkedlist.append(4)
newlinkedlist.append(5)
newlinkedlist.append(6)


#traversing the linked list
newlinkedlist.traversal()

newlinkedlist.insert(1,33)

print(newlinkedlist)
print(newlinkedlist.traversal())



#The time complexity for the traversal for the singly linked list will be o(n)
#The space complexity will be o(1)





