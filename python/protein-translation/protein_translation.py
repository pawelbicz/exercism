CODON = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan'       
        }

STOP = ['UAA', 'UAG', 'UGA']


def proteins(strand):
    strands = split_strand(strand)
    return match_protein(strands)


def split_strand(strand):
    strands = []
    for i in range(0, len(strand), 3):
       act_strand = strand[i:i+3]
       if strand[act_strand] in STOP:
           break
       else:
           strands.append(act_strand)
    return strands


def match_protein(strands):
    result = []
    for s in strands:
        if s in CODON.keys():
            result.append(CODON[s])
    return result
