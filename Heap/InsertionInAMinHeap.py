
class InsertInMinHeap:
    def __init__(self,arr):
        self.arr =  arr

    def Parent(arr,cur_index):
        return (cur_index-1)//2

    def insert(self,val):

        #First insert element at the end
        if(self.arr):
            self.arr.append(val) 
        cur_index = len(self.arr)-1     

        #Check for the parent node of newly inserted node, if it is greater than swap it.(Update current index with parents index)
        #Do this till we reach root(i.e 0 index) to find it's correct position
        while(cur_index>0):
            parent_index = self.Parent(cur_index)
            if self.arr[parent_index]<=val:
                break
            else:
                self.arr[parent_index],self.arr[cur_index] =  self.arr[cur_index],self.arr[parent_index]
                cur_index = parent_index               

    def showHeap(self):
        print(self.arr)


arr = [10,20,15,40,50,100,25,45]
h1 = InsertInMinHeap(arr)
h1.insert(12)
h1.showHeap()
h1.insert(14)
h1.showHeap()


'''
Proprties of a MinHeap in array
Parent[i] = i-1//2 (floor div)
LeftChild[i] = 2*(i)+1
Rightchild[i] = 2*(i)+2

Time Complexity: O(Log n) -> 
Since the height of the binary heap is logarithmic 
with respect to the number of elements (base 2), the number of comparisons needed to insert an element and maintain the heap property is O(log n), where n is the number of elements in the heap.
'''