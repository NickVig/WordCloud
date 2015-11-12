__author__ = 'Nick'

import nltk as nltk
import time

class WordCounter():

    # --- start config variables - to be moved to config file
    defaultPunctuationInFile = "punctuation.txt"
    defaultStopWordInFile = "stop_words.txt"
    # --- end config variables - to be moved to config file


    def __init__(self, punctuationInFileName = "NotSet", stopWordsInFileName = "NotSet"):
        """Sets up the ..."""
        if punctuationInFileName == "NotSet":
            self.punct = set([line.rstrip() for line in open(self.defaultPunctuationInFile)])
        else:
            self.punct = set([line.rstrip() for line in open(punctuationInFileName)])

        if stopWordsInFileName == "NotSet":
            # note 1: stop words have a case?
            # note 2: probably a better way of removing blank space.
            self.stopWords = set([line.rstrip() for line in open(self.defaultStopWordInFile)]) - set("")
        else:
            self.stopWords = set([line.rstrip() for line in open(stopWordsInFileName)])


    def processText(self, textFileName, removeNumbers=True, processAsLowerCase=True ):
        #ToDo - add line processing code as well as individual text processing
        #ToDo - improve processing with optional number removal
        #ToDo - improve processing by parsing with all lower case

        startTime = time.time()

        #ToDo - optimise tokeniser!

        tokenText = open(textFileName).read()
        tokenText = nltk.word_tokenize(tokenText)

        tokenText2 = [{'RawText' : line.rstrip()} for line in open(textFileName)]


        #print(tokenText2[0:10])
        #print(tokenText2[2]['RawText'])

        #tokenText3 = tokenText2.copy()
        #tokenText3 = [{'TokenText' : nltk.word_tokenize(i['RawText'])}for i in tokenText2]

        #tokenText3=[]
        #for i in tokenText2:
        #    tokenText3 = tokenText3 + [{'RawText' : i['RawText'], 'TokenText' : nltk.word_tokenize(i['RawText'])}]

        #for i in tokenText3:
        #    print(i)

        tokenText4 = []
        lenTokenText2 = 0
        for line in open(textFileName):
            tempDict = {'RawText' : line.rstrip(), 'TokenText' : nltk.word_tokenize(line)}
            tempDict['LenTokenText'] = len(tempDict['TokenText'])
            lenTokenText2 += tempDict['LenTokenText']
            tokenText4.append(tempDict)

        for i in tokenText4:
            print(i)

        print(lenTokenText2)

        self.lenTokenText = len(tokenText)

        self.strippedText = []
        for x in tokenText:
            if x in self.punct:
                continue
            elif x in self.stopWords:
                continue
            elif x.isdigit():
                continue
            else:
                self.strippedText.append(x)

        self.fdist = nltk.FreqDist(self.strippedText)

        self.elapsedProcessText = time.time() - startTime

    def printPunctuation(self):
        print(self.punct)

    def addPuctuation(self, addedValues):
        self.punct = self.punct | set(addedValues)

    def removePunctuation(self, removeValues):
        self.punct = self.punct - set(removeValues)

    def printStopWords(self):
        print(self.stopWords)

    def addStopWords(self, addedValues):
        self.stopWords = self.stopWords | set(addedValues)

    def removeStopWords(self, removeValues):
        self.stopWords = self.stopWords - set(removeValues)

    def showTextProcessingStats(self):
        print("Processing time:                     %2.2f Seconds" % (self.elapsedProcessText))
        print("Text number of words:                %d" % self.lenTokenText)
        print("Text number of 'clear' words:        %d" % len(self.strippedText))
        print("Text number of individual words:     %d" % len(self.fdist))

        #ToDo - record a dictionary of times to allow comparisions through out the module

    def showFreqDist(self, plotSize = 50):

        #ToDo - improve plotSize selection

        print("Frequency distribution plot size is:                 %d" % plotSize)
        print("Frequency distribution plot size as pc of words:     %2.2f" % ((plotSize/len(self.fdist))*100))
        self.fdist.plot(plotSize, cumulative=False)

if __name__ == "__main__":

    wc1 = WordCounter()
    #wc1.printPunctuation()
    #wc1.printStopWords()
    wc1.processText("LessonsLearnt.txt")
    wc1.showTextProcessingStats()

    if 1 == 0:
        wc1.showFreqDist()
