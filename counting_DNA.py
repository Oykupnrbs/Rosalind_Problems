def count_nucleotides(dna_sequence):
    counts = {
        'A': dna_sequence.count('A'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G'),
        'T': dna_sequence.count('T')
    }
    
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"

if __name__ == "__main__":
    dna_input = input("Enter DNA sequence: ")
    print(count_nucleotides(dna_input))