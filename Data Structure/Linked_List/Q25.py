"""
Question:25 Write a function named min that accepts an object of a ListNode
representing the front of a linked list. Your function should return the minimum
value in the linked list of integers. If the list is empty, you should throw a
string exception.
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


def min(front):
    if front is None:
        return
    
    minimum = None
    while front is not None:
        if minimum is None:
            minimum = front.data
        elif minimum > front.data:
            minimum = front.data

        front = front.next

    return minimum


p = None
p = addNode(p, 3)
p = addNode(p, 3)
p = addNode(p, 6)
p = addNode(p, 9)
p = addNode(p, 15)
p = addNode(p, 15)
p = addNode(p, 23)
p = addNode(p, 1)
p = addNode(p, 1)
p = addNode(p, 1)
p = addNode(p, 23)
p = addNode(p, 23)
p = addNode(p, 40)
p = addNode(p, 40)
printList(p)
print(min(p))
        
