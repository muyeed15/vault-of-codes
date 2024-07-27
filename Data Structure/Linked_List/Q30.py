"""
Question:30.Write a function named removeAllThreshold that accepts three parameters:
a reference to an object of a ListNodeDouble representing the front of a linked list
of real numbers, a real number value to remove, and a tolerance threshold. Your
function should remove all values from the list that are within +/- threshold of the
given value to remove. You must preserve the original order of the remaining
elements of the list. For example, if a variable named front points to the front of
a list containing the following values: {3.0, 9.0, 4.2, 2.1, 3.3, 2.3, 3.4, 4.0,
2.9, 2.7, 3.1, 18.2}
Then the call of removeAllThreshold(front, 3.0, 0.3); would remove all values that
are between 2.7 and 3.3 inclusive from the list, yielding the following values:
{9.0, 4.2, 2.1, 2.3, 3.4, 4.0, 18.2}
You may assume that the tolerance threshold passed is non-negative.
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


def removeAllThreshold(front, value, threshold):
    start = value - threshold
    end = value + threshold

    current = front
    while current is not None:
        if start <= current.data <= end:
            front = remNode(front, current.data)
        current = current.next

    return front


p = None
p = addNode(p, 3.0)
p = addNode(p, 9.0)
p = addNode(p, 4.2)
p = addNode(p, 2.1)
p = addNode(p, 3.3)
p = addNode(p, 2.3)
p = addNode(p, 3.4)
p = addNode(p, 4.0)
p = addNode(p, 2.9)
p = addNode(p, 2.7)
p = addNode(p, 3.1)
p = addNode(p, 18.2)
printList(p)
p = removeAllThreshold(p, 3.0, 0.3)
printList(p)
