#Original Code by Marco Bonzanini
#All edits by Bassam Salim
#this code needs Tweet_processing func to execute
#Currently only counts words with hashtages, can be simplified to count words in general
import operator
import json
from collections import Counter
import Tweet_processing_func as tp #need so that we can call preprocess to "tokenize" tweets
from nltk.corpus import stopwords
import string
from nltk import bigrams



def counted_words():
    count_all = Counter()
    count_all_master = Counter()
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['rt', 'via', '...', '.', '*', '@realDonaldTrump']
    fnames = ['realdonaldtrump_RR_02_20.json', 'realdonaldtrump_RR_02_24.json', 'realdonaldtrump_BSC_2_28.json']

    for fname in fnames:

        with open(fname, 'r') as f:

            for line in f:
                try:
                    # print(line)
                    tweet = json.loads(line)

                    # Create a list with all the terms
                    terms_all = [term for term in tp.preprocess(tweet['text'])]

                    # With stop-word removal
                    terms_stop = [term for term in tp.preprocess(tweet['text']) if term not in stop]

                    # The bigrams() function from NLTK will take a list of tokens and produce a list of tuples using adjacent tokens.
                    terms_bigram = bigrams(terms_stop)

                    # Count terms only once, equivalent to Document Frequency
                    terms_single = set(terms_all)

                    # Count hashtags only
                    terms_hash = [term for term in tp.preprocess(tweet['text'])
                                  if term.startswith('#')]

                    # Count terms only (no hashtags, no mentions)
                    terms_only = [term for term in tp.preprocess(tweet['text'])
                                  if term not in stop and
                                  not term.startswith(('#', '@'))]
                    # mind the ((double brackets))
                    # startswith() takes a tuple (not a list) if
                    # we pass a list of inputs

                    # Update the counter
                    count_all.update(terms_hash)

                except ValueError:  # print(tweet['text'])
                    var1 = 1
        count_all_master.update(count_all)
    return count_all_master


#countall = counted_words()
#print(countall.most_common(20))
# Print the first 5 most frequent words
# print(count_all.most_common(15))
