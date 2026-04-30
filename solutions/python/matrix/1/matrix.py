"""
Matrix Utility
"""

class Matrix:
    """
    Matrix Class
    """
    def __init__(self, matrix_string: str) -> None:
        """
        Matrix Class Initializer

        Assumptions: The matrix has equal length of rows and columns
        
        :param str matrix_string: String to process as a matrix
        """
        if not matrix_string.strip():
            raise ValueError("Invalid string: must be non empty")
        self.matrix: list[list[int]] = [list(map(int, row.split())) for row in matrix_string.split("\n")]

    
    def row(self, index: int) -> list[int]:
        """
        Returns the row of a matrix if available

        :param int index: Index of row
        :return list[int]: The row of the matrix
        """
        if index > len(self.matrix) or index - 1 < 0:
            raise ValueError("Index for matrix row out of bounds")
        return self.matrix[index - 1]

    
    def column(self, index: int) -> list[int]:
        """
        Returns the column of a matrix if available
        
        :param int index: Index of column
        :return list[int]: The column of the matrix
        """
        if index > len(self.matrix[0]) or index - 1 < 0:
            raise ValueError("Index for matrix column out of bounds")
        return [row[index - 1] for row in self.matrix]
        