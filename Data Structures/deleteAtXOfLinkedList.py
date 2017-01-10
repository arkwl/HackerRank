"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    local = head
    prev = None
    
    if position == 0:
        head = head.next
        return head
    else: 
        while (position != 0):
            prev = local
            local = local.next
            position -= 1
        prev.next = local.next
    
        return head
