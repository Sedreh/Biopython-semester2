import re
import sys
import random


def make_snp(n, seq):
    if n > len(seq):
        raise ValueError ("WARNING: number of SNPs is more than sequence length")
        n = len(seq)
    snp_pos = random.sample(range(0, len(seq)), n)
    snp = []
    for pos in snp_pos:
        snp.append([seq[pos], random.choice(('A', 'C', 'G', 'T')), pos])
    return snp

#passing arguments with the wrong value (e.g. a number outside expected boundaries) should result in a ValueError

def process_file(filename, n):
    print("    SEQ_ID         |  MUTATION  |  POSITION-OF-MUTATION")
    with open(filename) as f:
        for line in f:
            seq_id, seq = re.split(r'\s+', line.strip())
            mutations = make_snp(n, seq)
            for mutation in mutations:
                print(f"{seq_id: <22}{mutation[0]: >10}->{mutation[1]}\t{mutation[2]}")


#sys.argv is a list in Python, which contains the command-line arguments passed to the script.
#With the len(sys.argv) function you can count the number of arguments.


#X in SNPX is bigger than the length of the shortest string in a file -> print warning message
#and assign X to the length of the shortest string in a file.
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: script.py <path-to-seqs> <SNP#>")
        exit()

    filename = sys.argv[1]
    n = int(sys.argv[2][3:])
    try:
        process_file(filename, n)
    except FileNotFoundError as error:
        print(f"No such file: {filename}")
        print(error)



#import sys
#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)
#This is the name of the script:  sysargv.py
#Number of arguments in:  1
#The arguments are:  ['sysargv.py']

#If I run it again with additional arguments, I will get this output:
#This is the name of the script:  sysargv.py
#Number of arguments in:  3
#The arguments are:  ['sysargv.py', 'arg1', 'arg2']