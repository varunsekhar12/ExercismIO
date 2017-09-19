#!/usr/bin/python

#ALLERGIES

"""I could modify to add Dictionaries """

def allergies(item):
	if item == "eggs":
		score = 1
	if item == "peanuts":
		score = 2
	if item == "shellfish":
		score = 4
	if item == "strawberries":
		score = 8
	if item == "tomatoes":
		score = 16
	if item == "chocolate":
		score = 32
	if item == "pollen":
		score = 64
	if item == "cats":
		score = 128
	return score

def main():
	Tscore = 0
	list =[]
	no = int(raw_input("Enter No of Stuff: "))
	for i in range(0,no):
		item = raw_input("Enter Allergic Items: ")
		list.append(item)
		score = allergies(item)
		Tscore = Tscore + score
	print Tscore
	score = int(raw_input("Enter the Score : "))
	if score == Tscore:
		print list
	else:
		print "Error"


if __name__ == '__main__':
	main()



