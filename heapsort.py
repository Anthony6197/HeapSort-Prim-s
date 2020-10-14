class Heap:
    def __init__(self, Array):
        # Set up the heapSize and heap variables
        # Call the buildHeap to build a heap from the array
        self.heapSize = len(Array)
        self.heap = Array
        self.buildHeap(Array)

    def parentOf(self, Index):
        # Returns the index of the parent of the index node
        return (Index - 1) // 2

    def leftChildOf(self, Index):
        # Returns the left child index of the index node
        return (2 * Index + 1)

    def rightChildOf(self, Index):
        # Returns the right child index of the index node
        return (2 * Index + 2)

    def isEmpty(self):
        # Returns if the heap is empty
        return (self.heapSize == 0)

    def buildHeap(self, inputArray):
        # Builds the heap from the half way of the array
        for r in range(len(inputArray)//2, -1, -1):
            self.walkDown(r)

    def lookUpLargest(self):
        # Returns the root of the heap. Or prints Empty Heap if there is no elements in it
        if self.heapSize == 0:
            print("Empty Heap")
        else:
            return self.heap[0]

    def insert(self, val):
        # Insert the value towards the end of the heap and checks the heap at the end
        self.heap.insert(self.heapSize, val)
        self.heapSize = self.heapSize + 1
        self.walkUp(self.heapSize-1)

    def walkUp(self, startPos):
        # Checks the corresponding heap of the input node
        currPos = startPos
        parentPos = self.parentOf(currPos)
        while currPos > 0 and self.heap[currPos] > self.heap[parentPos]:
            temp = self.heap[currPos]
            self.heap[currPos] = self.heap[parentPos]
            self.heap[parentPos] = temp
            currPos = parentPos
            parentPos = self.parentOf(currPos)

    def deleteLargest(self):
        # Takes away the root and checks the corresponding heap of the new root
        self.heap[0] = self.heap[self.heapSize - 1]
        self.heapSize = self.heapSize - 1
        self.walkDown(0)

    def walkDown(self, startPos):
        # Finds the larger kid of the node at the startPos and determines whether to swap them or not
        currPos = startPos
        bigChildPos = self.findLargerChild(currPos)
        while 2 * currPos + 1 < self.heapSize and self.heap[currPos] < self.heap[bigChildPos]:
            temp = self.heap[bigChildPos]
            self.heap[bigChildPos] = self.heap[currPos]
            self.heap[currPos] = temp
            currPos = bigChildPos
            bigChildPos = self.findLargerChild(currPos)

    def findLargerChild(self, pos):
        # Compares the two children of the node at the pos index
        lchildPos = self.leftChildOf(pos)
        rchildPos = self.rightChildOf(pos)

        if lchildPos >= self.heapSize:
            return -1

        elif rchildPos >= self.heapSize:
            return lchildPos

        elif self.heap[lchildPos] < self.heap[rchildPos]:
            return rchildPos

        else:
            return lchildPos


def heapSort(array):
    # Takes in an array and heap sort it and returns an array with increasing order
    heap = Heap(array)
    for i in range(heap.heapSize - 1, -1, -1):
        temp = heap.lookUpLargest()
        heap.deleteLargest()
        array[i] = temp
    return array

array = [0,15,2,3,1,4]
print(heapSort(array))

array2 = [9,2,3,8,4,10,1]
print(heapSort(array2))

array3 = [0,1000,9992,382,123,4382,584,2394,384,2384,574]
print(heapSort(array3))

array4 = [0,372,392,485,753,2,1,4,2384,574]
print(heapSort(array4))

array5 = [1,2,3,4,5,6,7,8]
print(heapSort(array5))