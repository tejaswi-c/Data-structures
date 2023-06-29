Arrays

1.Brute force: This approach involves checking every possible combination of elements in the array. 
 It is the simplest approach but has a time complexity of O(n^2) or worse, making it inefficient for  large arrays.

2.Two pointers: This approach involves using two pointers to traverse the array, usually from opposite ends.
This approach has a time complexity of O(n) and is often used for problems that involve finding pairs of elements that satisfy a certain condition.
It is inefficient for large arrays

3.Sorting: This approach involves sorting the array and then using the sorted array to solve the problem.
Sorting has a time complexity of O(n log n), so it is less efficient than the two-pointer approach, but it can be useful in some situations.

4.Hash tables: This approach involves using a hash table or dictionary to store the elements of the array and their indices. 
This approach is often used for problems that involve finding duplicates orcounting occurrences of elements.

5.Dynamic programming: This approach involves breaking down the problem into smaller subproblems and solving each subproblem recursively. 
This approach is often used for problems that involve finding the maximum or minimum value of a subarray.

6.Sliding window: This approach involves maintaining a "window" of contiguous elements in the array and sliding the window along the array.
This approach is often used for problems that involve finding a subarray that satisfies a certain condition, such as the maximum sum subarray.


Searching Algorithms
Linear Search: This is the simplest search algorithm, where each element of the list is sequentially checked until a match is found.

Binary Search: This algorithm is applicable only to sorted lists. It repeatedly divides the search space in half, narrowing down the possibilities until the target element is found or determined to be absent.

Hashing: Hashing involves using a hash function to map the search key to an index in an array. It provides efficient lookup, insert, and delete operations.

Sorting Algorithms:

Bubble Sort: This algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order until the entire list is sorted.

Insertion Sort: This algorithm builds the final sorted array one element at a time by inserting each element into its proper position within the sorted portion of the array.

Selection Sort: This algorithm sorts an array by repeatedly finding the minimum element from the unsorted part and placing it at the beginning.

Merge Sort: This algorithm divides the array into two halves, recursively sorts them, and then merges the two sorted halves to obtain a fully sorted array.

Quick Sort: This algorithm selects an element as a pivot, partitions the array around the pivot, and recursively sorts the sub-arrays on either side of the pivot.

Radix sort:This algorithm is sorting is performed from the least significant digit to the most significant digit, creating a chain of sorted sublists. Each subsequent sorting operation takes into account the ordering established by the previous digits.
