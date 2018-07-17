import sys, os, operator
from nltk.tokenize import word_tokenize
import fiveGrams

folderLocation = sys.argv[1]
output = sys.argv[2]

if output[-1] != "/":
    output += "/"


for file in os.listdir(folderLocation):

    # word_counts = {}

    filepath = os.path.join(folderLocation, file)

    myFile = open(filepath).read()

    grams = fiveGrams.get_grams(myFile)

    ngrams = [{}, {}, {}, {}, {}] # array of ngram arrays. ind 0 should be characters
    token_group = []

    for gram in grams:
        for tup in gram:
            words = []
            for word in tup:
                word = word.lower()
                words.append(word)
                for c in word:
                    if c not in ngrams[0]:
                        ngrams[0][c] = 1
                    else:
                        ngrams[0][c] += 1

            merged = "_".join(words)
            
            if merged not in ngrams[len(words)]:
                ngrams[len(words)][merged] = 1
            else:
                ngrams[len(words)][merged] += 1


    for group in ngrams:
        data = sorted(group.items(), key=operator.itemgetter(1), reverse=True)
        token_group.append(data)

    wout = open(output + file, "w+")

    count = 0
    for tg in token_group:
        if count > 0:
            wout.write("\n")

        wout.write("// GRAM-" + str(count) + "\n\n")
        for pair in tg:
            wout.write(pair[0] + "\t" + str(pair[1]) + "\n")
        count += 1



    # for tokens in token_group:
    #     for token in tokens: 
    #         if token in word_counts:
    #             word_counts[token] += 1
    #         else:
    #             word_counts[token] = 1

    # wout = open(sys.argv[2] + file, "w+")

    # for gram in unigrams:
    #     wout.write(gram[0] + "\t" + str(gram[1]) + "\n")
