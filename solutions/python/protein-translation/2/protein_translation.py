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

def proteins(strand):
    """
    Given the codon strand, produce the amino acid proteins coded within

    :param str strand: Codon strand
    :return list[str]: Amino acids from codons
    """
    amino_acids = []
    step = 3
    if len(strand) < 3:
        return amino_acids
    protein = None
    for index in range(0, len(strand), step):
        protein = strand[index:index+step]
        if protein not in CODON_TO_AMINO_ACID:
            continue 
        protein = CODON_TO_AMINO_ACID[protein]
        if protein == "STOP":
            break 
        amino_acids.append(protein)
    return amino_acids