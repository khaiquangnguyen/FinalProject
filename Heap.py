from HeapInt import *

'''*
 * An implementation of a minimum heap with handles
 '''

class Heap:

    def __init__(self):
        '''
          The constructor has been set up with an initial array of size 4
          so that your doubleHeap() method will be tested.  Don't change
          this!
        '''
        self.array = [0]*4
        self.heapsize = 0
        self.arraysize = 4
 

    def exchange(self, pos1, pos2):
        '''
          Exchanges that values at positions pos1 and pos2 in the heap array.
          Handles must be exchanged correctly as well.

          Running time = O(1)
        '''

        # Provide your implementation here
        self.array[pos2], self.array[pos1] = self.array[pos1], self.array[pos2]
        tempHandle = self.array[pos2].getHandle()
        self.array[pos2].setHandle(self.array[pos1].getHandle())
        self.array[pos1].setHandle(tempHandle)


    def doubleHeap(self):
        '''
          Doubles the size of the array.  A new array is created, the elements in
          the heap are copied to the new array, and the array data member is set
          to the new array.  Data member arraysize is set to the size of the
          new array.

          Running time = O(n)
        '''

        # Provide your implementation here
        newArray = [0] * self.arraysize * 2
        for i in range(self.arraysize):
            newArray[i] = self.array[i]
        self.array = newArray
        self.arraysize *= 2


    def heapifyDown(self, pos):
        '''
          Fixes the heap if the value at position pos may be bigger than one of
          its children.  Using exchange() to swap elements will simplify your
          implementation.  HeapElts contain records, and records contain
          keys; you will need to decide how to handle comparisons.

          Running time = O(lg n)
        '''

        # Provide your implementation here
        left = pos * 2
        right = pos * 2 + 1
        min = pos
        if left <= self.heapsize and self.array[left].getKey() < self.array[pos].getKey():
            min = left
        else:
            min = pos
        if right <= self.heapsize and self.array[right].getKey() < self.array[min].getKey():
            min = right
        if min != pos:
            self.exchange(pos, min)
            self.heapifyDown(min)


    def heapifyUp(self, pos):
        """
          Fixes the heap if the value at position pos may be smaller than its
          parent.  Using exchange() to swap elements will simplify your
          implementation.  HeapElts contain records, and records contain
          keys; you will need to decide how to handle comparisons.

          Running time = O(lg n)
        """

        # Provide your implementation here
        parent = pos//2
        if parent >= 1 and self.array[parent].getKey() > self.array[pos].getKey():
            self.exchange(pos, parent)
            self.heapifyUp(parent)


    def insert(self, inElt):
        '''
          Insert inElt into the heap.  Before doing so, make sure that there is
          an open spot in the array for doing so.  If you need more space, call
          doubleHeap() before doing the insertion.

          Running time = O(lg n)
          but if there is not enough space in the array then the running time will be O(n) because of doubleHeap()
        '''

        # Provide your implementation here
        if self.heapsize == self.arraysize - 1:
            self.doubleHeap()
        self.heapsize += 1
        inElt.setHandle(self.heapsize)
        self.array[self.heapsize] = inElt
        self.heapifyUp(self.heapsize)

    def removeMin(self):
        '''
          Remove the minimum element from the heap and return it.  Restore
          the heap to heap order.  Assumes heap is not empty, and will
          cause an exception if the heap is empty.

          Running time = O(lg n)
        '''

        # Provide your implementation here
        if self.heapsize == 0:
            print("Heap is empty.\n")
        else:
            temp = self.array[1]
            self.exchange(1, self.heapsize)
            self.heapsize -= 1
            self.heapifyDown(1)
            return temp

    def getHeapsize(self):
        '''
          Return the number of elements in the heap..

          Running time = O(1)
        '''

        # Provide your implementation here    
        return self.heapsize

    def printHeap(self):
        '''
          Print out the heap for debugging purposes.  It is recommended to 
          print both the key from the record and the handle.

          Running time = O(n)
        '''

        # Provide your implementation here
        for i in range(1, self.heapsize):
            print("  " + str(self.array[i].getKey()) + "       " + str(self.array[i].getHandle()))