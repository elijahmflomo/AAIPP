"""
Sample output produced by running the few-shot prompt from Q2.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    value: Any
    next: Optional["Node"] = None


class LinkedList:
    """Singly linked list with insert and delete helpers."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def insert(self, value: Any, index: int) -> None:
        """Insert value at zero-based position; append if index exceeds length."""
        new_node = Node(value)
        if self.head is None or index <= 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev = self.head
        current_index = 0
        while prev.next and current_index < index - 1:
            prev = prev.next
            current_index += 1

        new_node.next = prev.next
        prev.next = new_node

    def delete(self, value: Any) -> bool:
        """Delete first node matching value. Return True if removed."""
        prev: Optional[Node] = None
        current = self.head
        while current:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True
            prev, current = current, current.next
        return False

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(repr(current.value))
            current = current.next
        return "LinkedList([" + ", ".join(values) + "])"


if __name__ == "__main__":
    lst = LinkedList()
    lst.insert("a", 0)
    lst.insert("b", 1)
    lst.insert("c", 2)
    print(lst)
    lst.insert("z", 1)
    print(lst)
    lst.delete("b")
    print(lst)

