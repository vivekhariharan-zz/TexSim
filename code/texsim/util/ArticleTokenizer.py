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
# class that accepts file path and tokenizes text in the file and prints to outputfile
# author: Vivek Hariharan

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

class ArticleTokenizer:

	inputFileName=""
	outputFileName=""
	
	#parameterized constructor
	def __init__(self, inputFileName):
		self.inputFileName=inputFileName
		self.outputFileName=inputFileName+".tokenized"
		
	
	#setter for inputFileName and outputFileName
	def setInputFileName(self, inputFileName):
		self.inputFileName=inputFileName
		self.outputFileName=inputFileName+".tokenized"
		
		
	#getter for ouputFileName
	def getOutputFilePath(self):
		return self.outputFileName
		
		
		
	#tokenizer
	def tokenize(self):
		inputFile=open(self.inputFileName,'r')
		outputFile=open(self.outputFileName,'w')
		tokens=[]
		#read all text into a single string from the file
		text=""
		for line in inputFile:
			text+=line+" "
			
		#performing sentence tokenizer
		#performing word tokenization on sentence tokenized text
		for t in sent_tokenize(text):
			for wordToken in word_tokenize(t):
				if wordToken != "":
					tokens.append(wordToken)
				
		#send that string to tokenizer
		#tokenizedResult=Token(TEXT=text)
		#WSTokenizer().tokenize(tokenizedResult,addlocs=True)
		
		#write tokenized words to outputfilename
		
		for word in tokens:
			outputFile.write(word+' ')
		outputFile.close()
	
