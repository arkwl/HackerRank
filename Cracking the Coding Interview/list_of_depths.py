import Queue

class Node(object):
    def __init__(self, data, left=None, right=None, marked=False, parentIndex= None):
        self.data = data
        self.left = left
        self.right = right
        self.marked = marked
        self.parentIndex = parentIndex

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
    queue.put((node, 0))

    result = {}

    while (not queue.empty()):

        info = queue.get()
        r = info[0]
        index = info[1]

        #print(str(r.data) + " " + str(index))
        #result[index].append(r.data)
        if index not in result:
            result[index] = []
        result[index].append(r.data)

        #left
        if(r.left != None and r.left.marked == False):
            r.left.marked = True
            queue.put((r.left, index + 1))

        #right
        if(r.right != None and r.right.marked == False):
            r.right.marked = True
            queue.put((r.right, index + 1))

    print result


root = binary_search([1, 2, 3, 4, 6 ,7, 8])
print_tree(root)
bfs(root)
