#!/usr/bin/python

#COLLATZ COJECTURE

def Collatz(number):
	c = 0
	print number
	while(number >0):
		if number%2 == 0:
			c += 1
			number = number/2
		else:
			number = 3*number + 1
			c +=1
		if(number == 1):
			break
	print "The Number of Steps : ",c
	return 

def main():
	number = int(raw_input("Enter a Number : "))
	Collatz(number)
	return

if __name__ == '__main__':
	main()
