"""
Complex Number Utility
"""
from __future__ import annotations
from dataclasses import dataclass
from math import sqrt, exp, sin, cos
from typing import Any

@dataclass
class ComplexNumber:
    """
    Complex Number Class
    """
    real: float
    imaginary: float

    def __hash__(self) -> int:
        """
        Hash
        :return int:
        """
        return hash((self.real, self.imaginary))

    def __eq__(self, other: Any) -> bool:
        """
        Equality
        :param Any other:
        :return bool:
        """
        return self.real == other.real and self.imaginary == other.imaginary

    def __radd__(self, other: Any) -> ComplexNumber:
        """
        Right addition
        :param Any other:
        :return ComplexNumber:
        """
        return self.__add__(other)

    def __add__(self, other: Any) -> ComplexNumber:
        """
        Addition
        :param Any other:
        :return ComplexNumber:
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                real=self.real + other.real,
                imaginary=self.imaginary + other.imaginary
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(
                real=self.real + other,
                imaginary=self.imaginary
            )
        else:
            return NotImplemented

    def __rmul__(self, other: Any) -> ComplexNumber:
        """
        Right multiplication
        :param Any other:
        :return ComplexNumber:
        """
        return self.__mul__(other)

    def __mul__(self, other) -> Any:
        """
        Multiplication
        :param Any other:
        :return ComplexNumber:
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                real=self.real * other.real - self.imaginary * other.imaginary,
                imaginary=self.imaginary * other.real + self.real * other.imaginary
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(
                real=self.real * other,
                imaginary=self.imaginary * other
            )
        else:
            return NotImplemented

    def __rsub__(self, other: Any) -> ComplexNumber:
        """
        Right subtraction
        :param Any other:
        :return ComplexNumber:
        """
        if isinstance(other, (int, float)):
            return ComplexNumber(
                real=other - self.real,
                imaginary= -self.imaginary
            )
        else:
            return NotImplemented


    def __sub__(self, other: Any) -> ComplexNumber:
        """
        Subtraction
        :param Any other:
        :return ComplexNumber:
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                real=self.real - other.real,
                imaginary=self.imaginary - other.imaginary
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(
                real=self.real - other,
                imaginary=self.imaginary
            )
        else:
            return NotImplemented

    def __rtruediv__(self, other: Any) -> ComplexNumber:
        """
        Right division
        :param Any other:
        :return ComplexNumber:
        """
        if isinstance(other, (int, float)):
            return ComplexNumber(
                real = (
                    (self.real * other)
                    /
                    (self.real ** 2 + self.imaginary ** 2)
                ),
                imaginary = (
                    (self.imaginary * -other)
                    /
                    (self.real ** 2 + self.imaginary ** 2)
               )
            )
        else:
            return NotImplemented

    def __truediv__(self, other: Any) -> ComplexNumber:
        """
        Division
        :param Any other:
        :return ComplexNumber:
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                real=(
                    (self.real * other.real + self.imaginary * other.imaginary)
                    /
                    (other.real ** 2 + other.imaginary ** 2)
                ),
                imaginary=(
                    (self.imaginary * other.real - self.real * other.imaginary)
                    /
                    (other.real ** 2 + other.imaginary ** 2)
                )
            )
        elif isinstance(other, (int, float)):
            return ComplexNumber(
                real= self.real / other,
                imaginary=self.imaginary / other
            )
        else:
            return NotImplemented

    def __abs__(self) -> float:
        """
        Absolute value
        :return float:
        """
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self) -> ComplexNumber:
        """
        Conjugate
        :return ComplexNumber:
        """
        return ComplexNumber(
            real=self.real,
            imaginary=self.imaginary * -1
        )

    def exp(self) -> ComplexNumber:
        """
        Exponent
        :return ComplexNumber:
        """
        return ComplexNumber(
            real= exp(self.real) * cos(self.imaginary),
            imaginary= exp(self.real) * sin(self.imaginary)
        )
