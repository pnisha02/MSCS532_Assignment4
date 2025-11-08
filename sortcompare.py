import random
import time
from typing import List, Callable
import Heapsort
from priorityqueue import Task, MaxHeapPQ

# Custom in-place quicksort

def quicksort(a: List[int]) -> None:
    """Simple in-place quicksort using random pivot."""
    def _qs(lo, hi):
        if lo >= hi:
            return
        pivot = a[random.randint(lo, hi)]
        i, j = lo, hi
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        _qs(lo, j)
        _qs(i, hi)
    _qs(0, len(a) - 1)


# Timing helper

def time_sort(sort_fn: Callable[[List[int]], None], arr: List[int]) -> float:
    a = arr.copy()
    start = time.perf_counter()
    sort_fn(a)
    end = time.perf_counter()
    assert a == sorted(arr)  # ensure correctness
    return end - start

def python_sort(a: List[int]) -> None:
    a.sort()


# Benchmark runner

def run_benchmarks(sizes=(1000, 5000, 10000), repeats=3):
    # New number distributions
    distributions = {
        "random": lambda n: [random.randint(0, n*2) for _ in range(n)],
        "sorted": lambda n: list(range(0, n*2, 2)),
        "reverse": lambda n: list(range(n*2, 0, -2)),
        "few_unique": lambda n: [random.choice([10, 20, 30, 40, 50]) for _ in range(n)]
    }
    sort_fns = [
        ("Heapsort", Heapsort.heapsort),
        ("Quicksort", quicksort),
        ("Python Timsort", python_sort)
    ]
    results = {}
    for name, fn in sort_fns:
        results[name] = {}
        for dist_name, gen in distributions.items():
            results[name][dist_name] = {}
            for n in sizes:
                times = []
                for _ in range(repeats):
                    arr = gen(n)
                    t = time_sort(fn, arr)
                    times.append(t)
                avg = sum(times) / len(times)
                results[name][dist_name][n] = avg
                print(f"{name:12} | {dist_name:10} | n={n:6} | avg {avg:.6f}s")
    return results


# Scheduler simulation with new numbers

def scheduler_simulation(n_tasks=10):
    pq = MaxHeapPQ()
    # New priorities for demonstration
    new_priorities = [15, 45, 30, 70, 25, 55, 40, 60, 35, 50]
    for i in range(n_tasks):
        t = Task(id=i, priority=new_priorities[i])
        pq.insert(t)

    processed = []
    while not pq.is_empty():
        task = pq.extract_max()
        processed.append(task)

    return processed


# Main example run

if __name__ == "__main__":
    print("Running brief benchmarks with new number distributions...\n")
    run_benchmarks(sizes=(1000, 2000), repeats=2)

    print("\nRunning scheduler simulation with new task priorities...")
    processed = scheduler_simulation(10)
    print("Tasks processed in descending priority order:")
    for t in processed:
        print(t)
