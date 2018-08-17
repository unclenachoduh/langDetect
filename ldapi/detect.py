import sys
import re
import math
from fiveGrams import get_grams
# local imports
from contentLoader import getTestText, getTrainModels

def detect(modelData, input_line):

	smallestcounts = modelData[0]
	totalcounts = modelData[1]
	vocab = modelData[2]
	languages = modelData[3]

	words = input_line.lower().split(" ")

	my_grams = get_grams(input_line)

	ngrams = [[], [], [], [], []]

# Add characters to ngrams list
	for c in input_line:
		if c != " ":
			ngrams[0].append(c.lower())

# Add ngrams to ngrams list
	for gram in my_grams:
		for tup in gram:
			words = []
			for word in tup:
				word = word.lower()
				words.append(word)

			merged = "_".join(words)

			ngrams[len(words)].append(merged)

	scores = []

	lang_count = 0
	for lang in languages:

		scores_ngram = [0, 0, 0, 0, 0]
		matches = [0, 0, 0, 0, 0] # number of tokens that match the language model
		all_matches = [0, 0, 0, 0, 0] # total number of tokens try for match

		ngram_count = 0
		for tokens in ngrams:

			all_matches[ngram_count] = len(tokens)

			for token in tokens:

				if token in vocab[lang_count][ngram_count]:
					matches[ngram_count] += 1

			ngram_count += 1

		great_score = 0

		score_count = 0
		for score in scores_ngram:
			great_score += matches[score_count] * ((score_count * 10) + 1)
			score_count += 1

		print(lang + "\t\t" + str(great_score))

		scores.append(great_score)

		lang_count += 1

	within_30 = []
	next_best_score = 0
	best_score = max(scores)
	best_lang = "unk"
	final_counter = 0
	for score in scores:
		if score == best_score:
			best_lang = languages[final_counter]
		else:
			if score > best_score * 0.70:
				within_30.append(score)
		
			if score > next_best_score:
				next_best_score = score

		final_counter += 1

	if best_score * 0.75 > next_best_score and len(within_30) < 3:
		return(best_lang)
	else:
		return("unk")




if __name__ == "__main__":
	modelData = getTrainModels(sys.argv[1])

	tests = getTestText(sys.argv[2])

	output = sys.argv[3]

	for text in tests:
		print(text[1])
		result = detect(modelData, text[1])
		print("\nTRUE\t:\tRESULT")
		print(text[0] + " : " + result + "\n")