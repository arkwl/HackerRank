#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    array = []
    length = 0
    headLength = head
    while (headLength != None):
        headLength = headLength.next
        length += 1
    #print length
    while (head != None):
        array.append(head.data)
        head = head.next
    if (position == 0):
        return array[length-1]
    else: 
        return array[length-position-1]
  
  
  
  
  
  
  
  
  
