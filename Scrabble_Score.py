#!/use/bin/python

#Scrabble Score

def scrabble_score(word):
	val1 = "AEIOULNRST"
	val2 = "DG"
	val3 = "BCMP"
	val4 = "FHVWY"
	val5 = "K"
	val8 = "JX"
	val10 = "QZ"
	score = 0
	word = word.upper()
	print word
	for char in word:
		if char in val1:
			score = score + 1
		if char in val2:
			score = score + 2
		if char in val3:
			score = score + 3
		if char in val4:
			score = score + 4
		if char in val5:
			score = score + 5
		if char in val8:
			score = score + 8
		if char in val10:
			score = score + 10
	print "The Score is : ",score
	return 

def main():
	word = raw_input("Enter a word: ")
	scrabble_score(word)
	return

if __name__ == '__main__':
	main()

