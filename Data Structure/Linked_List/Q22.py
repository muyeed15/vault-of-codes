"""
Question:22.Write a member function named isSorted that accepts an object to a
ListNode representing the front of a linked list. Your function should return true
if the list is in sorted (non-decreasing) order and false otherwise. An empty list
is considered to be sorted.
"""

class ListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def addNode(front, data):
    newNode = ListNode(data)

    if front is None:
        return newNode
    
    current = front
    while current.next is not None:
        current = current.next

    current.next = newNode
    
    return front


def remNode(front, data):
    if front is None:
        return
    
    if front.data == data:
        front = front.next
    else:
        current = front
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return front
            
            current = current.next
        
    return front


def printList(front):
    if front is None:
        print("Empty List!")
        return
    
    print("front", end=" --> ")
    while front is not None:
        if front.next is not None:
            print(front.data, end= " --> ")
        else:
            print(front.data, end="\n")

        front = front.next


def isSorted(front):
    while front.next is not None:
        if front.next.data < front.data:
            return False
        
        front = front.next
        
    return True

p = None
p = addNode(p, 1)
p = addNode(p, 2)
p = addNode(p, 3)
p = addNode(p, 4)
p = addNode(p, 5)
printList(p)
print(isSorted(p))
