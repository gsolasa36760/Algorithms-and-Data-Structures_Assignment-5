### Project Overview
The project implements the Quicksort algorithm, including both deterministic and randomized versions. The goal is to demonstrate how randomization in pivot selection improves performance, particularly in avoiding worst-case scenarios. The project provides a detailed analysis of Quicksort’s time complexity in best, average, and worst cases, as well as space complexity. An empirical comparison of the two versions is included, showing how randomization minimizes the likelihood of encountering poor performance in real-world scenarios.

### Prerequisites
Before running the code, make sure you have the following:
- Python 3.x installed on your machine.
- Basic knowledge of Quicksort and its implementation.

### Running the Code
- Run both the deterministic and randomized Quicksort algorithms.
- Compare their performance on various input distributions (random, sorted, reverse-sorted) and input sizes (1000, 5000, 10000).
- Print out the time taken by both algorithms for each test case.

### Summary of Findings

##### Time Complexity:
The deterministic Quicksort performs efficiently in the best and average cases, with a time complexity of O(nlog⁡n). However, in the worst-case scenario, where the pivot consistently divides the array into highly unbalanced subarrays, the time complexity becomes O(n^2). The randomized version, by choosing pivots randomly, reduces the likelihood of encountering the worst-case scenario and maintains O(nlog⁡n) performance even with sorted or reverse-sorted arrays.

##### Space Complexity:
The space complexity of Quicksort primarily depends on the recursion stack. In the average and best cases, the recursion depth is logarithmic, leading to a space complexity of O(log⁡n). However, in the worst case, where the recursion tree becomes unbalanced, the space complexity can increase to O(n).

##### Effect of Randomization:
Randomization significantly improves Quicksort’s performance by reducing the chances of unbalanced partitions, especially for sorted or reverse-sorted arrays. By randomizing the pivot selection, the likelihood of encountering the worst-case O(n^2) time complexity is greatly reduced, resulting in more consistent and efficient performance.

### Conclusion
The implementation of both deterministic and randomized Quicksort shows the effectiveness of randomization in improving the algorithm's robustness. While the deterministic version struggles with sorted or reverse-sorted arrays, the randomized version maintains consistent O(nlogn) performance. This makes randomized Quicksort a more reliable and efficient sorting algorithm for real-world data, where input distributions are not always random. The empirical analysis confirms that randomization significantly minimizes the risk of worst-case performance, making it a preferable choice in practice.
The implementation of both deterministic and randomized Quicksort shows the effectiveness of randomization in improving the algorithm's robustness. While the deterministic version struggles with sorted or reverse-sorted arrays, the randomized version maintains consistent O(nlog⁡n)O(n \log n)O(nlogn) performance. This makes randomized Quicksort a more reliable and efficient sorting algorithm for real-world data, where input distributions are not always random. The empirical analysis confirms that randomization significantly minimizes the risk of worst-case performance, making it a preferable choice in practice.
