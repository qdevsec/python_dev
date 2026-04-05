### Algorithm Complexities

> O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)

> Best / Most Efficient
1. O(1) - constant time
    - Example: Accessing an array index
    - doesn't grow with input size

2. O(log n)  - Logarithmic time
    - Example: binary search
    - Grows very slowly

3. O(n) - Linear time
    - Example: single loop through data
    - Scale proportionally

> Moderate
4. O(n log n) - Linearithmic time
    - Example: efficient sorting like merge sort, heap sort
    - Very practical for large datasets

> Slow
5. O(n^2) - Quadratic time
    - Example: nested loops (bubble sort, selection sort)
    - Becomes slow quickly as n grows

6. O(n^3) - Cubic time
    - Example: triple nested loops
    - Rarely practical for large inputs

> Very Slow / Worst
7. O(2^n) - Exponential time
    - Example: brute-force recursion (subset generation)
    - Explodes rapidly

8. O(n!) - Factorial time
    - Example: permutations (traveling salesman brute force)
    - Completely impractical beyond very small n

### Big-O vs Real Performance

- Two O(n log n) algorithms:
    - Merge sort -> consistent, but uses extra memory
    - Quick sort -> often faster in practice due to cache efficiency

### Examples

```
# O(n) - Linear time - efficient (fast) Single loop

for i in range(n):
    print(i)

# O(n^2) - Quadratic (slow) Nested Loops (dependent)

runs n * n = O(n^2)

for i in range(n):          <- 
    for j in range(n):      <-
        print(i, j)

# O(log n) - Logarithmic loops

doubles each time

i = 1
while i < n:
    i *= 2

# O(n) - Multiple independent loops

Adds up -> n + n = 2n = O(n)

for i in range(n):
    print(i)

for j in range(n):
    print(j)

# O(log n) - halves each time - Divide and conquer (recursion)

def f(n):
    if n <= 1:
        return
    f(n/2)

# Splits into 2 each time -> O(n)

def f(n):
    f(n/2)
    f(n/2)

Merge Sort -> O(n log n)

# Drop constants and lower-order terms

Example:
3n^2 + 5n + 10 --> O(n^2)
n log n + n --> O(n log n)

# Checklist
- How many loops? Nested or separate?
- Does input size shrink each step? (-> log n)
- Is there recursion? How many calls?
- What's the worst-case scenario?

# Example walkthrough

for i in range(n):
    for j in range(n):
        for k in range(10):
            print(i, j, k)

- Outer loops: n * n = n^2
- Inner loop: constant(10)
- Total -> 10n^2 --> O(n^2)

```

##### Sorting Algorithms

- Quick Sort:
    - Avg Time: O(n log n)
    - Worst Time: O(n^2)
    - Notes: Usually fastest in practice

- Merge Sort:
    - Avg Time: O(n log n) 
    - Worst Time: O(n log n)
    - Notes: Stable, predictable

- Heap Sort:
    - Avg Time: O (n log n)
    - Worst Time: O(n log n)
    - Notes: Slower constants

- Bubble Sort:
    - Avg Time: O(n^2)
    - Worst Time: O(n^2)
    - Notes: Only for teaching

- Insertion Sort:
    - Avg Time: O(n^2)
    - Worst Time: O(n^2)
    - Notes: Great for small or nearly sorted data

Small data -> Insertion sort can win

Large data -> Quick sort / Merge sort dominate

##### Searching Algorithms

- Linear Search
    - Time complexity: O(n)
    - Real Performance: Simple, no setup

- Binary Search
    - Time complexity: O(log n)
    - Real Performance: Extremely fast, but requires sort data

##### Graph Algorithms
- Algorithm: BFS / DFS
    - Complexity: O(V + E)
    - Notes: Very efficient

- Algorithm: Dijkstra
    - Complexity: O((V + E) logV)
    - Notes: Fast with priority queue

- Algorithm: Floyd-Warshall
    - Complexity: O(n^3)
    - Notes: Only for small graphs

### What actually affects performance

> Constant Factors
- O(100n) vs O(n) -> same Big-O, but slower in reality

> Memory Usage
- Merge sort uses extra space -> can slow things down
- In-place algorithms (like quicksort) often faster

> Cache Efficiency
- Algorithms accessing memory sequentially -> faster
- Random memory access -> slower

> Input Data
- Nearly sorted -> insertion sort is very fast
- Random -> quicksort shines
- Worst-case patterns can break some algorithms

##### Key points
- Big-O = scaling behavior
- Performance = Big-O + constants + hardware + input
