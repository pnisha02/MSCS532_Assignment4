# MSCS532_Assignment4
Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications
## Overview
This repository contains Python implementations and analysis of heap-based data structures, specifically:

1. **Heapsort (`Heapsort.py`)**  
   An in-place sorting algorithm using a max-heap, demonstrating predictable O(n log n) performance across all input types.

2. **Priority Queue (`priorityqueu.py`)**  
   A binary max-heap priority queue implementation (`MaxHeapPQ`) that supports dynamic task management, including insertion, extraction, and priority updates.

3. **Benchmark and Scheduler Simulation (`sortcompare.py`)**  
   Compares the performance of Heapsort, QuickSort, and Python’s built-in sort on different input distributions, and demonstrates a scheduler simulation using `MaxHeapPQ`.

## Repository Structure
## Requirements
- Python 3.8 or higher  
- No external libraries required  
## How to Run

### 1. Heapsort
Run `Heapsort.py` to sort several example arrays:

```bash
##1.python Heapsort.py
#output:
Example 1 (Random small numbers)
Before sorting: [14, 7, 22, 3, 18, 11, 5]
After sorting:  [3, 5, 7, 11, 14, 18, 22]

Example 4 (Mixed positives/negatives)
Before sorting: [9, -6, 15, -2, 0, 7, -3]
After sorting:  [-6, -3, -2, 0, 7, 9, 15]

##2.python priorityqueue.py
pq = MaxHeapPQ()
pq.insert(Task(id=1, priority=35))
pq.insert(Task(id=2, priority=50))
max_task = pq.extract_max()
print(max_task)
#Output:
Inserting tasks into priority queue...
Inserting: Task(id=1, priority=35)
Inserting: Task(id=2, priority=50)
Extracted: Task(id=2, priority=50)
Extracted: Task(id=1, priority=35)

##3.python sortcompare.py
#output:
Heapsort     | random     | n=1000 | avg 0.00523s
Quicksort    | random     | n=1000 | avg 0.00419s
Python Timsort | random   | n=1000 | avg 0.00385s

Tasks processed in descending priority order:
Task(id=3, priority=80)
Task(id=6, priority=70)
Task(id=2, priority=50)
...



