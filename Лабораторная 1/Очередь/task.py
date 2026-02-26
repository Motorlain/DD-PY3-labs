from typing import Any

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, elem: Any) -> None:
        self._items.append(elem)

    def dequeue(self) -> Any:
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self, ind: int = 0) -> Any:
        if not isinstance(ind, int):
            raise TypeError("Index must be integer")
        if ind < 0 or ind >= len(self._items):
            raise IndexError("Index out of range")
        return self._items[ind]

    def clear(self) -> None:
        self._items = []

    def __len__(self) -> int:
        return len(self._items)

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"Размер очереди: {len(queue)}")
    print(f"Первый элемент: {queue.peek()}")
    print(f"Второй элемент: {queue.peek(1)}")

    print(f"Извлечено: {queue.dequeue()}")
    print(f"Извлечено: {queue.dequeue()}")

    print(f"Размер после извлечения: {len(queue)}")

    queue.clear()
    print(f"Размер после очистки: {len(queue)}")