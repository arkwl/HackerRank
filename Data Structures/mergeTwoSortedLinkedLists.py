"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if (headA == None):
        return headB
    elif (headB == None):
        return headA
    else: 
        headNew = None
        returned = None
        
        if (headA.data > headB.data):
           headB.next = MergeLists(headA, headB.next)
           return headB
        else:
           headA.next = MergeLists(headA.next, headB)
           return headA

  
  
  
  
  
  
  
  
  