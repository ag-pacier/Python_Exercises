#! python
#Poetry.py
#poetry exercise from talkpython beginner's book

#importing random to allow me to use random.choice() to pick words
import random

#Lists to pull words from. Must have enough unique matches to fill out poem
noun_list = ["fossil", "jewel", "computer", "Python", "phone", "corn"]
verb_list = ["licks", "dances", "tastes", "jiggles", "chews"]
adjective_list = ["glistening", "furry", "giddy", "randy"]
preposition_list = ["into", "within", "over", "against", "for", "in", "behind"]
adverb_list = ["tantalizingly", "curiously", "confidently"]

#Lists I'd rather you didn't change to make the poem grammatically correct
start_list = ["a", "an"]
the_vowel = ["a","e","i","o","u"]

#Empty lists the poem will be built from
adjective = []
noun = []
verb = []
preposition = []
adverb = []

def set_start(word):
	"""Takes a word and inspects the first letter to see if it's a vowel.
		if it is, set the proceeding A/AN to an. Otherwise, it's just a."""
	if word[0].lower() in the_vowel:
		return start_list[1]
	else:
		return start_list[0]

def make_choice(list, word_list):
	""" Randomly selects from a list of available words to populate the word lists.
		Checks to make sure the second list doesn't already have the word before
		returning the choice."""
	choice = random.choice(list)
	while choice in word_list:
		choice = random.choice(list)
	return choice

def make_poem(adj, no, ver, prep, adv):
	"""Spit out a collection of words using adjective, noun, verb, preposition
		and adverb lists. Only populates the lists, it does not print or format
		the list.

		Accepts number of adjectives, nouns, verbs, prepositions and adverbs"""
	for i in range(adj):
		adjective.append(make_choice(adjective_list, adjective))
	for i in range(no):
		noun.append(make_choice(noun_list, noun))
	for i in range(ver):
		verb.append(make_choice(verb_list, verb))
	for i in range(prep):
		preposition.append(make_choice(preposition_list, preposition))
	for i in range(adv):
		adverb.append(make_choice(adverb_list, adverb))

make_poem(3, 3, 3, 2, 1)
print(f"{set_start(adjective[0])} {adjective[0]} {noun[0]}")
print(f"{set_start(adjective[0])} {adjective[0]} {noun[0]} {verb[0]} {preposition[0]} the {adjective[1]} {noun[1]}")
print(f"{adverb[0]}, the {noun[0]} {verb[1]}")
print(f"the {noun[1]} {verb[2]} {preposition[1]} {set_start(adjective[2])} {adjective[2]} {noun[2]}")