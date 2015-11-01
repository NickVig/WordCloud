__author__ = 'Nick'

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

text = open('Alice.txt').read()

wc = WordCloud(background_color="white", max_words=100, stopwords=STOPWORDS.add("said"))
wc.generate(text)

print(wc.process_text(text=text))

plt.imshow(wc)
plt.axis("off")
plt.show()