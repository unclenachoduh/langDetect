import sys, os, operator
from nltk import word_tokenize

folderLocation = sys.argv[1]

for file in os.listdir(folderLocation):
	
	word_counts = {}

	filepath = os.path.join(folderLocation, file)

	myFile = open(filepath).read()

	tokens = word_tokenize(myFile)

	for token in tokens:
		if token.isupper() or token.islower():
			if token in word_counts:
				word_counts[token] += 1
			else:
				word_counts[token] = 1
	unigrams = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)

	wout = open(sys.argv[2] + file, "w+")

	for gram in unigrams:
		wout.write(gram[0] + "\t" + str(gram[1]) + "\n")
