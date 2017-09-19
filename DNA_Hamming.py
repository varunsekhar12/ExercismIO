#!/usr/bin/python

#HAMMING difference in python

def ham_distance(dna1,dna2):
	c = 0
	for char1,char2 in zip(dna1,dna2):
		if(char1!=char2):
			c += 1
	return c

def main():
	dna1 = raw_input("Enter DNA Strand 1 : ")
	dna2 = raw_input("Enter DNA Strand 2 : ")
	distance = ham_distance(dna1,dna2)
	print "The distance is %d"%(distance)
	return

if __name__ == '__main__':
	main() 

	
