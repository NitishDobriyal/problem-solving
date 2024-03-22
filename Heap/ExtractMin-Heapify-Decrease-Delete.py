import math
class MyMinHeap:
    def __init__(self,arr):
        self.arr = arr

    def Parent(self,index):
        return (index-1)//2
    
    def LeftChild(self,index):
        left_index = 2*(index)+1
        return left_index if left_index<len(self.arr) else None
    
    def Rightchild(self,index):
        right_index = 2*(index)+2
        return right_index if right_index<len(self.arr) else None

    def ExtractMin(self):
        '''
        Approach:
        1. Loop from end, as it is the last element in a Min Heap. 
        2. Go untill root node, and swap it with last element
        3. Now pop the last element(which was min)
        4. Now reorder the array(so that it follows properties of a Min heap)
        5. Check for min(parent,left,right): i) if parent is min break
                                             ii) else swap min child with parent
        '''

        if not self.arr:
            return math.inf
        last_val = self.arr[-1]
        cur_index = len(self.arr)-1

        while(cur_index > 0 ):
            parent_index =  self.Parent(cur_index)
            cur_index = parent_index
        self.arr[parent_index],self.arr[-1] = self.arr[-1],self.arr[parent_index]

        self.arr.pop()
        # return self.arr
        self.ShowHeap()
        self.MinHeapify()

    def MinHeapify(self):
        current = 0
        while(current<len(self.arr)):
            left = self.LeftChild(current)
            right = self.Rightchild(current)

            
            if not (left and right):
                return
            if (self.arr[current]>self.arr[left] or self.arr[current]>self.arr[right]):
                if(self.arr[left]<self.arr[right]):
                    print('LEFT SWAP')
                    print('Arr right',self.arr[right])
                    self.arr[current],self.arr[left] = self.arr[left],self.arr[current]
                    current =  left
                else:
                    print('RIGHT SWAP')
                    self.arr[current],self.arr[right] = self.arr[right],self.arr[current]
                    current = right

            else:
                break
            print('------------')
            
    #Approach
    '''
    1. Decrease the element
    2. Check for parent, and loop untill you find parent is less. Otherwise swap parent and current element
    '''
    def DecreaseKey(self,index,decreased_val):
        self.arr[index] = decreased_val
        while(index>0):
            parent_idx = self.Parent(index)
            if(self.arr[index]<self.arr[parent_idx]):
                self.arr[index],self.arr[parent_idx] = self.arr[parent_idx],self.arr[index]
                index = parent_idx
            else:
                break   
        return self.arr    

    def DeleteElement(self,index):
        decreased_val = float('-inf')
        self.DecreaseKey(index,decreased_val)
        self.ShowHeap()
        self.ExtractMin()


    def ShowHeap(self):
        print(self.arr)    


# arr = [12,25,30,35,40,80,32,100,70,60]
# arr = [25,35,30,60,40,80,34,100,70]
# h1 = MyMinHeap(arr)
# h1.ShowHeap()
# h1.DeleteElement(3)
# h1.ShowHeap()

arr = [70,25,30,35,40,80,34,65]
h2 = MyMinHeap(arr)
h2.ShowHeap()
h2.ExtractMin()
h2.ShowHeap()

'''
TC:
Extract Min-> O(log n)
Heapify-> O(log n)
Total: O(log n)

'''