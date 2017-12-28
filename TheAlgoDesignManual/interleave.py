class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def merge(p, q):
    p_curr = p
    q_curr = q
    # While there are available positions in p;
    while p_curr != None and q_curr != None:

        # Save next pointers
        p_next = p_curr.next
        q_next = q_curr.next

        # make q_curr as next of p_curr
        q_curr.next = p_next # change next pointer of q_curr
        p_curr.next = q_curr # change next pointer of p_curr

        # update current pointers for next iteration
        p_curr = p_next
        q_curr = q_next
    return p

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

one = Node('1')
two = Node('2')
three = Node('3')
one.next = two
two.next = three
three.next = four
four.next = five

printList(a)
print()
printList(one)
new = merge(a, one)
print()
printList(new)
