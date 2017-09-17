#!/usr/bin/python

def Space_Age(age,planet):
	earth_sec = 31557600
	earth_age = float(age/earth_sec)
	Planet_yr = float(earth_sec/planet)
	Planet_age = earth_age * Planet_yr
	return Planet_age

def planet_calc(option):	
	planet = 0;
	if(option == 1):
		planet = 7600387.7512
		return planet
	if(option == 2):
		planet = 19413750.4043
		return planet
	if(option == 3):
		planet = 59352813.9214
		return planet
	if(option == 4):
		planet = 374347972.1494
		return planet
	if(option == 5):
		planet = 929273280.9060
		return planet
	if(option == 6):
		planet = 2651315576.4133
		return planet
	if(option == 7):
		planet = 5200311775.2566
		return planet
	else:
		print "eRRoR"

def main():
	age = long(raw_input("Enter Age in Seconds : "))
	print "1.Mercury 2.Venus 3.Mars 4.Jupiter 5.Saturn 6.Uranus 7.Neptune"
	opt= int(raw_input("Enter Option : "))
	planet = planet_calc(opt)
	planet_age = Space_Age(age,planet)
	print "Your Age in Planet %d "%(opt)
	print planet_age
	return 

if __name__ == '__main__':
	main()

