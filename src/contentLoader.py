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
	smallestcounts = [[0, 0, 0, 0, 0]] * numModels # list of smallest individual word count per language
	totalcounts = [[None, None, None, None, None]] * numModels # list of total number of words counts per language
	vocab = [[None, None, None, None, None]] * numModels # list of dictionaries with words + word count per lang
	place = 0 # counter that keeps track of the index for the arrays above
	nplace = 0 # count for the ngram 

	languages = []

	for file in os.listdir(folderLocation):
		nplace = 0

		filepath = os.path.join(folderLocation, file)

	# get just the lang code from the file name
		filename = file.split(".")
		code = filename[0]

		languages.append(code)

	# read text from file
		openfile = open(filepath, 'r')
		texts = openfile.read().split("\n")
		openfile.close()

		wordcount = [0] * 5 # sum of the counts for all words. Will be added to list of total word counts per lang
		gloss = [{}] * 5 # List of dictionary of words + counts in a file
		m = 0 # counter to avoid boundary error (last line blank)\


		for l in texts:
			if l != "":
				checkhead = l.split("-")

				if checkhead[0] == "// GRAM":
					if checkhead[1] == "0":
						nplace = 0
					elif checkhead[1] == "1":
						nplace = 1
					elif checkhead[1] == "2":
						nplace = 2
					elif checkhead[1] == "3":
						nplace = 3
					elif checkhead[1] == "4":
						nplace = 4
					elif checkhead[1] == "5":
						nplace = 5
					else:
						print("PROBLEM")

				else:
					mysplit = l.split("\t")
			# separate word from count
					word = mysplit[0].lower()

			# add this count to total count for this file
					# print(mysplit)
					wordcount[nplace] += int(mysplit[1])

			# update the smallest individual word count in this file
					if smallestcounts[place][nplace] < int(mysplit[1]):
						smallestcounts[place][nplace] = int(mysplit[1])

			# add this word to dictionary
					gloss[nplace][mysplit[0]] = mysplit[1]

					m += 1

	# Add dictionary to list of dictionaries for all languages
		vocab[place] = gloss

	# add word count to list of word counts for all languages
		totalcounts[place] = wordcount

		place += 1

	return [smallestcounts, totalcounts, vocab, languages]
