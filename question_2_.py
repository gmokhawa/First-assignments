#Python Assignment From Gaone Gee Mokhawa Student Number 14M8501
#2.this program prompts for a DNA sequence and then returns the first 3 bases and the las 3 bases. if the sequece is shorter than 6, it shows a warning message preventing the execution of the tak.

DNA_sequence=raw_input ("enter DNA sequence ")

#counter=1
if len (DNA_sequence) < 6:
    print "the lenth of your sequence is short "
else:
        
    print DNA_sequence[:3]
    
    print DNA_sequence[-3:]


