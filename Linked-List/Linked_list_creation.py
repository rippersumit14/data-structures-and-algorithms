#Linked-list elements are not stored at a contiguous memory location
#to create a linked_list we need to define a class with value and pointer

#declaring the node class
class Node:
    def __init__(self, value):
        self.value = value #the value
        self.next = None #the address will be the none

#creating the linkedlist class
class LinkedList:
    def __init__(self, value):
        new_node = Node(value) #creating new node
        self.head = new_node
        self.tail = new_node
        self.length = 1 #one element is there in the Linked Lists

new_linked_list = LinkedList(10)
print(new_linked_list)#location at the memory
print(new_linked_list.head.value) #new node's value of the head
print(new_linked_list.tail.value)#new node's value of the tail

#the time complexity of this code o(1)
#the space complexity of this code o(1)





