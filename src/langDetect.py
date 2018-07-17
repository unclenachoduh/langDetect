import sys
import re
import math
from fiveGrams import get_grams
# local imports
from contentLoader import getTestText, getTrainModels

def detect(models, test, outfilename):

	modelData = getTrainModels(models)

	smallestcounts = modelData[0]
	totalcounts = modelData[1]
	vocab = modelData[2]
	languages = modelData[3]

	# input files

	tests = getTestText(test)

	wout = open(outfilename, "w+")

	for parts in tests:

		line = parts[0] + "\t" + parts[1]
		wout.write(line + "\n")

		words = parts[1].lower().split(" ")


		# Todo
		# get n grams

		my_grams = get_grams(parts[1])

		ngrams = [{}, {}, {}, {}, {}] # array of ngram arrays. ind 0 should be characters
		token_group = [[]] * 5

		for gram in my_grams:
			for tup in gram:
				words = []
				for word in tup:
					word = word.lower()
					words.append(word)
					for c in word:
						if c not in ngrams[0]:
							ngrams[0][c] = 1
							token_group[0].append(c)

				merged = "_".join(words)
	            
				if merged not in ngrams[len(words)]:
					ngrams[len(words)][merged] = 1
					token_group[len(words)].append(merged)


		length = len(words) # the number of words in the sentence
		matches = [0] * len(languages) # the number words found in the dictionary per language for this sentence
		wordprobs = [] # all language probabilities for word
		probs = [None] * len(languages) # probability of each lang for a given word. Stored by word in above array

		gram_count = 0
		for words in token_group:
			for word in words:
				count = 0
				while count < len(languages):
					if word != "":
						if word in vocab[count]:

		# if word is a match, set logprob to word count / total count for that language
							probs[count] = math.log10(int(vocab[count][word]) / int(totalcounts[count][gram]))
							matches[count] += 1
						else:

		# if word is not a match, se logprob to 1 count in the dictionary for that language
							probs[count] = math.log10(1 / int(totalcounts[count][gram_count]))

					count += 1

				wordprobs.append(probs)






		count = 0

		finalscore = 1 # will be updated with the total logprob for printing and win checking
		finalname = "XXX" # will be updated with the best score for printing

		weightscores = [0] * len(languages)

	# loops through each language
		while count < len(languages):

			win = False # if this score beats previous, this flags it as current best

			probstomult = [] # for extracting items from matrix-style data structure
	# get probabilities of all words in this sentences for this language
			for word in wordprobs:
				probstomult.append(word[count])

	# Add logprob for each word
			total = 0
			for num in probstomult:
				total += num

			divnum = total / length # reward for each matched word

	# reward the language for each matched word
			total -= (divnum * matches[count])

	# if this score better than previous best, update best
			if finalscore == 1:
				finalscore = total
				win = True
			elif total > finalscore:
				finalscore = total
				win = True

	# print each language score
			wout.write(languages[count] + "\t" + str(total) + "\n")

	# if this language is best score so far, update best
			if win == True:
				finalname = languages[count]

			weightscores[count] = total

			count += 1

		margin = True
		margincount = -1

		weightcount = 0
		while weightcount < len(languages):
			if finalscore-15 <= weightscores[weightcount]:
				margincount += 1
			weightcount += 1

	# print according to threshold for unknown languages
		if margincount > 2:
			wout.write("result \tunk\n")
		elif finalscore < -95:
			wout.write("result \tunk\n")
		else:
			wout.write("result\t" + finalname + "\n")


if __name__ == "__main__":
	detect(sys.argv[1],sys.argv[2],sys.argv[3])