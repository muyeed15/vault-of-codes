"""
Question:29.Write a function named removeAll that accepts two parameters: a
reference to an object of a ListNode representing the front of a linked list, and an
integer value. Your function should remove all occurrences of that value from the
list. You must preserve the original order of the remaining elements of the list.
For example, if a variable named front points to the front of a list containing the
following values: {3, 9, 4, 2, 3, 8, 17, 4, 3, 18}
Then the call of removeAll(front, 3); would remove all occurrences of the value 3
from the list, yielding the following values: {9, 4, 2, 8, 17, 4, 18}
"""

class ListNodeDouble:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def addNode(front, data):
    newNode = ListNodeDouble(data)

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


def duplicate(front, data):
    count = 0

    while front is not None:
        if front.data == data:
            count += 1
        front = front.next

    return count


def removeAll(front, data):
    for i in range(duplicate(front, data)):
        front = remNode(front, data)

    return front


p = None
p = addNode(p, 3)
p = addNode(p, 9)
p = addNode(p, 4)
p = addNode(p, 2)
p = addNode(p, 3)
p = addNode(p, 8)
p = addNode(p, 17)
p = addNode(p, 4)
p = addNode(p, 3)
p = addNode(p, 18)
printList(p)
p = removeAll(p, 3)
printList(p)
