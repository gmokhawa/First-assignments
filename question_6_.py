#Python Assignment From Gaone Gee Mokhawa Student Number 14M8501
#6.this program computes the average length of a list of DNA sequences (eg. using the list ['TGAC','aattggcc','ccCCcc']it computes and prints 6)

Sequence_list=input ("enter list ")
L = [len (i) for i in Sequence_list]

print sum (L)/len(Sequence_list)

#print len(Sequence_list)
