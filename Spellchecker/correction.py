from spellchecker import SpellChecker
 
spell = SpellChecker()
spell.split_words("this sentnce has misspelled werds")
words = spell.split_words("this sentnce has misspelled werds")

for i in words:
	print(spell.correction(i))
	print(spell.candidates(i))