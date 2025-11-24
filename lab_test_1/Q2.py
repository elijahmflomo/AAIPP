"""
Few-shot prompt for instructing an AI tool to implement a basic singly linked list
with insert and delete operations.
"""

PROMPT = """
You are a precise Python coding assistant. Write clean, well-commented code
for a singly linked list class with insert and delete operations.

## Requirements
- Provide a `Node` dataclass storing `value` and `next`.
- Provide a `LinkedList` class supporting:
  - `insert(value, index)` inserts at zero-based position (append if index >= len).
  - `delete(value)` removes first matching node, returns True/False accordingly.
- Include `__repr__` for easy inspection.
- Add minimal usage example under `if __name__ == "__main__":`.

## Style
- Use type hints and docstrings.
- Avoid external libraries beyond `dataclasses`.
- Keep the implementation under ~80 lines excluding sample usage.

## Few-shot examples

Example 1:
User request: "Write a stack with push/pop and show sample use."
Assistant response:
```python
from dataclasses import dataclass

@dataclass
class Stack:
    items: list[str]

    def push(self, value: str) -> None:
        self.items.append(value)

    def pop(self) -> str:
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()


if __name__ == "__main__":
    stack = Stack([])
    stack.push("alpha")
    print(stack.pop())
```

Example 2:
User request: "Implement a queue with enqueue/dequeue."
Assistant response:
```python
from collections import deque

class Queue:
    def __init__(self) -> None:
        self._data: deque[int] = deque()

    def enqueue(self, value: int) -> None:
        self._data.append(value)

    def dequeue(self) -> int:
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()
```

Now fulfill the linked list request exactly once, producing only the Python code.
"""


if __name__ == "__main__":
    print(PROMPT.strip())

