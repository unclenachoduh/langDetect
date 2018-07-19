# LangDetect

A simple language detection system.

By: Uncle Nacho, duh.

## System Description

This system guesses the language of a string based on its superficial characteristics (AKA, words). There are two implementations: Naïve Bayes and N-grams. The N-grams implementation is generally more performant.

### N-gram-oriented Classifier

This implementation counts the number of n-grams from the input that are seen in the model. This includes characters and n-grams from size one to four. It is possible that increasing the n-gram size _could_ increase system performance, but these increases are likely marginal. 

The count for each N-gram is multiplied by ten times the number of it's size plus one. Characters are weighted by 1, unigrams by 11, bigrams by 21, etc.

If the best scoring language does not beat the next best score by a margin of 25% or the next best three scores by a margin of 30%, then the result "unknown" is returned.

### Naïve Bayessian Language Classifier

This implementation uses only unigrams for classification. Token probability is generated from training data in the form of a unigram count language model and those probabilities are applied to each word in the input sentence for each language model available. The language whose model scores the highest probability is selected, given it beats other languages by a large enough margin.

If the best scoring language doesn't beat other languages by a large enough margin, the guess is "unknown". This system is reliable and leans towars false negatives rather than false positives. 

**System Limitations**

This system is built to return more false negatives than false positives. If language models are unequal in size and quality, this implementation will struggle to return accurate results, as opposed to the N-gram implementation, which is generally performant within reason.

On an unseen dataset, the system encountered some encoding errors. Some encoding expertise is needed to ensure processing.

## Running The System

To run the N-gram system, in the `root` directory, run:

`python3 src/langDetect.py <train_data_folder> <input_file> <output_file>`

The `train_data_folder` should have at least one text file with a unigram language model. The name of each language model file will be used as the language name in the output.

To run the Naïve Bayes version of the system, include the argument `NB`:

`python3 src/langDetect.py <train_data_folder> <input_file> <output_file> uni`

The code should execute and terminate quickly.

## Input

The main script `langDetect.py` processes a Python list of strings to identify. It accepts a list where for each index, there is a list with an identifier in index 0 and the string in index 1. A text file with "<identifier>\t<string>" on each line will process correctly. If you with to format your file differently, you will need to make adjustments to the code.

## Output

- Input text
- Scores for each language
- Identified Language *

_\* If the language with the best score does not win by a large enough margin, a result of "unknown" is returned in order to avoid incorrect guesses._

## Sample Tests

You can test the system with the command:

`python3 src/langDetect.py test`

This will test both the Naïve Bayes and N-gram system and write the output to the `output/` directory.

## Precision / Recall

### N-gram

100% precision and recall. 🎉

### Naïve Bayes

**Sample Test Set**

| | Occurrences out of 10 | Performance |
| - | ------------------- | ----------- |
| Correct Results | 9 | 90% |
| False Positives | 0 | 100% |
| False Negatives | 1 | 90% |
| Incorrect Positives | 0 | 100% |
| Average Performance | - | 95% |

**Unseen Test Set**

| | Occurrences out of 15 | Performance |
| - | ------------------- | ----------- |
| Correct Results | 14 | 93.3% |
| False Positives | 0 | 100% |
| False Negatives | 1 | 93.3% |
| Incorrect Positives | 0 | 100% |
| Average Performance | - | 96.7% |

## Sample data

Sample data was created by generating unigram and n-gram files from raw Wikipedia articles about dogs.

Those language models should not be used for practical purposes outside of being a sample here. If you do use them, however, that use should be guided by Wikipedia license. 

**Generating Unigram Language Models**

I have included the short scripts I used to generate the Wikipedia unigram and n-gram models in `src/unigramGetter.py` and `src/ngramGetter.py`.

From the `root` directory, run:

`python3 src/unigramGetter.py <raw_text_folder> <output_folder>`

`python3 src/ngramGetter.py <raw_text_folder> <output_folder>`

For all raw text files in the source folder, it will create an n-gram count model with the same name in the output folder.
