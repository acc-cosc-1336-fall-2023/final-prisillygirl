#write functions here, don't add input('') statements here!

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
     
    positions = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        positions.append(i + 1)

    return tuple(positions)

dna_string1 = "GATATATGCATATACTT"
dna_string2 = "ATAT"

positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)


for position in positions:
    print(position)