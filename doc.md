                             Quicksort Implementation and Analysis

1. Implementation
Quicksort is a divide-and-conquer algorithm that sorts arrays by selecting a pivot, partitioning the array around that pivot, and recursively sorting the resulting sub-arrays. [1]
Please review the implementation in QuickSort.py file and check the overview of the file in Readme file.

2. Performance Analysis [1]
- Best Case
In best case scenario, the pivot divides the array into two equal halves at each steps. This results in time complexity
O(n log n)
- Average Case
On average, the pivot divides the array into reasonably balanced parts. Similar to the best case,
the recursion depth remains O(log n), and partitioning still takes O(n), leading to O(n log n).
- Worst Case
The worst-case scenario occurs when the pivot divides the array in a highly unbalanced way. The recursion depth becomes
O(n), resulting in a total complexity of O(n ^ 2).

- Space Complexity [2]
Quicksort is an in-place sorting algorithm with O(log n) space complexity due to the recursive stack depth.
In the worst case, the stack depth could be O(n), leading to O(n) space complexity.

3. Randomized Quicksort [3]
Please review QuickSort.py for the implementation of Randomized Quicksort where pivot is chosen random.
Randomized Quicksort improves performance by randomly selecting the pivot, reducing the chance of hitting the worst-case scenario. The average-case time complexity remains O( n log n), but with randomization, Quicksort is expected to perform well on a wider range of input distributions.

4. Empirical Analysis
Please check the output to verify the below comparison:

-Randomly Generated arrays
Both algorithm perform similar performance on average, though Randomized Quicksort have little bit better consistency.
-Already Sorted Arrays
Randomized Quicksort is faster than Deterministic Quicksort.
-Reverse Sorted Arrays
Randomized Quicksort outperform Deterministic Quicksort.



                                        Reference

1. GeeksforGeeks. (n.d.). Quick sort algorithm. GeeksforGeeks. https://www.geeksforgeeks.org/quick-sort-algorithm/#complexity-analysis-of-quick-sort-

2. Simplilearn. (n.d.). Quick sort algorithm. Simplilearn. https://www.simplilearn.com/tutorials/data-structure-tutorial/quick-sort-algorithm

3. Saylor Academy. (n.d.). Quicksort and Randomized Algorithms. Saylor Academy. https://learn.saylor.org/mod/page/view.php?id=19003
