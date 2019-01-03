def to_rna(dna_strand):
    dna_strand = dna_strand.upper()
    rna_strand = ''
    switch = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for i in dna_strand:
        try:
            rna_strand += switch[i]
        except:
            print('There is no DNA strand')
    return rna_strand
