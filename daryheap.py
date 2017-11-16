"""
The d-ary heap consists of an array of n items, each of which 
has a priority associated with it. These items may be viewed as 
the nodes in a complete d-ary tree, listed in breadth first traversal 
order: the item at position 0 of the array forms the root of the tree, 
the items at positions 1 through d are its children, the next d2 items 
are its grandchildren, etc. Thus, the parent of the item at position i 
(for any i > 0) is the item at position floor((i − 1)/d) and its children 
are the items at positions di + 1 through di + d. According to the heap property, 
in a min-heap, each item has a priority that is at least as large as its parent; 
in a max-heap, each item has a priority that is no larger than its parent.[2][3]

The minimum priority item in a min-heap (or the maximum priority item in a max-heap) may always be found at position 0 of the array. To remove this item from the priority queue, the last item x in the array is moved into its place, and the length of the array is decreased by one. Then, while item x and its children do not satisfy the heap property, item x is swapped with one of its children (the one with the smallest priority in a min-heap, or the one with the largest priority in a max-heap), moving it downward in the tree and later in the array, until eventually the heap property is satisfied. The same downward swapping procedure may be used to increase the priority of an item in a min-heap, or to decrease the priority of an item in a max-heap.[2][3]

To insert a new item into the heap, the item is appended to the end of the array, 
and then while the heap property is violated it is swapped with its parent, moving 
it upward in the tree and earlier in the array, until eventually the heap property 
is satisfied. The same upward-swapping procedure may be used to decrease the 
priority of an item in a min-heap, or to increase the priority of an item in a 
max-heap.[2][3]

To create a new heap from an array of n items, one may loop over the items in 
reverse order, starting from the item at position n − 1 and ending at the item at 
position 0, applying the downward-swapping procedure for each item.[2][3]
"""
