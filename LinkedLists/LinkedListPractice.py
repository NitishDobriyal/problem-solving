class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node    


    def middle(self):
        p = self.head
        q = self.head 
        while(q.next and q.next.next):
            q = q.next.next
            p = p.next 

        return p.val  

    def deleteKthFromEnd(self,k):
        '''
        Approach:
        Take 2 pointers p,q
        Increment p by 1
        Give push start of k nodes to q
        When q will reach end, p will point to n-k
        '''

        p = self.head
        q = self.head
        
        for i in range(k):
            q =  q.next

        print('q=',q.val)    

        while(q.next):
            q = q.next
            p = p.next

        p.next = p.next.next     

    def display(self):
        temp = self.head
        while(temp!=None):
            print(temp.val,end='->')   
            temp = temp.next     


if __name__=="__main__":
    link_list = LinkedList() 
    link_list.insert_at_end(5)
    link_list.insert_at_end(7)
    link_list.insert_at_end(1)
    link_list.insert_at_end(8)
    link_list.insert_at_end(9)
    link_list.insert_at_end(13)
    link_list.insert_at_end(3)
    link_list.display()
    print('\n')
    # print(link_list.middle())   
    link_list.deleteKthFromEnd(3)
    link_list.display()        






