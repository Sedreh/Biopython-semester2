from Bio.SubsMat import MatrixInfo as matlist
from Bio import pairwise2


# """Task: complete the following code that should be able to return the best alignment of two seqs based on BLOSUM62
# matrix."""

def balign(first_seq, second_seq):
    # Load the matrix
    matrix = matlist.blosum62

    # Generate the alignments
    alns = pairwise2.align.globaldx(first_seq, second_seq, matrix)

    # Extract the best alignment (first one in the alns list)
    top_aln = alns[0]

    # Print the alignment, ...
    aln_A, aln_B, score, begin, end = top_aln
    print(pairwise2.format_alignment(aln_A, aln_B, score, begin, end))


balign("KEVLA", "EVL")


# """ TASK: Try to create one-line function (without using Bio package) that returns
# reverse complementary to a given sequence.
# Hint: using dictionaty & list comprehensions might be helpful.
# """

def rev_compl_one_line(seq):
    return ''.join([{'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[x] for x in seq][::-1])


print(rev_compl_one_line("AAATTTTCCCAAAGGG"))
