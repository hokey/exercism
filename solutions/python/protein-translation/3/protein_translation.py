"""
Protein Translation Library
"""
CODON_TO_AMINO_ACID = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

def proteins(strand: str) -> list[str]:
    """
    Given the codon strand, produce the amino acid proteins coded within

    :param str strand: Codon strand
    :return list[str]: Amino acids from codons
    """
    amino_acids = []
    step = 3
    codon = None
    for index in range(0, len(strand), step):
        codon = strand[index:index+step]
        if codon not in CODON_TO_AMINO_ACID:
            continue 
        if CODON_TO_AMINO_ACID[codon] == "STOP":
            break 
        amino_acids.append(CODON_TO_AMINO_ACID[codon])
    return amino_acids