# Sorting Algorithm Visualizer 
#### What are sorting algorithms and why are they important? 
A sorting algorithm is a method for reorganizing many items into a specific order, such as alphabetical, highest-to-lowest value or shortest-to-longest. We need these algorithms in programming because sorting a list of items can take a long time, especially if it is a large list. A computer program can be created to do this, making sorting a list of data much easier and quicker. 
## Sorting Algorithms supported so far
#### Bubble Sort
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list in order to sort it. This algorithm compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

This algorithm is simple but it is too slow and impractical for most problems even when compared to Python’s built-in sort() function. Bubble sort can be practical if the input is in mostly sorted order or the input is small.

Time/space complexity analysis:

|Worst Case|Average Case|Best Case|In-place?|
|---|---|---|---|
|O(n<sup>2</sup>)|Θ(n<sup>2</sup>)|Ω(n)|Yes|

_in-place means that the algorithm does not use extra space for manipulating the input but may require a small though nonconstant extra space for its operation._
#### Merge Sort
Merge sort is a much faster and more efficient algorithm than Bubble sort. Merge sort is a divide and conquer algorithm. Conceptually, a merge sort works as follows:
•	Divide the unsorted list into n sub-lists, each containing one element (a list of one element is considered sorted).
•	Repeatedly merge sub-lists to produce new sorted sub-lists until there is only one sub-list remaining. This will be the sorted list.

Time/space complexity analysis:

|Worst Case|Average Case|Best Case|In-place?|
|---|---|---|---|
|O(n log(n))|Θ(n log(n))|Ω(n log(n))|Yes|

#### Quick Sort
Quicksort (sometimes called partition-exchange sort) is an efficient sorting algorithm, serving as a systematic method for placing the elements of an array in order. When implemented well, it can be about two or three times faster than its main competitors, merge sort and heapsort.

Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation (formally, a total order) is defined. In efficient implementations it is not a stable sort, meaning that the relative order of equal sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional amounts of memory to perform the sorting. It is very similar to selection sort, except that it does not always choose worst-case partition.

Time/space complexity analysis:

|Worst Case|Average Case|Best Case|In-Place?|
|---|---|---|---|
|O(n<sup>2</sup>)|Θ(n log(n))|Ω(n log(n))|Yes|

##### How to run this on your own computer 
First, download the UI, BubbleSort, MergeSort and QuickSort file and place them in the same folder. Next, you will be able to run the UI file which will launch the app. 

