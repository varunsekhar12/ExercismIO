#!/usr/bin/python

#ISOGRAM

def is_isogram(word):
	size = 0
	alphabets="abcdefghijklmnopqrstuvwxyz"
	phrase=""
	for char in word:
		for letter in alphabets:
			if char == letter and char not in phrase:
				phrase += char
	if(word == phrase):
		print "Word is an Isogram!"
	else:
		print "Word is not an Isogram!"
	return 

def main():
	word = raw_input("Enter a word : ")
	is_isogram(word)
	return 

if __name__ == '__main__':
	main()