def leap_year(year):
	flag = 0;
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 != 0:
				flag = 0
			else:
				flag = 1
		else:
				flag = 1

	if flag == 1:
		print "Leap Year"
	else:
		print "Not a Leap Year"
	return;

leap_year(2010);
leap_year(1700);
leap_year(1600);
leap_year(2000);
leap_year(2016);