def decrypt_cipher(word, key):
	length_word = len(word)
	for i in length_word:
		if ord(word[i]) - key < 97:
			temp = ord(word[i]) - 97
			temp1 = key - temp
			temp2 = 122 - temp1
			ord(word[i]) = temp2
		else:
			ord(word[i]) = ord(word[i]) - key

	return word
