from dataclasses import dataclass, field
from typing import Any, List, Optional

@dataclass(order=False)
class Task:
    id: int
    priority: int
    arrival_time: Optional[float] = None
    deadline: Optional[float] = None
    meta: Any = field(default=None)

    def __repr__(self):
        return f"Task(id={self.id}, priority={self.priority})"

class MaxHeapPQ:
    def __init__(self):
        self._data: List[Task] = []
        self._pos_by_id = {}  # id -> index in _data

    def __len__(self):
        return len(self._data)

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def _swap(self, i: int, j: int):
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._pos_by_id[self._data[i].id] = i
        self._pos_by_id[self._data[j].id] = j

    def _sift_up(self, idx: int):
        while idx > 0:
            parent = (idx - 1) // 2
            if self._data[parent].priority >= self._data[idx].priority:
                break
            self._swap(parent, idx)
            idx = parent

    def _sift_down(self, idx: int):
        n = len(self._data)
        while True:
            left = 2 * idx + 1
            right = left + 1
            largest = idx
            if left < n and self._data[left].priority > self._data[largest].priority:
                largest = left
            if right < n and self._data[right].priority > self._data[largest].priority:
                largest = right
            if largest == idx:
                break
            self._swap(idx, largest)
            idx = largest

    def insert(self, task: Task):
        idx = len(self._data)
        self._data.append(task)
        self._pos_by_id[task.id] = idx
        self._sift_up(idx)

    def extract_max(self) -> Task:
        if not self._data:
            return None
        top = self._data[0]
        last = self._data.pop()
        del self._pos_by_id[top.id]
        if self._data:
            self._data[0] = last
            self._pos_by_id[self._data[0].id] = 0
            self._sift_down(0)
        return top

    def peek_max(self) -> Task:
        return self._data[0] if self._data else None

    def increase_key(self, task_id: int, new_priority: int) -> bool:
        idx = self._pos_by_id.get(task_id)
        if idx is None:
            return False
        if new_priority <= self._data[idx].priority:
            return False
        self._data[idx].priority = new_priority
        self._sift_up(idx)
        return True

    def decrease_key(self, task_id: int, new_priority: int) -> bool:
        idx = self._pos_by_id.get(task_id)
        if idx is None:
            return False
        if new_priority >= self._data[idx].priority:
            return False
        self._data[idx].priority = new_priority
        self._sift_down(idx)
        return True

# Example usage with new task numbers

if __name__ == "__main__":
    # New task examples
    tasks = [
        Task(id=1, priority=35),
        Task(id=2, priority=50),
        Task(id=3, priority=15),
        Task(id=4, priority=70),
        Task(id=5, priority=25),
        Task(id=6, priority=90),
        Task(id=7, priority=40),
    ]

    pq = MaxHeapPQ()
    print("Inserting tasks into priority queue...")
    for t in tasks:
        print("Inserting:", t)
        pq.insert(t)

    print("\nExtracting tasks by priority:")
    while not pq.is_empty():
        t = pq.extract_max()
        print("Extracted:", t)

    # Test increase/decrease key
    print("\nRe-inserting tasks for key updates...")
    for t in tasks:
        pq.insert(t)

    print("Increasing Task 3 priority to 80...")
    pq.increase_key(task_id=3, new_priority=80)
    print("Decreasing Task 6 priority to 20...")
    pq.decrease_key(task_id=6, new_priority=20)

    print("\nTasks after priority updates (extracting max):")
    while not pq.is_empty():
        t = pq.extract_max()
        print("Extracted:", t)
