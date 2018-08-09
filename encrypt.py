def encrypt_cipher(word, key):
	first_key = key
	new_key = first_key % 26
	for i in range(0,len(word)):
		encrypted = ord(word[i])
		if encrypted + (key) > ord('z'):
	    temp = ord('z') - encrypted
	    temp1 = (key - temp)
	    temp2 = 96 + temp1
	    encrypted = temp2
	else:
    	encrypted = encrypted + (key)
	print(chr(encrypted))
