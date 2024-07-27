class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    
def addNode(head, value):
    if head is None:
        return Node(value)
    else:
        current = head
        while current.next is not None:
            current = current.next
        
        newNode = Node(value)
        current.next = newNode
        
    return head


def addInc(head, ind, value):
    if ind == 0:
        if head is not None:
            newNode = Node(value)
            newNode.next = head
            return newNode
        else:
            return Node(value)
    else:
        current = head
        for i in range(ind - 1):
            current = current.next
        
        newNode = Node(value)
        newNode.next = current.next
        current.next = newNode

    return head
    

def removeNode(head, value):
    if head is None:
        return
    
    while head.data is value:
        head = head.next

    
    current = head
    while current.next is not None:
        if current.next.data is value:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


def removeInd(head, ind):
    if head is None:
        return
    
    if ind == 0:
        head = head.next
    else:
        current = head
        for i in range(ind - 1):
            current = current.next

        
        current.next = current.next.next

    return head


def printLst(head):
    while head is not None:
        if head.next is not None:
            print(head.data, end=" --> ")
        else:
            print(head.data, end="")
        
        head = head.next
    print("")


def main():
    p = None
    p = addNode(p, 5)
    p = addNode(p, 15)
    p = addNode(p, 56)
    p = addNode(p, 83)
    p = addNode(p, 57)
    p = addNode(p, 59)
    p = addNode(p, 9)
    printLst(p)

    p = removeInd(p, 6)
    printLst(p)

main()
