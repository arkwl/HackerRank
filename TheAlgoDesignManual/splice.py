class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def splice(head, start, end):
    if (start == end):
        return None
    counter = 0
    new_list = None
    while head != None:
        if(counter == start):
            new_list = head
            head = new_list
        elif (counter == end - 1):
            head.next = None
            break

        counter = counter + 1
        head = head.next
    return new_list



def printList(node):
    if node != None:
        print(node.data)
        printList(node.next)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e
printList(a)
new = splice(a, 1, 3)
print()
printList(new)
