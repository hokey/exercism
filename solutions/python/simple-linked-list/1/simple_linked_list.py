"""
Music Playlist Linked List
"""
class EmptyListException(Exception):
    """
    EmptyListException
    """
    pass

class Node:
    """
    Music Playlist Node Item
    """
    def __init__(self, value: int) -> None:
        """
        Initializer for Node

        :param int value: Song ID
        """
        if not isinstance(value, int):
            raise ValueError("Must be music id")
        self.song_id = value
        self.next_song = None
        
    def value(self) -> int:
        """
        Returns the Song ID

        :return int: Song ID
        """
        return self.song_id

    def next(self):
        """
        Returns the associated Song Node

        :return Node | None: Next node or nothing if at the end of the list
        """
        return self.next_song

        
class LinkedList:
    """
    Music playlist as a simple linked list
    """
    def __init__(self, values: list[int] = None):
        """
        LinkedList for Songs initializer
        """
        self.head_song = None
        if not values:
            return
        for song_id in values:
            self.push(song_id)    
            
    def __iter__(self) -> int:
        """
        Linked List Iterator

        :return int: The next song in the list
        """
        current = self.head_song
        while current:
            yield current.value()
            current = current.next()
            
    def __len__(self) -> int:
        """
        Lenth of Songs in Linked List

        :param int: The length of the playlist
        """
        count = 0
        current = self.head_song
        while current is not None:
            count +=1
            current = current.next()
        return count
        
    def head(self) -> Node:
        """
        The end of the playlist

        :return Node: The last song of the playlist
        """
        if not self.head_song:
            raise EmptyListException("The list is empty.")
        return self.head_song
        
    def push(self, value: int) -> None:
        """
        Add a song into the playlist

        :param int: The Song ID to add
        """
        if not isinstance(value, int):
            raise ValueError("Must be a digit based song id")
        new_song = Node(value)
        new_song.next_song = self.head_song
        self.head_song = new_song
        
    def pop(self) -> int:
        """
        Remove and return a Song in the playlist
        
        :return int: The Song ID from the playlist
        """
        next_song = self.head()
        self.head_song = self.head_song.next()
        return next_song.value()

    def reversed(self):
        """
        Returns the reversed order of the playlist

        :return list[int]: The reversed playlist, starting from first entry to last
        """
        result = []
        current = self.head_song
        while current:
            result.insert(0, current.value())
            current = current.next()
        return result
