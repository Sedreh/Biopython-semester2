#More Random Strings
#determine the probability with which a given motif
# occurs in a randomly constructed genome

#form a large collection of smaller random strings
#having the same length as the motif;
#these smaller strings represent the genome's substrings,
#which we can then test against our motif.

#Task1

#Given: A positive integer N = 90000,
# a number x between 0 and 1, and
# a DNA string s of length at most 8 bp.

#Return: The probability that if N random DNA strings having the same length as s
# are constructed with GC-content x, then at least one of the strings equals s.

N = 90000
x = 0.6
s = 'ATAGCCGA'
AT = 0
GC = 0
for i in s:
    if i == 'A' or i == 'T':
        AT += 1
    elif i == 'G' or i == 'C':
        GC += 1
s_prob = (((1 - x) / 2)**AT) * (((x) / 2)**GC)
prob = 1 - (1 - s_prob)**N
print('%0.3f' % prob)

#Task2

#Introduction to Mass Spectrometry
#The prefix spectrum of a weighted string is
# the collection of all its prefix weights.

#Given: A list L of n (n≤100) positive real numbers.

#Return: A protein string of length n−1 whose prefix spectrum is equal to L. Consult the monoisotopic mass table.

mass_data = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
               'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049,
               'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768,
               'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
L = [3524.8542, 3710.9335, 3841.974,3970.0326,4057.0646]
x_masses = []
for i in range(len(L) - 1):
    x_mass = round(L[i + 1] - L[i], 4)
    x_masses.append(x_mass)

rnd_mass_data = {}
for k, v in mass_data.items():
    rnd_mass_data[round(v, 4)] = k

protein = ''
for x in x_masses:
    protein += rnd_mass_data[x]

print(protein)


#Task3

#Say that we have a string s containing t as an internal substring, so that there exist nonempty substrings s1 and s2 of s such that s can be written as s1ts2. A t-prefix contains all of s1 and none of s2; likewise, a t-suffix contains all of s2 and none of s1.
#Given: A list L containing 2n+3 positive real numbers (n≤100). The first number in L is the parent mass of a peptide P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.
#Return: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions exist, you may output any one.

mass_data = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
               'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049,
               'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768,
               'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
with open('/home/sedreh/ITMO/semester2/Biopython/session9/weight') as input_data:
        mass = [float(line.strip()) for line in input_data.readlines()]


def find_weight(current_w, w_list):
    for weight in w_list:
        for item in mass_data.items():
            if abs(item[1] - (weight - current)) < 0.01:
                return item[0]


# Given that len(weights) = 2n+3
n = (len(mass) - 3) / 2

# Initialize Variables
protein = ''
current = mass[1]
myw = [w for w in mass[2:]]

# Iteratively build the protein.
while len(protein) < n:
    temp = find_weight(current, myw)
    if temp == -1:
        break
    else:
        protein += temp
        current += mass_data[temp]
        print(protein)







#In “Inferring Protein from Spectrum”, we inferred a protein string from a list of b-ions. In practice, biologists have no way of distinguishing between b-ions and y-ions in the simplified spectrum of a peptide. However, we will often possess a pair of masses in the spectrum corresponding to a single cut. The two corresponding ions complement each other: for example, mass("PR") + mass("TEIN") = mass("PRTEIN"). As a result, we can easily infer the mass of a b-ion from its complementary y-ion and vice versa, as long as we already know the parent mass, i.e., the mass of the entire peptide.
#The theoretical simplified spectrum for a protein P of length n is constructed as follows: form all possible cuts, then compute the mass of the b-ion and the y-ion at each cut. Duplicate masses are allowed. You might guess how we could modify “Inferring Protein from Spectrum” to infer a peptide from its theoretical simplified spectrum; here we consider a slightly modified form of this problem in which we attempt to identify the interior region of a peptide given only b-ions and y-ions that are cut within this region. As a result, we will have constant masses at the beginning and end of the peptide that will be present in the mass of every b-ion and y-ion, respectively.



