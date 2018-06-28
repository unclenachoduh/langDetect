# LangDetect: Naïve Bayesian Language Classifier

By: Uncle Nacho, duh.

## System Description

This system guesses the language of a string based on the unigrams in the string. Token probability is generated from training data in the form of a unigram count language model and those probabilities are applied to each word in the input sentence for each language model available. The language whose model scores the highest probability is selected, given it beats other languages by a large enough margin.

If the best scoring language doesn't beat other languages by a large enough margin, the guess is "unknown". This system is reliable and leans towars false negatives rather than false positives. 

**Future System Improvements**

The system could be improved by including n-gram and character-level training beyond the current unigram model. N-gram training models would likely improve the system accuracy, and character-level training could make the system work for languages with character systems and word-level syntax that varies from the developer's native language (English).

On an unseen dataset, the system encountered some encoding errors. Some encoding expertise is needed to ensure processing.

## Running The System

In the `root` directory, run:

`python3 langDetect.py <train_data_folder> <input_file> <output_file>`

The `train_data_folder` should have at least one text file with a unigram language model. The name of each language model file will be used as the language name in the output. 

The code should execute and terminate quickly.

## Input

The main script `langDetect.py` processes a Python list of strings to identify. It accepts a list where for each index, there is a list with an identifier in index 0 and the string in index 1. A text file with "<identifier>\t<string>" on each line will process correctly. If you with to format your file differently, you will need to make adjustments to the code.

## Output

- Input text
- Scores for each language
- Identified Language *

_\* If the language with the best score does not win by a large enough margin, a result of "unknown" is returned in order to avoid incorrect guesses._

## Precision / Recall

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

Sample data was created by generating a unigram file from raw Wikipedia articles about dogs.

Those language models should not be used for practical purposes outside of being a sample here. If you do use them, however, that use should be guided by Wikipedia license. 

**Generating Unigram Language Models**

I have included the short script I used to generate the Wikipedia unigram models in `src/unigramGetter.py`.

From the `root` directory, run:

`python3 src/unigramGetter.py <raw_text_folder> <output_folder>`

For all raw text files in the source folder, it will create a unigram count model with the same name in the output folder.
