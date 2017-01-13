"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    head_1 = head
    head_2 = head
    
    while(head_2 != None):
        head_1 = head_1.next
        
        if head_2.next != None:
            head_2 = head_2.next.next
        else:
            return False
        
        if (head_1 == head_2):
            return True
       
        
    return False