DNA_TO_RNA = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}
def to_rna(dna_strand):
    if dna_strand:
        dna_strand = list(dna_strand)
        for index in range(0, len(dna_strand)):
            dna_strand[index] = DNA_TO_RNA[dna_strand[index]]
    return "".join(dna_strand)