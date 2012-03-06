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


#! /usr/bin/env/ python
# stemmer class that is used to stem words in a input file and writes to an output file
# author: Vivek Hariharan

from nltk.stem.porter import PorterStemmer

class Stemmer:

	inputFileName=""
	outputFileName=""
	
			
	#constructor that initializes inputfilename and outputfilename
	def __init__(self,inputFileName):
		self.inputFileName=inputFileName
		self.outputFileName=inputFileName+".stemmed"
		
	
	#getter for ouputFileName
	def getOutputFilePath(self):
		return self.outputFileName	
	
	#setter for inputFileName and outputFileName	
	def setInputFileName(self, inputFileName):
		self.inputFileName=inputFileName
		self.outputFileName=inputFileName+".stemmed"
		
	#stemming process using Porter Stemmer
	def doStemming(self):
		inputFile=open(self.inputFileName,'r')
		outputFile=open(self.outputFileName,'w')
		
		stemmedWords=[]
		#get each line
		for line in inputFile:
			splitWords=line.split(" ")
			#go through each word
			for word in splitWords:
				stemmedWords+=PorterStemmer().stem_word(word)
		
		#write stemmed list to outputFile
		for word in stemmedWords:
			outputFile.write(word+" ")
		outputFile.close()

