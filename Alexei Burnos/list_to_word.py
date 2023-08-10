def list_to_word(list):
	word = ''
	i = 0
	while True:
		if list == []:
			break
		else:
			word = word + list[i]
			list.remove(list[i])
			i += 1
	return word
	


