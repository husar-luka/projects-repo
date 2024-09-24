#%% Generating a random protein
import numpy as np

amino_acid_dict = {
    "Isoleucine": ["ATT", "ATC", "ATA"],
    "Leucine": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"],
    "Valine": ["GTT", "GTC", "GTA", "GTG"],
    "Phenylalanine": ["TTT", "TTC"],
    "Methionine": ["ATG"],
    "Cysteine": ["TGT", "TGC"],
    "Alanine": ["GCT", "GCC", "GCA", "GCG"],
    "Glycine": ["GGT", "GGC", "GGA", "GGG"],
    "Proline": ["CCT", "CCC", "CCA", "CCG"],
    "Threonine": ["ACT", "ACC", "ACA", "ACG"],
    "Serine": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
    "Tyrosine": ["TAT", "TAC"],
    "Tryptophan": ["TGG"],
    "Glutamine": ["CAA", "CAG"],
    "Asparagine": ["AAT", "AAC"],
    "Histidine": ["CAT", "CAC"],
    "Glutamic acid": ["GAA", "GAG"],
    "Aspartic acid": ["GAT", "GAC"],
    "Lysine": ["AAA", "AAG"],
    "Arginine": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "Stop codons": ["TAA", "TAG", "TGA"]
}

def generate_random_protein(n):
    protein = []
    final_protein= []
    protein1 = []
    for i in range(3*n):
        num = np.random.randint(1, 5)
        protein.append(num)
    count = 0
    for i in protein:
        if i == 1:
            protein[count] = "A"
        elif i == 2:
            protein[count] = "G"
        elif i == 3:
            protein[count] = "C"
        elif i == 4:
            protein[count] = "T"
        count += 1
        i = 0
    while i < len(protein):
        codon = str(protein[i]) + str(protein[i+1]) + str(protein[i + 2])
        if codon not in amino_acid_dict["Stop codons"]:
            final_protein.append(codon)
        i = i + 3
        count += 1
    result = "".join(final_protein)
    return result

protein = generate_random_protein(40)
print(f"{protein}")
# %% Frequency of an amino acid in a protein
def frequency_amino_acid(protein, amino_acid):
    sorted_protein = []
    count = 0
    if amino_acid in amino_acid_dict:
        i = 0
        while i < len(protein):
            codon = str(protein[i]) + str(protein[i+1]) + str(protein[i + 2])
            sorted_protein.append(codon)
            i = i + 3
        count = 0
        for i in sorted_protein:
            if i in amino_acid_dict[amino_acid]:
                count += 1
            
    return count


protein = generate_random_protein(10)
frequency_amino_acid(protein, "Serine")
