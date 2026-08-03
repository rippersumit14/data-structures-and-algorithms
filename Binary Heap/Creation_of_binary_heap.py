# -----------------------------------------------------
# Binary Heap
# -----------------------------------------------------

# A Binary Heap is a Complete Binary Tree.

# It is generally implemented using an Array instead of linked nodes.

# Binary Heap is mainly used to implement a Priority Queue.

# There are two types of Binary Heap:
# 1. Min Heap  -> Parent Node <= Child Nodes
# 2. Max Heap  -> Parent Node >= Child Nodes

# Complete Binary Tree:
# Every level is completely filled except the last level.
# The last level is filled from left to right.

# Heap Property:
# Every parent node follows the Min Heap or Max Heap rule.

# Binary Heap does NOT maintain sorted order.
# It only guarantees the heap property.

# Root Node:
# Min Heap -> Smallest element is always at the root.
# Max Heap -> Largest element is always at the root.

# Binary Heap is stored using an Array.

# Array Index Formulas:
# Left Child  = 2 * i + 1
# Right Child = 2 * i + 2
# Parent      = (i - 1) // 2

# Common Operations:
# Insert
# Peek (Get Root)
# Extract Root (Delete Root)
# Heapify Up
# Heapify Down
# Build Heap

# Time Complexities:
# Insert        -> O(log n)
# Delete Root   -> O(log n)
# Peek          -> O(1)
# Heapify       -> O(log n)
# Build Heap    -> O(n)

# Space Complexity:
# O(n)

# Real-World Applications:
# - Priority Queue
# - CPU Scheduling
# - Task Scheduling
# - Dijkstra's Algorithm
# - A* Search Algorithm
# - Top K Elements
# - Kth Largest / Smallest Element
# - Job Scheduling
# - Event Scheduling
# - Network Routing
# - Ride Matching (Uber/Ola)
# - Food Delivery Prioritization
# - Background Job Queues (BullMQ, Redis Queues)

#declaring the heap class
class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1



#peek of the heap-> root node of the Heap
def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1] #1st index value is being returned
    #Time-complexity=>o(1)
    #Space-complexity=>o(1)

#Size of the heap means how many elements are there in the heap
#Returning all the filled cells
def size_of_Binary_heap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize
    #Time-complexity=>o(1)
    #Space-complexity=>o(1)


#Traversal of binary heap
#4 types
#POST ORDER, IN_ORDER, Pre_order and level-wise order

#Level order traversal
def level_order_traversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])
    #time-complexity=>o(n)
    #space-complexity=>o(1)




newBinaryHeap = Heap(5) #Size of 5

#Time complexity-> o(1)
#Space complexity-> o(n)





































