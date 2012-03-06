#! /usr/bin/env/ python
# stemmer class that is used to stem words in a input file and writes to an output file
# author: Vivek Hariharan

from nltk.stem.porter import PorterStemmer

class Stemmer:

	inputFileName=""
	outputFileName=""
	
	#default constructor
	def __init__(self):
		pass
			
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

