"""
Tools to transcribe data to RNA strands
"""
DNA_TO_RNA = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}


def to_rna(dna_strand: str) -> str:
    """
    Given a DNA strand, convert that sequence to an RNA Strand

    :param str dna_strand: DNA strand
    :return str: RNA strand
    """
    if dna_strand:
        dna_strand = list(dna_strand)
        for index, character in enumerate(dna_strand):
            dna_strand[index] = DNA_TO_RNA[character]
    return "".join(dna_strand)
    