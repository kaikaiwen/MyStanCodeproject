"""
File: boggle.py
Name: Kevin Chen
----------------------------------------
boggle game ?!:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


class TrieNode:
	def __init__(self):
		self.children = {}
		self.end = False

	def print_trie(self, prefix=''):
		if self.end:
			print(prefix)
		for char, child in self.children.items():
			child.print_trie(prefix + char)


class Trie:
	def __init__(self):
		self.ds = TrieNode()

	def insert(self, word):
		cur = self.ds
		for char in word:
			if char in cur.children:
				cur = cur.children[char]
			else:
				cur.children[char] = TrieNode()
				cur = cur.children[char]
		cur.end = True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	alphabet = Trie()

	with open(FILE, 'r') as f:                     # 1. Read the file.
		for word in f:                             # 2. Read the contents.
			word = word.strip()                    # 3. Remove the newline (\n).
			if len(word) >= 4:                     # Ⅰ. word length should more than 4 and word
				alphabet.insert(word)              # 4. Append the word to the list.
	return alphabet


def find_word(row_letters, trie):
	"""
	:param row_letters:the 16 letters we typed
	:param trie: Turn a word in a dictionary into a trie
	:return: Words that can be found from the 16 letters we typed
	"""
	result = []
	rows = len(row_letters)
	col = len(row_letters[0])
	used = [[False] * col for _ in range(rows)]
	for i in range(rows):
		for j in range(col):
			dfs(trie.ds, '', i, j, row_letters, result, used)
	return result


def dfs(node, word, row, col, board, result, used):
	char = board[row][col]

	if char not in node.children:
		return

	node = node.children[char]
	word += char

	if node.end:
		result.append(word)
		node.end = False

	used[row][col] = True

	rows = len(board)
	cols = len(board[0])
	for i in range(row - 1, row + 2):                 # letters near each letter
		for j in range(col - 1, col + 2):
			if 0 <= i < rows and 0 <= j < cols and not used[i][j]:
				dfs(node, word, i, j, board, result, used)

	word = word[:-1]
	used[row][col] = False


def main():
	"""
	Boggle Game
	"""
	start = time.time()
	###################
	row_letters = []
	for i in range(4):
		row = input(f'{i+1} row of letter: ').strip().split(' ')

		if len(row) != 4:
			print("Illegal input")
			return
		for letter in row:
			if len(letter) != 1 or not letter.isalpha():
				print("Illegal input")
				return
		row_letters.append(row)

	trie = read_dictionary()

	result = find_word(row_letters, trie)

	for word in result:
		print(f"Found'{word}'")
	print(f"There are {len(result)} words in total.")

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


if __name__ == '__main__':
	main()
