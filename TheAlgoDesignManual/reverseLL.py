class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse_list(head):
    new_head = None  # this is where we build the reversed list (reusing the existing nodes)
    while head:
        temp = head  # temp is a reference to a node we're moving from one list to the other
        head = temp.next  # the first two assignments pop the node off the front of the list
        temp.next = new_head  # the next two make it the new head of the reversed list
        new_head = temp
    return new_head


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
new = reverse_list(a)
print()
printList(new)
