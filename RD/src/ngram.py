import sys
import re
import math
from fiveGrams import get_grams
# local imports
from contentLoader import getTestText, getTrainModels

def detect(models, test, outfilename):

	modelData = getTrainModels(models)

	smallestcounts = modelData[0]
	# print("SMALLCOUNT:", smallestcounts)
	totalcounts = modelData[1]
	# print("TOTAL:", totalcounts)
	vocab = modelData[2]
	# print("VOCAB:", vocab)
	languages = modelData[3]
	# print("LANGS:", languages)

	# input files

	tests = getTestText(test)

	wout = open(outfilename, "w+")

	for input_line in tests:
		# print(input_line)

		line = input_line[0] + "\t" + input_line[1]
		wout.write(line + "\n")

		# print(line)

		words = input_line[1].lower().split(" ")


		# Todo
		# get n grams

		my_grams = get_grams(input_line[1])

		ngrams = [[], [], [], [], []]

# Add characters to ngrams list
		for c in input_line:
			# print("C", c)
			if c != " ":
				ngrams[0].append(c.lower())

# Add ngrams to ngrams list
		for gram in my_grams:
			for tup in gram:
				# print("TUP", tup)
				words = []
				for word in tup:
					# print("WORD", word)
					word = word.lower()
					words.append(word)

				merged = "_".join(words)
	            
				# print(len(words))
				# print("MERGED", merged)

				ngrams[len(words)].append(merged)

		scores = []

		lang_count = 0
		for lang in languages:
			# count = 0
			# print(lang)

			scores_ngram = [0, 0, 0, 0, 0]
			# matches = [0, 0, 0, 0, 0]
			matches = [0, 0, 0, 0, 0] # number of tokens that match the language model
			all_matches = [0, 0, 0, 0, 0] # total number of tokens try for match

			ngram_count = 0
			for tokens in ngrams:
				# print(count, tokens, "\n")
				# count += 1

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

			# print(lang, great_score)
			wout.write(lang + "\t\t" + str(great_score) + "\n")

			scores.append(great_score)

			lang_count += 1

		within_30 = []
		next_best_score = 0
		best_score = max(scores)
		# print("MAX ---------", best_score)
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
			# print("WINNER:", best_lang, best_score * 0.75, next_best_score, len(within_30), "\n")
			# print("\nWINNER:", best_lang, "\n")
			wout.write("\nresult: \t" + best_lang + "\n\n")
			# print(best_score - (best_score/3), next_best_score)
		else:
			# print("WINNER: unk", "UNKOWN", best_score * 0.75, next_best_score, len(within_30), "\n")
			# print("\nWINNER: unk", "\n")
			wout.write("\nresult: \tunk\n\n")
			# print(best_score - (best_score/3), next_best_score)





if __name__ == "__main__":
	detect(sys.argv[1],sys.argv[2],sys.argv[3])