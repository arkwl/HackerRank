'''
Given a linked list, return a linked list that takes elements alternatively from the begining and the end

A->b->c->d->e->f


a->f->b->e->c->d

'''


# back - c b a - front : queue    a b c
# back - d e f - front : stack    f e d

# STEP 1: dequeue - a
#        : pop - f
#        : dequeue - b
#           pop - e

#a b c
# f e d

class Node(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

def alternate(node):

    if node == None:
        return node

    length = lengthList(node)


    if lenght < 3:
        return node

    midpoint = length / 2

    # heads of seperated linked lists
    first_portion = spliceList(node, 0, midpoint)
    second_portion = spliceList(node, midpoint, length)

    second_portion = reverse(second_portion)

    head = first_portion
    while 1:
        nextNode = first_portion.nextNode
        first_portion.nextNode = second_portion
        second_portion = second_portion.nextNode

        # i'm getting kicked out of the room as we have run out of time
        # you can still finish this function as my reference

        # thank you!!! Im still wotking on it

        
        # a -> f
        reference to b
        second_portion = e




def lengthList(node):
    if (node == None):
        return 0
    else:
        return lengthList(node.nextNode) + 1


#def spliceNode(node, start, end):
#    counter = 0
#    if (start == end):
#        return
#    else:
#        return spliceNode(node.nextNode, counter + 1, end)


def reverse(node):
    prev = None
    current = node
    nextNode = current.nextNode

    while current:
        current.nextNode = prev
        prev = current
        current = nextNode
        if nextNode != None:
            nextNode = nextNode.nextNode
