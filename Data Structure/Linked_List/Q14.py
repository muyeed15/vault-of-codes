"""
Question:14. Write a function named countDuplicates that accepts an object to a
ListNode representing the front of a linked list. Your function should return the
number of duplicates in a sorted list. Your code should assume that the list's
elements will be in sorted order, so that all duplicates will be grouped together.
For example, if a variable named front points to the front of the following sequence
of values, the call of countDuplicates(front) should return 7 because there are 2
duplicates of 1, 1 duplicate of 3, 1 duplicate of 15, 2 duplicates of 23 and 1
duplicate of 40: {1, 1, 1, 3, 3, 6, 9, 15, 15, 23, 23, 23, 40, 40}
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


def duplicate(front, data):
    count = 0
    while front is not None:
        if front.data == data:
            count += 1
        front = front.next
    
    return count


def countDuplicate(front):
    count = 0
    current = front
    while current is not None:
        number = duplicate(front, current.data)
        if number > 1:
            for i in range(number - 1):
                front = remNode(front, current.data)
                count += 1

        current = current.next

    return count


p = None
p = addNode(p, 1)
p = addNode(p, 1)
p = addNode(p, 1)
p = addNode(p, 3)
p = addNode(p, 3)
p = addNode(p, 6)
p = addNode(p, 9)
p = addNode(p, 15)
p = addNode(p, 15)
p = addNode(p, 23)
p = addNode(p, 23)
p = addNode(p, 23)
p = addNode(p, 40)
p = addNode(p, 40)
printList(p)
print(countDuplicate(p))
