class MaxHeap:
    def __init__(self):
        self.arr = [0] * 100
        self.size = 0

    def insert(self, val):
        self.size += 1
        index = self.size
        self.arr[index] = val

        while index > 1:
            parent = index // 2

            if self.arr[parent] < self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                return
            
    def delete_from_heap(self):
        if self.size == 0:
            print("Nothing to Delete in the Heap")
            return
        
        #step 1 : put last element into first index
        self.arr[0] = self.arr[self.size - 1]
        #step 2: remove the last element
        self.size -= 1


        # step 3: take the root node to its correct position
        i = 1
        while i < self.size:
            left_index = 2 * i
            right_index = 2 * i + 1

            if left_index < self.size and self.arr[i] < self.arr[left_index]:
                self.arr[i],self.arr[left_index] = self.arr[left_index],self.arr[i]
                i = left_index
            
            elif right_index < self.size and self.arr[i] < self.arr[right_index]:
                self.arr[i],self.arr[right_index] = self.arr[right_index],self.arr[i]
                i = right_index
            
            else:
                return 


    def print_heap(self):
        for i in range(1, self.size + 1):
            print(self.arr[i], end=" ")
        print()

# Example of usage
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(50)
    max_heap.insert(55)
    max_heap.insert(53)
    max_heap.insert(52)
    max_heap.insert(57)
    max_heap.insert(51)
    max_heap.insert(49)
    max_heap.print_heap()
    max_heap.delete_from_heap()
    max_heap.print_heap()
