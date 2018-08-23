word = "hello"
new_word = ""
first_key = 257
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

print(new_word)

def decrypt(word, first_key):
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

