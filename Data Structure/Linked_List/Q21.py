"""
Question:21.Write a function named isEmpty that accepts an object to a ListNode
representing the front of a linked list. Your function should return true if the
list contains no elements, or false if the list does contain at least one element.
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


def isEmpty(front):
    if front is None:
        return True
    return False

p = None
p = addNode(p, 1)
p = addNode(p, 2)
p = addNode(p, 3)
p = addNode(p, 4)
p = addNode(p, 5)
printList(p)
print(isEmpty(p))
