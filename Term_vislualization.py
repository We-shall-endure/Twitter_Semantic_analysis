#Original Code by Marco Bonzanini
#All edits by Bassam Salim
#this code needs Wordcounter1 to execute as well as the proper HTML skeleton
#Outputs a Barchart of frequecny of words for a given twitter handle

import vincent
#import Word_counter_with_co_occurence as wcc
from collections import Counter
import Word_counter1 as wc

terms=wc.counted_words()
word_freq = terms.most_common(30)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')