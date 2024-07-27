"""
Question:6. Write a function named addBack that accepts reference to an object of a
ListNode representing the front of a linked list, along with an integer value. Your
function should insert the given value into a new node at the end of the list. For
example, suppose a variable named front points to the front of a list containing the
following sequence of values:
{8, 23, 19, 7, 102}
The call of addBack(front, 42); should change the list to store the following:
{8, 23, 19, 7, 102, 42}
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


def addBack(front, value):
    newNode = ListNode(value)

    current = front
    while current.next is not None:
        current = current.next
    
    current.next = newNode

    return front


p = ListNode(8)
p.next = ListNode(23)
p.next.next = ListNode(19)
p.next.next.next = ListNode(7)
p.next.next.next.next = ListNode(102)
printList(p)
p = addBack(p, 42)
printList(p)
