#!/usr/bin/python

#Caesar Cipher

def caesar(word, key): 
  encoded = ""
  for ch in word:
    if ch.isalpha():
      alphabet = ord(ch) + key 
      if alphabet > ord('z'):
        alphabet -= 26
      letter = chr(alphabet)
      encoded += letter
  print "Your ciphertext is: ", encoded
  return

def main():
	word = raw_input("Enter the Text : ")
	key = int(raw_input("Enter the Key : "))
	caesar(word,key)
	return 

if __name__ == '__main__':
		main()	