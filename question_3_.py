#Python Assignment From Gaone Gee Mokhawa Student Number 14M8501
#3this program takes a DNA sequence and returns the number of non-nucleotide bases

DNA_sequence = raw_input("enter sequence ")
total=0
counter = 0
for counter in range (len(DNA_sequence)):
    if DNA_sequence[counter]== "A" or DNA_sequence[counter]== "T" or DNA_sequence[counter]== "G" or DNA_sequence[counter]== "C":
        continue
    else:
        total = total+1
        counter = counter+ 1
print total

