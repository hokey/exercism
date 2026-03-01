"""
Get the Humming Distance
"""

def distance(strand_a: str, strand_b: str) -> int:
    """
    Find the Hamming distance between DNA strands

    :param str strand_a: DNA sequence
    :param str strand_b: DNA sequence
    :return int: Hamming distance
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(a != b for a, b in zip(strand_a, strand_b))