__author__ = 'Nick'

import nltk as nltk
import pandas as pd
import string
import matplotlib.pyplot as plt
import csv
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator

# Install tokenizer / nltk if needed
# nltk.download()

# Setup punctuation list
punct = set(string.punctuation)
punct = punct | {"''", "``"}
print(type(punct))
print(punct)

punctList3 = set()

punctList = open('punctuation.txt').read()

for line in punctList:
#    if line != '\n':
    punctList3.add(line)

punctList3 | {"''", "``"}

print(punctList3)
print(punct - punctList3)


stopWords = open('stop_words.txt').read()
stopWords = set(nltk.word_tokenize(stopWords))
print(stopWords)

# Get text
text = open('LessonsLearnt.txt').read()

# Tokenize text
splitText = nltk.word_tokenize(text)

# Remove punctuation
strippedText = []
for x in splitText:
    if x in punct:
        continue
    elif x in stopWords:
        continue
    elif x.isdigit():
        continue
    else:
        strippedText.append(x)


print(len(strippedText))   # Number of words (including repeats)
fdist3= nltk.FreqDist(strippedText)
print(len(fdist3))          # Number of individual words
fdist3_common = fdist3.most_common(len(fdist3))



#print(fdist3_common)
#fdist3.plot(50, cumulative=True)
#print(test)

df = pd.DataFrame(fdist3_common)

wnl = nltk.WordNetLemmatizer()
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

df[2] = [wnl.lemmatize(t) for t in df[0]]
df[3] = [porter.stem(t).lower() for t in df[0]]
df[4] = [lancaster.stem(t) for t in df[0]]

df.columns = ['Raw', 'Count', 'Lemmantize', 'Porter', 'Lancaster']
df.sort(columns=['Count'], ascending=False, axis=0, inplace=True)

groupSet = set(df['Porter'])
print(len(groupSet))

z = []
for x in groupSet:
    z.append((df[df['Porter'] == x].iloc[0]['Raw'],df[df['Porter'] == x]['Count'].sum(0) ))

proWords = pd.DataFrame(z)
proWords.columns = ['Word', 'Freq']
proWords.sort(columns=['Freq'], ascending=False, axis=0, inplace=True)
proWords.index = range(0,len(proWords))

#maxWord = proWords['Freq'].iloc[0]
#print(maxWord)

#proWords['CloudFreq'] = proWords['Freq'] / maxWord

list1 = proWords['Word'].tolist()
list2 = proWords['Freq'].tolist()

test5 = list(zip(list1, list2))
print(test5)
df.to_csv("wordSamples.csv", index_label="index")
proWords.to_csv("wordSamples2.csv", index_label="index")

"""
wc = WordCloud(background_color="white", max_words=100, max_font_size=60, width= 600, height=400)
wc.generate_from_frequencies(test5)

plt.imshow(wc)
plt.axis("off")
plt.show()
"""