class MyMinHeap:
    def __init__(self):
        self.arr = arr

    def Parent(self,index):
        return (index-1)//2
    
    def Build(self):
        size = len(self.arr)-1
        for cur in range(size,-1,-1):
            while(cur>0):
                parent_idx = self.Parent(cur)
                if(self.arr[cur]<self.arr[parent_idx]):
                    self.arr[cur],self.arr[parent_idx] = self.arr[parent_idx],self.arr[cur]
                    cur = parent_idx
                else:
                    break
    def showHeap(self):
        print(self.arr)  

arr = [10,5,20,2,4,8]
h1 = MyMinHeap()
h1.Build()
h1.showHeap()          


'''
Approach:
1. Loop from end, adjust each element by checking whether it is rightly placed(by comparing that element with its parent)

TC: O(n*logn)
'''