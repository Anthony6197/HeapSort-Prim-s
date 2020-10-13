# programming-3

# HeapSort
So we setup a constructor which initializes the array, the size, and transforming the array to a heap. 
Then we built some basic method which gets the lchid, rchild, the parent, is Empty, etc. 
Then we built the walk up and walk down which checks the node's corresponding heap with it as a child and as a parent as we moves through.
Finally we kept deleting the largest node/ the root and keep making sure the order of the heap is right until every node is being deleted.
And that returns us the order from small to large of the array.

The average time is less than the provided one. We tested the algorithm by creating many different off-order arrays and them put them in the heap sort to see how they turn out. Also, we took a correct order array and put it in the heap sort to see how it turns out. Heap sort is very special compare to other sorts and I think we took some time to translate the pseudocode into the actual codes and eventually we understand why both walk up and walk down are needed.

# Prim's Algorithm
Instead of using the heapsort we implemented, we use one of the built-in function of python called heapq to contain the neighbors of the chosen vertices.After we implement the Prim's Algorithm, we carried two different knids of tests: 1) starting at different vertices in the same graph; 2) testing on different graphs, regardless the choice of the starting vertex. The results are expressed as a list contain the index of the predecessor vertex of the vertex at that index. For example, result [None, 3, 0, 2, 1] means that vertex with index 0 is a terminal, vertex 1 connects to its predecessor 3 and vertex 2 connects to its predecessor vertex 0 and so on until all the vertices are connected to a path, which is the MST of the input graph. The Algorithm works as expected. However, there might be some waste of memory due to using heapq.
