"""
Circular Buffer Utility
"""
from typing import Any

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message: str) -> None:
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message: str) -> None:
        self.message = message


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
        self.size = capacity
        self.clear()
        self.front = self.back = 0

    
    def read(self) -> Any:
        """
        Read from the circular buffer and complain if it's empty
        """
        if self.buffer[self.back] is None:
            raise BufferEmptyException( "Circular buffer is empty")
        item = self.buffer[self.back]
        self.buffer[self.back] = None
        self.back = (self.back + 1) % self.size
        return item
        

    def write(self, data: Any) -> None:
        """
        Writes to the buffer if not full

        :param Any data: Data to write to buffer
        """
        if self.front == self.back and self.buffer[self.front] is not None:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.front] = data
        self.front = (self.front + 1) % self.size

    
    def overwrite(self, data):
        """
        Writes to the buffer explicitly

        :param Any data: Data to write to buffer
        """
        if self.front == self.back and self.buffer[self.front]:
            self.buffer[self.back] = data
            self.front = (self.front + 1) % self.size
            self.back = (self.back + 1) % self.size
        else:
            self.write(data)

    
    def clear(self) -> None:
        """
        Clears entire buffer
        """
        self.buffer: list[Any] = [None] * self.size