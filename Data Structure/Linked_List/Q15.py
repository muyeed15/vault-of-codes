"""
Question:15. Write a function named countDuplicateStrings that accepts an object to
a ListNodeString representing the front of a linked list of strings. Your function
should return the number of duplicates in a sorted list, case-insensitively. Your
code should assume that the list's elements will be in case-insensitive sorted
order, so that all duplicates will be grouped together. For example, if a variable
named front points to the front of the following sequence of values, the call of
countDuplicateStrings(front) should return 7 because there are 2 duplicates of
"apple", 1 duplicate of "bat", 1 duplicate of "car", 2 duplicates of "dog" and
1 duplicates of "fox".
{"apple", "apple", "Apple", "bat", "Bat", "car", "car", "dog", "dog", "dog", "fox",
"fox"}
"""

class ListNodeString:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def addNode(front, data):
    newNode = ListNodeString(data)

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
        if (front.data).lower() == (data).lower():
            count += 1
        front = front.next
    
    return count


def countDuplicateStrings(front):
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
p = addNode(p, "apple")
p = addNode(p, "apple")
p = addNode(p, "Apple")
p = addNode(p, "bat")
p = addNode(p, "Bat")
p = addNode(p, "car")
p = addNode(p, "car")
p = addNode(p, "dog")
p = addNode(p, "dog")
p = addNode(p, "dog")
p = addNode(p, "fox")
p = addNode(p, "fox")
printList(p)
print(countDuplicateStrings(p))

