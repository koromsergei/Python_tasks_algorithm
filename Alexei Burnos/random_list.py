import random


def random_list(letters):
	
	used_letters = []
	listed_letters = list(letters)
	
	start_letters = listed_letters
	
	while True:
		letter = random.choice(listed_letters)
		listed_letters.remove(letter)
		used_letters.append(letter)
		if len(used_letters) == len(list(map(len, letters))):
			break
		used_letters = list(used_letters)
	
	return used_letters
	
	

def list_to_word(list_):
	word = ''
	i = 0
	while True:
		word = word + list_[i]
		i += 1
		if len(list(map(len, word))) == len(list_):
			break
	return word
	
	
a = input()
b = random_list(a)
print(b)
print(list_to_word(b))

