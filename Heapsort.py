from typing import List

def _sift_down(a: List[int], start: int, end: int) -> None:
    """Sift element at index start down the heap until heap property restored."""
    root = start
    while True:
        left = 2 * root + 1
        if left > end:
            break
        right = left + 1
        swap = root
        if a[swap] < a[left]:
            swap = left
        if right <= end and a[swap] < a[right]:
            swap = right
        if swap == root:
            return
        a[root], a[swap] = a[swap], a[root]
        root = swap

def _build_max_heap(a: List[int]) -> None:
    """Transform list into a max-heap in-place."""
    n = len(a)
    for start in range((n - 2) // 2, -1, -1):
        _sift_down(a, start, n - 1)

def heapsort(a: List[int]) -> None:
    """Sort list a in-place in ascending order using Heapsort."""
    n = len(a)
    if n <= 1:
        return
    _build_max_heap(a)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]  # move current max to end
        _sift_down(a, 0, end - 1)

# Example usage with new number examples
if __name__ == "__main__":
    examples = {
        "Example 1 (Random small numbers)": [14, 7, 22, 3, 18, 11, 5],
        "Example 2 (Already sorted)": [2, 4, 6, 8, 10, 12, 14],
        "Example 3 (Reverse order)": [100, 80, 60, 40, 20, 0],
        "Example 4 (Mixed positives/negatives)": [9, -6, 15, -2, 0, 7, -3],
        "Example 5 (Repeated elements)": [4, 7, 4, 2, 9, 2, 7, 4, 9],
    }

    for name, arr in examples.items():
        print("\n" + "="*70)
        print(name)
        print("Before sorting:", arr)
        heapsort(arr)
        print("After sorting: ", arr)
