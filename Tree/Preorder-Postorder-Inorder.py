# Preorder, Postorder and Inorder traversals
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
                
    def PreOrder(self):
        print(self.val)
        if(self.left):
            self.left.PreOrder()
        if(self.right):
            self.right.PreOrder()
    
    def PostOrder(self):
        if(self.left):
            self.left.PostOrder()
        
        if(self.right):
            self.right.PostOrder()
        print(self.val)    
    
    def InOrder(self):
        if(self.left):
            self.left.InOrder()
        print(self.val)  
        if(self.right):
            self.right.InOrder()
          
        
                
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
    root.InOrder()
