#A nucleotide is a single piece of a DNA strand (Either A, G, T, or C). An Amino Acid is similar, but for proteins.
# A codon is a group of three nucleotides that translates into an amino acid. Transcription is how an enzyme reads
# the DNA or RNA sequence and makes it into an amino acid chain based on the codons. Some codons "Start" the transcription process.
# Some "Stop" the transcription process until it finds another "Start" codon so it can start all over with a different
# group of nucleotides on the same DNA strand.

#A program to generate all possible peptides for a given dna strand

#Translate DNA into protein using six possible reading frames.
#DNA sequence is assumed to be the coding strand.
# DNA sequence is first transcribed into RNA and
# then translated into protein. The six possible reading frames are:


#1 (forward)
#2 (forward)
#3 (forward)
#-1 (reverse)
#-2 (reverse)
#-3 (reverse)
#Translated sequences are yielded in this order.



##Six-frame translation
#Since DNA is interpreted in groups of three nucleotides (codons),
#a DNA strand has three distinct reading frames.The double helix of a DNA molecule 
#has two anti-parallel strands; with the two strands having three reading frames each, 
#there are six possible frame translations.

from skbio import DNA

dna = DNA('AGTACTAGAGCATTCTATGGAG')
peptides = [str(x) for x in dna.translate_six_frames()]   #
x = sorted(peptides, key=len)



#with Bio package
import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dna = Seq("AGTACTAGAGCATTCTATGGAGA", generic_dna)
print(dna)
dna.complement()

#generate three frameshifts for each of the complement strands
seq1 = dna[0:]
seq2 = dna[1:]
seq3 = dna[2:]
seq4 = dna.complement()[0:]
seq5 = dna.complement()[1:]
seq6 = dna.complement()[2:]

proteins = []
for i in range(3):
    proteins.append(seq1[i:].translate(table=1, to_stop=True))
    proteins.append(seq2[i:].translate(table=1, to_stop=True))
    proteins.append(seq3[i:].translate(table=1, to_stop=True))
    proteins.append(seq4[i:].translate(table=1, to_stop=True))
    proteins.append(seq5[i:].translate(table=1, to_stop=True))
    proteins.append(seq6[i:].translate(table=1, to_stop=True))

P = sorted(proteins, key = lambda x: len(x))
print(P)

#Apply the function to generate all possible translates skipping STOP codon:
def translate(seq, start=False):
    dna = Seq(seq, generic_dna)
    seqs = [dna[0:], dna[1:], dna[2:], dna.complement()[0:], dna.complement()[1:], dna.complement()[2:]]
    proteins = []
    if start:
        for seq in seqs:
            position = seq.find("ATG")
            proteins.append(seq[position:].translate(table=1))
    else:
        for seq in seqs:
            for i in range(3):
                proteins.append(seq[i:].translate(table=1))
    for protein in sorted(proteins, key = lambda x: len(x)):
        print(protein)

translate("AGTACTAGAGCATTCTATGGAG")
