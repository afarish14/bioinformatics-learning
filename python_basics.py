sequence = "ATGCGTACGTTAGC"

bases = ["A", "T", "G", "C"]

print("Sequence:", sequence)
print("Length:", len(sequence))

for base in bases:
    count = sequence.count(base)
    print(base, count)

def count_bases(sequence):
    for base in bases:
        count = sequence.count(base)
        print(base, count)

count_bases(sequence)