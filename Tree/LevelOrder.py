# Preorder, Postorder and Inorder traversals
from collections import deque
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self,val):

        if not self:
            return Node(val)
            
        if val<self.val:
            if(self.left is None):
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            
            if(self.right is None):
                self.right = Node(val)
            else:
                self.right.insert(val)
              
        return self  
        
    def print_tree(self):
            if self.left:
                self.left.print_tree()
            print(self.val, end=" ")
            if self.right:
                self.right.print_tree()
                
    def LevelOrder(self):
        q1 = deque()
        q1.append(self)
        while(len(q1)>0):
            item = q1.popleft()
            print(item.val)
            
            if(item.left ):
                q1.append(item.left)
            if(item.right ):
                q1.append(item.right)
     
if __name__ == "__main__":
    root = Node(4)
    root.insert(2)
    root.insert(5)
    root.insert(3)
    root.insert(8)
    root.insert(9)
    root.insert(6)
    root.insert(1)
    # root.PreOrder()
    # root.PostOrder()
    # root.InOrder()
    root.LevelOrder()
