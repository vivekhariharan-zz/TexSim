#! /usr/bin/env python
# wrapper that calls stopWordRemover
# 		     stemmer
#		     and similarityFinder

from texsim.util.ArticleTokenizer import ArticleTokenizer
from texsim.util.StopWordRemover import StopWordRemover
from texsim.util.Stemmer import Stemmer
from texsim.util.SimilarityFinder import SimilarityFinder

import sys

#populate files ../data/textInput1
# ../data/textInput2

inputFilePath1="../data/file1"
inputFilePath2="../data/file2"
at1 = ArticleTokenizer(inputFilePath1)
at1.tokenize()
at2= ArticleTokenizer(inputFilePath2)
at2.tokenize()

swr1=StopWordRemover(at1.getOutputFilePath())
swr2=StopWordRemover(at2.getOutputFilePath())
print at1.getOutputFilePath() +" here"
swr1.removeStopWords()
swr2.removeStopWords()
print swr1.getOutputFilePath() + " present"
stem1=Stemmer(swr1.getOutputFilePath())
stem2=Stemmer(swr2.getOutputFilePath())
stem1.doStemming()
stem2.doStemming()
print stem1.getOutputFilePath() + " here too"

simFinder=SimilarityFinder(stem1.getOutputFilePath(),stem2.getOutputFilePath())
print simFinder.findSimilarity()








