import random
import math


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
	

def all_combinations_of_letters(letters):
	list_of_combinations = []
	while True:
		combination = random_list(letters)
		word = list_to_word(combination)
		length = len(letters) - len(set(letters)) + 1
		if word not in list_of_combinations:
			list_of_combinations.append(word)
		if len(list_of_combinations) == math.factorial(len(combination)) / math.factorial(length):
			break
		print(length)
	return list_of_combinations


comb = all_combinations_of_letters(input())
print(*comb)


