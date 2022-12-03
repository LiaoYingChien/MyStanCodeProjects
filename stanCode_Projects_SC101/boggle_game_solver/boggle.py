"""
File: boggle.py
Name: Norah Liao
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	ds = {}
	index_lst = []
	for i in range(1, 5):
		letters_1 = input(str(i) + " row of letters:")
		if len(letters_1) < 7:
			print("Illegal input")
			return
		else:
			# letters_1 = letters_1[:7]
			j = 1
			for letter in letters_1.split():
				if len(letter) > 1:
					print("Illegal input")
					return
				else:
					ds[(i, j)] = letter
					index_lst.append((i, j))
					j += 1

	find_anagrams(ds, index_lst)

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagrams(ds, curr_lst):
	dictionary = read_dictionary(ds)
	found_num = 0
	for key in list(ds.keys()):
		value = ds[key]
		curr_lst.remove(key)
		found_num = find_anagrams_helper(ds, key, dictionary, value, curr_lst, found_num, [])
		curr_lst.append(key)
	print(f'There are {found_num} word in total')


def find_anagrams_helper(ds, key, dic, curr_word, curr_lst, found_num, ans_lst):
	if len(curr_lst) == 0:
		print("Base Case")
		pass
	else:
		if key[0] == 1:
			row_top = key[0]
			row_down = key[0]+1
		elif key[0] == 4:
			row_top = key[0]-1
			row_down = key[0]
		else:
			row_top = key[0]-1
			row_down = key[0]+1

		if key[1] == 1:
			col_top = key[1]
			col_down = key[1]+1
		elif key[1] == 4:
			col_top = key[1]-1
			col_down = key[1]
		else:
			col_top = key[1]-1
			col_down = key[1]+1

		for i in range(row_top, row_down+1):
			for j in range(col_top, col_down+1):

				if (i, j) in curr_lst:
					# Choose
					curr_word += ds[(i, j)]
					curr_lst.remove((i, j))

					# Explore
					if has_prefix(curr_word, dic):
						if len(curr_word) >= 4 and curr_word not in ans_lst and curr_word in dic[curr_word[0]]:
							print(f'Found "{curr_word}"')
							ans_lst.append(curr_word)
							found_num += 1

						found_num = find_anagrams_helper(ds, (i, j), dic, curr_word, curr_lst, found_num, ans_lst)

					# Un-choose
					curr_word = curr_word[:-1]
					curr_lst.append((i, j))

	return found_num


def read_dictionary(target_ds):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = {}
	with open(FILE, "r") as f:
		for word in f:
			word = word.strip()
			if len(word) >= 4 and (word[0] in target_ds.values()):
				if word[0] in dic:
					dic[word[0]].append(word)
				else:
					dic[word[0]] = [word]
	return dic


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (dic) dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
