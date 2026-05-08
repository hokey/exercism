"""
Garden Utility Class
"""
from dataclasses import dataclass, field

@dataclass
class Garden:
    """
    Garden management class for Kindergarten students
    """
    diagram: str | list[str]
    students: list[str] = field(default_factory = lambda: [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry"
    ])
    PLANTS = {
        "C": "Clover",
        "G": "Grass",
        "R": "Radishes",
        "V": "Violets"
    }

    
    def __post_init__(self):
        """
        Post initializer for Garden, this cleans up the diagram string
        """
        self.diagram = self.diagram.split("\n")
        self.students = list(sorted(self.students))
        if len(self.diagram) != 2:
            raise ValueError("The diagram must have 2 rows")
        if len(self.diagram[0]) != len(self.diagram[1]):
            raise ValueError("Rows must have same length")
        if any(plant not in self.PLANTS for row in self.diagram for plant in row):
            raise ValueError("Invalid plant submitted")

        
    def plants(self, student):
        """
        Returns the list of plants for the requested student.

        :param str student: The student
        :return list[str]: The plants, or raise an error if student is not found
        """
        if student not in self.students:
            raise ValueError("Student not found in class list")
        student_index: int = self.students.index(student) * 2
        row1: list[str] = [self.PLANTS[plant] for plant in self.diagram[0][student_index:student_index + 2]]
        row2: list[str] = [self.PLANTS[plant] for plant in self.diagram[1][student_index:student_index + 2]]
        return row1 + row2