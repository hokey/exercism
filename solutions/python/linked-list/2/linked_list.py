from __future__ import annotations

class Node:
    """
    Node class for linked list
    """
    def __init__(self, value: int, succeeding: Node | None=None, previous: Node | None =None):
        """
        Node constructor
        :param int value:
        :param Node | None succeeding:
        :param Node | None previous:
        """
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    """
    Linked list class
    """
    def __init__(self):
        """
        Linked list constructor
        """
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def __len__(self) -> int:
        """
        Linked list length
        :return:
        """
        return self.length

    def push(self, value: int) -> None:
        """
        Linked list push
        :param int value:
        :return: None
        """
        temp = Node(value)
        if not self.head:
            self.head = temp
            self.tail = temp
        else:
            self.tail.succeeding = temp
            temp.previous = self.tail
            self.tail = temp
        self.length += 1

    def pop(self) -> int:
        """
        Linked list pop
        :return int:  Popped value
        """
        if self.length == 0:
            raise IndexError("List is empty")

        temp = self.tail
        if not temp.previous:
            self.head = None
            self.tail = None
        else:
            self.tail.previous.succeeding = None
            self.tail = self.tail.previous
        self.length -= 1
        return temp.value

    def shift(self) -> int:
        """
        Linked list shift
        :return int: Shifted value
        """
        if self.length == 0:
            raise IndexError("List is empty")
        temp: Node = self.head
        self.head = temp.succeeding
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.length -= 1
        return temp.value

    def unshift(self, value:int ) -> None:
        """
        Linked list unshift
        :param int value:
        :return: None
        """
        temp = Node(value)
        if not self.head:
            self.head = temp
            self.tail = temp
        else:
            self.head.previous = temp
            temp.succeeding = self.head
            self.head = temp
        self.length += 1

    def delete(self, value: int ) -> None:
        """
        Linked list delete
        :param int value: Deleting value
        :return: None
        """
        temp: Node = self.head
        while temp:
            if temp.value == value:
                if not temp.previous and not temp.succeeding:
                    self.head = None
                    self.tail = None
                else:
                    if temp.previous:
                        temp.previous.succeeding = temp.succeeding
                    else:
                        self.head = temp.succeeding
                    if temp.succeeding:
                        temp.succeeding.previous = temp.previous
                    else:
                        self.tail = temp.previous
                        if self.tail:
                            self.tail.succeeding = None

                self.length -= 1
                return
            temp = temp.succeeding

        raise ValueError("Value not found")
