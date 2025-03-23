def parse_fasta(fasta_string):
    sequences = {}
    label = None
    
    for line in fasta_string.strip().split("\n"):
        if line.startswith(">"):
            label = line[1:]
            sequences[label] = ""
        else:
            sequences[label] += line
    
    return sequences

def gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    return (gc_count / len(dna_sequence)) * 100

if __name__ == "__main__":
    fasta_input = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
    sequences = parse_fasta(fasta_input)
    
    max_label = max(sequences, key=lambda seq: gc_content(sequences[seq]))
    max_gc = gc_content(sequences[max_label])
    
    print(max_label)
    print(f"{max_gc:.6f}")
