#!/usr/bin/python


def triangle(a,b,c):
	if a == b and b == c and a == c:
		print "Equilateral Triangle"
	elif a == b or b == c or a == c:
		print "Isoceles Triangle"
	else:
		print "Scalene Triangle"
	return

def main():
	a = int(raw_input("Enter Side 1 : "))
	b = int(raw_input("Enter Side 2 : "))
	c = int(raw_input("Enter Side 3 : "))
	triangle(a,b,c)
	return

if __name__ == '__main__':
	main()