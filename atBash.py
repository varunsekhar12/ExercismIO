#!/use/bin/python

#AT_BASH CIPHER

def atbash_encode(word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	cipher = "zyxwvutsrqponmlkjihgfedcba"
	encoded = ""
	for char in word:
		for letter1,letter2 in zip(alphabet,cipher):
			if char == letter1:
				encoded += letter2
	print "THE ENCODED TEXT :  %s "%(encoded)
	atbash_decode(encoded)
	return 

def atbash_decode(word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	cipher = "zyxwvutsrqponmlkjihgfedcba"
	decoded = ""
	for char in word:
		for letter1,letter2 in zip(alphabet,cipher):
			if char == letter2:
				decoded += letter1
	print "THE DECODED TEXT :  %s "%(decoded)
	return 

def main():
	word = raw_input("Enter the Text : ")
	atbash_encode(word)
	return 

if __name__ == '__main__':
		main()	