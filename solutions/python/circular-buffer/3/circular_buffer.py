"""
Circular Buffer Utility
"""
from typing import Any

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    pass


class CircularBuffer:
    """
    Circular Buffer Class
    """
    def __init__(self, capacity: int) -> None:
        """
        Initializer for circular buffer

        :param int capacity: 
        """
        if capacity < 1:
            raise ValueError("Buffer size must be a postive number")
        self._size = capacity
        self._buffer = [None] * capacity
        self._front = 0
        self._back = 0

    
    def read(self) -> Any:
        """
        Read from the circular buffer and complain if it's empty
        """
        if self._buffer[self._back] is None:
            raise BufferEmptyException( "Circular buffer is empty")
        item = self._buffer[self._back]
        self._buffer[self._back] = None
        self._back = (self._back + 1) % self._size
        return item
        

    def write(self, data: Any) -> None:
        """
        Writes to the buffer if not full

        :param Any data: Data to write to buffer
        """
        if data is None:
            raise ValueError("Write data is empty")
        if self._front == self._back and self._buffer[self._front] is not None:
            raise BufferFullException("Circular buffer is full")
        self._buffer[self._front] = data
        self._front = (self._front + 1) % self._size

    
    def overwrite(self, data):
        """
        Writes to the buffer explicitly

        :param Any data: Data to write to buffer
        """
        if self._front == self._back and self._buffer[self._front] is not None:
            self._buffer[self._back] = data
            self._front = (self._front + 1) % self._size
            self._back = (self._back + 1) % self._size
        else:
            self.write(data)

    
    def clear(self) -> None:
        """
        Clears entire buffer
        """
        self._buffer: list[Any] = [None] * self._size
        self._front = 0
        self._back = 0