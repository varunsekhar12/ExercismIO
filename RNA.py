#!/usr/bin/python

def to_rna(dna):
	list = ['G','C','T','A']
	for i in dna:
		if i not in list:
			print "illegal"
		else:
			dna = dna.replace('G','C')
			dna = dna.replace('C','G')
			dna = dna.replace('T','A')
			dna = dna.replace('A','U')
	return dna

def main():
	dna = raw_input()
	rna = to_rna(dna)
	print rna

if __name__ == '__main__':
	main()


