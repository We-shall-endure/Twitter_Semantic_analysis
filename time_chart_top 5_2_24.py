import pandas
import json
import Tweet_processing_func as tp
import vincent
import Word_counter1 as wc
dates_CPAC = []
dates_Fakenews=[]
dates_TheResistance=[]
dates_Trumptrain=[]
dates_FridayFeeling=[]
# f is the file pointer to the JSON data set
fname = 'realdonaldtrump_RR_02_24.json'


with open(fname, 'r') as f:
    for line in f:
        try:
            tweet = json.loads(line)
            # let's focus on hashtags only at the moment
            terms_hash = [term for term in tp.preprocess(tweet['text']) if term.startswith('#')]
            # track when the hashtag is mentioned
            if '#CPAC' in terms_hash:
                dates_CPAC.append(tweet['created_at'])
            if '#Fakenews' in terms_hash:
                dates_Fakenews.append(tweet['created_at'])
            if '#TheResistance' in terms_hash:
                dates_TheResistance.append(tweet['created_at'])
            if '#TrumpTrain' in terms_hash:
                dates_Trumptrain.append(tweet['created_at'])
            if '#FridayFeeling' in terms_hash:
                dates_FridayFeeling.append(tweet['created_at'])
        except ValueError:  # print(tweet['text'])
            print("ouch")

# a list of "1" to count the hashtags
ones = [1] * len(dates_CPAC)
# the index of the series
idx = pandas.DatetimeIndex(dates_CPAC)
# the actual series (at series of 1s for the moment)
CPAC = pandas.Series(ones, index=idx)

ones = [1] * len(dates_Fakenews)
# the index of the series
idx = pandas.DatetimeIndex(dates_Fakenews)
# the actual series (at series of 1s for the moment)
Fakenews = pandas.Series(ones, index=idx)

ones = [1] * len(dates_TheResistance)
# the index of the series
idx = pandas.DatetimeIndex(dates_TheResistance)
# the actual series (at series of 1s for the moment)
TheResistance = pandas.Series(ones, index=idx)

ones = [1] * len(dates_Trumptrain)
# the index of the series
idx = pandas.DatetimeIndex(dates_Trumptrain)
# the actual series (at series of 1s for the moment)
Trumptrain = pandas.Series(ones, index=idx)

ones = [1] * len(dates_FridayFeeling)
# the index of the series
idx = pandas.DatetimeIndex(dates_FridayFeeling)
# the actual series (at series of 1s for the moment)
FridayFeeling= pandas.Series(ones, index=idx)

# Resampling / bucketing
per_minute_i= CPAC.resample('1Min', how='sum').fillna(0)
per_minute_j= Fakenews.resample('1Min', how='sum').fillna(0)
per_minute_k= TheResistance.resample('1Min', how='sum').fillna(0)
per_minute_l= Trumptrain.resample('1Min', how='sum').fillna(0)
per_minute_m= FridayFeeling.resample('1Min', how='sum').fillna(0)
#all the data together
term_data=dict(CPAC=per_minute_i, Fakenews=per_minute_j,TheResistance=per_minute_k,Trumptrain=per_minute_l, FridayFeeling=per_minute_m )
#Set up data frame
all_terms=pandas.DataFrame(data=term_data,index=per_minute_i.index)

#resample "all_terms"
all_terms=all_terms.resample('1Min', how='sum').fillna(0)

#plot data
time_chart = vincent.Line(all_terms[['CPAC','Fakenews','TheResistance','Trumptrain','FridayFeeling']])
time_chart.axis_titles(x='Time', y='Freq')
time_chart.legend(title='Terms')
time_chart.to_json('time_chart_Top5_2_24.json')