__author__ = 'Nick'

import nltk as nltk
import time

class WordCounter():

    #ToDo - write / read file to / from JSON
    #ToDo - write file to CSV

    """
    Class takes:
        - stop words
        - stop punctuation
        - text to be processed

    Class produces:
        - Tokenised text in a list of dictionaries
            - idNum             int     increased by 1 for each line of text
            - RawText           string  each line of input text from the text file with line breakes removed
            - TokenText         list    tokenised RawText (without puncutaiton / stop words removed)
            - LenStrippedText   int     length of TokenText
            - StrippedText      list    tokenised text with puncuation and stop words removed
            - LenStrippedText   int     length of StrippedText

        - Assorted other helper methods
    """

    # --- start config variables - to be moved to config file
    defaultPunctuationInFile = "punctuation.txt"
    defaultStopWordInFile = "stop_words.txt"
    # --- end config variables - to be moved to config file


    def __init__(self, punctuationInFileName = "NotSet", stopWordsInFileName = "NotSet"):
        """Sets up the the stop punctuation and stop words"""
        if punctuationInFileName == "NotSet":
            self.punct = set([line.rstrip() for line in open(self.defaultPunctuationInFile)])
        else:
            self.punct = set([line.rstrip() for line in open(punctuationInFileName)])

        if stopWordsInFileName == "NotSet":
            # note 1: stop words have a case?
            self.stopWords = set([line.rstrip() for line in open(self.defaultStopWordInFile)]) - set("")
        else:
            self.stopWords = set([line.rstrip() for line in open(stopWordsInFileName)])


    def processText(self, textFileName, removeNumbers=True, processAsLowerCase=True ):
        """
        Method takes text file and returns a list of dictionarys
        :param textFileName: the name (and path) of the text file to read
        :param removeNumbers: not used in this version
        :param processAsLowerCase: boolian
        :return: nothing
        """
        #ToDo - add line processing code as well as individual text processing
        #ToDo - improve processing with optional number removal
        #ToDo - improve processing by parsing with all lower case

        startTime = time.time()

        idNum = 0
        self.textData = []
        self.lenTokenText = 0

        # ToDo - allow different line splits e.g. tab, new line etc
        for line in open(textFileName):

            tempDict = {'idNum' : idNum,
                        'RawText' : line.rstrip(),
                        'TokenText' : nltk.word_tokenize(line)}

            tempDict['LenTokenText'] = len(tempDict['TokenText'])
            self.lenTokenText += tempDict['LenTokenText']

            idNum += 1

            strippedText =[word for word in tempDict['TokenText'] \
                           if word not in self.punct \
                           and word not in self.stopWords \
                           and word is not word.isdigit()]

            if len(strippedText) > 0:
                tempDict['LenStrippedText'] = len(strippedText)
                tempDict['StrippedText'] = strippedText
                self.textData.append(tempDict)

        self.strippedText = [word for dataEntry in self.textData for word in dataEntry['StrippedText']]

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
        print("Processing time per word:            %2.2f uSeconds" % ((self.elapsedProcessText/self.lenTokenText)*1000000))
        print("Text number of words:                %d" % self.lenTokenText)
        print("Text number of 'clear' words:        %d" % len(self.strippedText))
        print("Text number of individual words:     %d" % len(self.fdist))

        #ToDo - record a dictionary of times to allow comparisions through out the module

    def showFreqDist(self, plotSize = 50):

        #ToDo - improve plotSize selection

        print("Frequency distribution plot size is:                 %d" % plotSize)
        print("Frequency distribution plot size as pc of words:     %2.2f" % ((plotSize/len(self.fdist))*100))
        self.fdist.plot(plotSize, cumulative=False)

    def printTextData(self, noRowsToPrint = 4):

        #ToDo - make print order (start with statistics)

        i = 0
        for x in self.textData:
            print(x)

            i += 1
            if i >= noRowsToPrint:
                return

if __name__ == "__main__":

    wc1 = WordCounter()
    #wc1.printPunctuation()
    #wc1.printStopWords()
    wc1.processText("LessonsLearnt.txt")
    wc1.showTextProcessingStats()
    wc1.printTextData()

    if 1 == 0:
        wc1.showFreqDist()
