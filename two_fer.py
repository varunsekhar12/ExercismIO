#!/usr/bin/python

#TWO-FER

def two_fer(name):
	if name != '':
		print "One for %s,one for me."%(name)
	else:
		print "One for you,one for me."
	return 

def main():
	name = raw_input("Enter Name ")
	two_fer(name)
	return 

if __name__ == '__main__':
	main()