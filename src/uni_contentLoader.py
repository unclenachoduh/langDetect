import os
import re

def getTestText(fileLocation):
	lines = open(fileLocation).read().split("\n")

	if lines[:-1] == "":
		lines = lines[:-1]

	desired = []

	for line in lines:
		parts = line.split("\t")

		desired.append(parts)

	return desired

def getTrainModels(folderLocation):

	numModels = len(os.listdir(folderLocation))
	smallestcounts = [0] * numModels # list of smallest individual word count per language
	totalcounts = [None] * numModels # list of total number of words counts per language
	vocab = [None] * numModels # list of dictionaries with words + word count per lang
	place = 0 # counter that keeps track of the index for the arrays above

	languages = []

	for file in os.listdir(folderLocation):
		filepath = os.path.join(folderLocation, file)

	# get just the lang code from the file name
		filename = file.split(".")
		code = filename[0]

		languages.append(code)

	# read text from file
		openfile = open(filepath, 'r')
		texts = openfile.read().split("\n")
		openfile.close()

		wordcount = 0 # sum of the counts for all words. Will be added to list of total word counts per lang
		gloss = {} # dictionary of words + counts in a file
		m = 0 # counter to avoid boundary error (last line blank)

		for l in texts:
			if m < len(texts) - 1:

	# separate word from count
				mysplit = l.split("\t")
				word = mysplit[0].lower()

	# add this count to total count for this file
				wordcount += int(mysplit[1])

	# update the smallest individual word count in this file
				if smallestcounts[place] < int(mysplit[1]):
					smallestcounts[place] = int(mysplit[1])

	# add this word to dictionary
				gloss[mysplit[0]] = mysplit[1]

				m += 1

	# Add dictionary to list of dictionaries for all languages
		vocab[place] = gloss

	# add word count to list of word counts for all languages
		totalcounts[place] = wordcount

		place += 1

	return [smallestcounts, totalcounts, vocab, languages]
