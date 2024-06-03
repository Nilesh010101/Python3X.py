def mrnatrans(dna_template):
    for i, j in dna_template.items():
        print(i,"--", j)
        mrnatrans={'A':'U', 'T':'A', 'C':'G', 'G':'C'}
        print(mrnatrans)

