#   Copyright [2012] [Vivek Hariharan]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


#! /usr/bin/env python
# wrapper that finds the Similarity of the two documents 
#		     stopWordRemover
# 		     stemmer
#		     and similarityFinder
# author: Vivek Hariharan

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








