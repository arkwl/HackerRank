"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""
class Stack():
  
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
  
    def pop(self):
        return self.items.pop()


def FindMergeNode(headA, headB):
    stackA = Stack()
    stackB = Stack()
    
    while(headA != None):
        stackA.push(headA)
        headA = headA.next
    
    while(headB != None):
        stackB.push(headB)
        headB = headB.next
    
    valueA = stackA.pop()
    valueB = stackB.pop()
    while(valueA.data == valueB.data):
        if stackA.isEmpty() or stackB.isEmpty():
            return None
        valueA = stackA.pop()
        valueB = stackB.pop()
        
    return valueA.next.data
  
  
  
  
  
  
