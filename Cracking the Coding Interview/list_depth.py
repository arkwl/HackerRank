import Queue

class Node(object):
    def __init__(self, data, left=None, right=None, marked=False):
        self.data = data
        self.left = left
        self.right = right
        self.marked = marked

root = None

def binary_search(array):
    midpoint = len(array)//2
    newNode = Node(array[midpoint])

    if(len(array) != 1):
        newNode.left = binary_search(array[0:midpoint])
        newNode.right = binary_search(array[midpoint+1:len(array)])

    return newNode


def print_tree(node):
    print(node.data)
    if node.left is not None:
        print_tree(node.left)
    #print(node.data)
    if node.right is not None:
        print_tree(node.right)

def bfs(node):
    queue = Queue.Queue()

    node.marked = True
    queue.put(node)

    while (not queue.empty()):
        r = queue.get()

        print(r.data)


        #left
        if(r.left != None and r.left.marked == False):
            r.left.marked = True
            queue.put(r.left)

        #right
        if(r.right != None and r.right.marked == False):
            r.right.marked = True
            queue.put(r.right)


root = binary_search([1, 2, 3, 4, 6 ,7, 8])
bfs(root)
