"""
Grade School Class
"""

class School:
    """
    Manages student rosters for a school.
    """
    def __init__(self):
        "Initializes class"
        self.add_event: list[bool] = []
        self.school_roster: dict[int, list[str]] = {}

    
    def add_student(self, name: str, grade: int) -> bool:
        """
        Passively adds student to roster.  Will track success/fail of addition.
        No student with the same name is allowed in different grades.

        :param str name: Name of student
        :param int grade: Grade of student
        :return bool: Result of add
        """
        if name in self.roster():
            self.add_event.append(False)
            return False
        self.school_roster.setdefault(grade, []).append(name)
        self.school_roster[grade] = sorted(self.school_roster[grade])
        self.add_event.append(True)
        return True

    
    def roster(self):
        """
        Give the full school roster

        :return list[str]: Full roster
        """
        return [
            student
            for index in sorted(self.school_roster)
            for student in self.grade(index)
        ]
        
    
    def grade(self, grade_number: int):
        """
        Give the roster of a grade

        :param int grade_number: The school grade
        :return list[str]: Sorted list of students in the grade
        """
        return self.school_roster.get(grade_number, [])

    
    def added(self):
        """
        Return a list of add attempts recorded

        :return list[bool]: List of attempts
        """
        return self.add_event