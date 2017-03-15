import operator
import json
from collections import Counter
import Tweet_processing_func as tp
from nltk.corpus import stopwords
import string
from collections import defaultdict

# com[x][y] contains the number of times the term x has been seen in the same tweet as the term y
com = defaultdict(lambda: defaultdict(int))  # creates a dictionary where the entry for each ey is a dictionary

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'via', '...', '.', '*']
fname = 'python.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        try:
            tweet = json.loads(line)  # Create a list with all the terms
            terms_only = [term for term in tp.preprocess(tweet['text']) if
                          term not in stop and not term.startswith(('@', '#'))]
            count_all.update(terms_only)  # Update the counter


        except ValueError:  # print(tweet['text'])
            var1 = 1
            # i=i+1
            # print(i)

        # Build co-occurrence matrix
        for i in range(len(terms_only) - 1):
            for j in range(i + 1, len(terms_only)):
                w1, w2 = sorted([terms_only[i], terms_only[j]])
                if w1 != w2:
                    com[w1][w2] += 1

com_max = []
#For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:30])



#Print the first 5 most frequent words
#print(count_all.most_common(30))
