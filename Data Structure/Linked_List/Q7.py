"""
Question:7. Write a function named addFront that accepts a reference to an object to
a ListNode representing the front of a linked list, along with an integer value.
Your function should insert the given value into a new node at the front of the
list. For example, suppose a variable named front points to the front of a list
containing the following sequence of values:
{8, 23, 19, 7, 102}
The call of addFront(front, 42); should change the list to store the following:
{42, 8, 23, 19, 7, 102}
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


def addFront(front, value):
    newNode = ListNode(value)
    newNode.next = front
    front = newNode
    return front


p = ListNode(8)
p.next = ListNode(23)
p.next.next = ListNode(19)
p.next.next.next = ListNode(7)
p.next.next.next.next = ListNode(102)
printList(p)
p = addFront(p, 42)
printList(p)
