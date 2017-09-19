#!/usr/bin/python

#PANAGRAM

def is_panagram(word):
	count = 0
	alphabets="abcdefghijklmnopqrstuvwxyz"
	phrase=""
	for char in word:
		for letter in alphabets:
			if char == letter and char not in phrase:
				phrase += char
	for char in phrase:
		for letter in alphabets:
			if char == letter:
				count = count + 1

	if count == 26:
		print count
		print "Word is Panagram!"
	else:
		print "Word is Not a Panagram"
		print count
	return 

def main():
	word = raw_input("Enter a word : ")
	is_panagram(word)
	return 

if __name__ == '__main__':
	main()