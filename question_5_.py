#Python Assignment From Gaone Gee Mokhawa Student Number 14M8501
#5.this program extends poit 4 by displaying the character 'U' instead of any 't' or 'T' in the original sequnce (eg. if the user inputs "aTtGC" the program prints the string "CGUUa")

DNA_sequence = raw_input("enter sequence ")

DNA_sequence=DNA_sequence.replace ("t","U")
DNA_sequence=DNA_sequence.replace ("T","U")

print DNA_sequence[::-1]
