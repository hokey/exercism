"""
Tools to transcribe data to RNA strands
"""
DNA_TO_RNA = str.maketrans({
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
})


def to_rna(dna_strand: str) -> str:
    """
    Given a DNA strand, convert that sequence to an RNA Strand

    :param str dna_strand: DNA strand
    :return str: RNA strand
    """
    return dna_strand.translate(DNA_TO_RNA)
    