from skbio import DNA

dna = DNA('AGTACTAGAGCATTCTATGGAG')
peptides = [str(x) for x in dna.translate_six_frames()]
x = sorted(peptides, key=len)

print(x)
