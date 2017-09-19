#!/bin/usr/python

#GIGASECONDS

from datetime import date

def gigasecond(birth_date):
	days_in_year = 365.2425    
	age = float((date.today() - birth_date).days / days_in_year)
	sec = float(age*31557600)
	if (sec >= 1000000000):
		print "This %d year old person is living for more than 10^9 Seconds!"%(age)
	else:
		print "This %d year old person has not yet lived for 10^9 Seconds!"%(age)
	return
	

def main():
	year = int(raw_input("Enter Year : "))
	month = int(raw_input("Enter Month : "))
	day = int(raw_input("Enter Day : "))
	birth_date = date(year, month, day)
	gigasecond(birth_date)
	return 

if __name__ == '__main__':
	main()
