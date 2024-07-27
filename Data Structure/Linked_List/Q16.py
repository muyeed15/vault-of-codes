"""
Question:16. Write a function named deleteBack that accepts an object to a ListNode
representing the front of a linked list. Your function should delete the last value
(the value at the back of the list) and return the deleted value. If the list is
empty (None), your function should throw a string exception.
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


def deleteBack(front):
    if (front is None) or (front.next is None):
        return

    current = front
    while current.next is not None:
        current.next = None
    
    return front


p = None
p = addNode(p, 1)
p = addNode(p, 2)
printList(p)
p = deleteBack(p)
printList(p)

