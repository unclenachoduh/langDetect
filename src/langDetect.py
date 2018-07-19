import sys
import ngram, unigram

if __name__ == "__main__":

	if len(sys.argv) == 2 and sys.argv[1] == "test":
		print("\n+------ ::Test System:: ------+")
		print("|                             |")

		utest = "resources/uni_sample_test.txt"
		umodel = "resources/unigram_models/"
		uout = "output/unigram_output.txt"

		unigram.detect(umodel, utest, uout)

		print("| > Unigram test complete.    |")
		print("|                             |")

		ntest = "resources/sample_test.txt"
		nmodel = "resources/ngram_models/"
		nout = "output/ngram_output.txt"

		ngram.detect(nmodel, ntest, nout)

		print("| > Ngram test complete.      |")
		print("|                             |")
		print("+-----------------------------+\n")

	elif len(sys.argv) == 4:
		print("\n+------ langDetect ------+")
		print("|                        |")

		ngram.detect(
			sys.argv[1], 
			sys.argv[2], 
			sys.argv[3])

		print("| > Ngram test complete. |")
		print("|                        |")
		print("+------------------------+\n")

	elif len(sys.argv) == 5 and sys.argv[4] == "NB":
		print("\n+----- Unigram langDetect ----+")
		print("|                             |")

		unigram.detect(
			sys.argv[1], 
			sys.argv[2], 
			sys.argv[3])

		print("| > Unigram test complete.    |")
		print("|                             |")
		print("+-----------------------------+\n")

	else:
		print("\nERROR:Problem with command args. See README or use format \'python3 src/langDetect.py <model> <input> <output>\'\n")