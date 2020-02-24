from functools import reduce
from operator import mul
inp = "The gunman was shot dead by police ."
ref = "The gunman was shot dead by the police ."


def nGrammer(inSplit, n, gram_array):
    grams_list = []
    i=0
    while i + n <= len(inSplit):
        grams_list.append(" ".join(inSplit[i:i+n]))
        i+=1
    gram_array.append(grams_list)
    return grams_list

def calcPrecision(ref, nGrams):
    precisions = []

    ref_gram1 = ref.split()
    ref_nGrams.append(ref_gram1)
    ref_gram2 = nGrammer(ref_gram1, 2, ref_nGrams)
    ref_gram3 = nGrammer(ref_gram1, 3, ref_nGrams)
    ref_gram4 = nGrammer(ref_gram1, 4, ref_nGrams)

    i=0
    while i < len(nGrams):
        ref_len = len(ref_nGrams[i])
        a = nGrams[i]
        b = ref_nGrams[i]
        match = set(a) & set(b)
        precisions.append(len(match)/ref_len)
        i+=1

    return reduce(mul, precisions, 1)


def calcMin(output, ref):
    return min(1, (len(output)/len(ref)) )


splitted = inp.split()
nGrams = []
ref_nGrams = []

gram1 = splitted
nGrams.append(gram1)
gram2 = nGrammer(splitted, 2, nGrams)
gram3 = nGrammer(splitted, 3, nGrams)
gram4 = nGrammer(splitted, 4, nGrams)

BLEU = calcMin(inp, ref) * calcPrecision(ref, nGrams)
print(BLEU)
