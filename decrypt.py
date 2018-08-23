def decrypt_cipher(word, key):
	new_word = ""
	key = first_key % 26
	length_word = len(word)


	for i in range(0,length_word):
  		if ord(word[i]) - key < 97:
  			temp = ord(word[i]) - 97
		    temp1 = key - temp
		    temp2 = 123 - temp1
		    new_word+= str((chr(temp2)))
		else:
			temp3 = ord(word[i]) - key
		    new_word+= str((chr(temp3)))

	return new_word

def main():
	message = input("Please enter a message: ")
	key = input("Please enter a key: ")
	new_message = decrypt_cipher(str(message), int(key))
	print(new_message)

main()
