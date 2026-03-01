def distance(strand_a: str, strand_b: str) -> int:
    """
    Find the Hamming distance between DNA strands

    :param str strand_a: DNA sequence
    :param str strand_b: DNA sequence
    :return int: Hamming distance
    """
    a_len = len(strand_a)
    b_len = len(strand_b)

    if a_len != b_len:
        raise ValueError("Strands must be of equal length.")

    result = 0
    for index in range(0, a_len):
        if strand_a[index] != strand_b[index]:
            result += 1
    return result
