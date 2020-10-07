# programming-3

# HeapSort
So we setup a constructor which initializes the array, the size, and transforming the array to a heap. 
Then we built some basic method which gets the lchid, rchild, the parent, is Empty, etc. 
Then we built the walk up and walk down which checks the node's corresponding heap with it as a child and as a parent as we moves through.
Finally we kept deleting the largest node/ the root and keep making sure the order of the heap is right until every node is being deleted.
And that returns us the order from small to large of the array.

The average time is less than the provided one. We tested the algorithm by creating many different off-order arrays and them put them in the heap sort to see how they turn out. Also, we took a correct order array and put it in the heap sort to see how it turns out. Heap sort is very special compare to other sorts and I think we took some time to translate the pseudocode into the actual codes and eventually we understand why both walk up and walk down are needed.

