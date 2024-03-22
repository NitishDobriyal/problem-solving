import math
class MyMinHeap:
    def __init__(self,arr):
        self.arr = arr

    def Parent(self,index):
        return (index-1)//2
    
    def LeftChild(self,index):
        return 2*(index)+1
    
    def Rightchild(self,index):
        return 2*(index)+2

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
        return self.arr
        # self.MinHeapify()

    def MinHeapify(self):
        current = 0
        while(current<len(self.arr)):
            left = self.LeftChild(current)
            right = self.Rightchild(current)
            if(self.arr[current]>self.arr[left] or self.arr[current]>self.arr[right]):
                if(self.arr[left]<self.arr[right]):
                    self.arr[current],self.arr[left] = self.arr[left],self.arr[current]
                    current =  left
                else:
                    self.arr[current],self.arr[right] = self.arr[right],self.arr[current]
                    current = right
            else:
                break

    def ShowHeap(self):
        print(self.arr)    


arr = [12,25,30,35,40,80,32,100,70,60]
h1 = MyMinHeap(arr)
h1.ShowHeap()
h1.ExtractMin()
h1.ShowHeap()
h1.MinHeapify()
h1.ShowHeap()

'''
TC:
Extract Min-> O(log n)
Heapify-> O(log n)
Total: O(log n)

'''