def encrypt_cipher(word, key):
	first_key = key
	new_key = first_key % 26
	encrypt_str = ''
	for i in range(0,len(word)):
		encrypted = ord(word[i])
		if encrypted + (key) > ord('z'):
			temp = ord('z') - encrypted
			temp1 = (key - temp)
			temp2 = 96 + temp1
			encrypted = temp2
		
		if encrypted >= 32 and encrypted <= 47:
			pass

		elif encrypted >= 58 and encrypted <= 64:
			pass

		elif encrypted >= 91 and encrypted <= 47:
			pass

		else:
			encrypted = encrypted + (key)
		encrypt_str += chr(encrypted)
	return encrypt_str

def main():
	message = input("Please enter a message: ")
	key = input("Please enter a key: ")
	new_message = encrypt_cipher(str(message), int(key))
	print(new_message)

main()
