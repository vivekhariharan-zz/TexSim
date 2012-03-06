#! /usr/bin/env python
# removes stop words from a file of text
# author: Vivek Hariharan

from nltk.corpus import stopwords

class StopWordRemover:
	
	#variables
	inputFileName=""
	outputFileName=""
	#Constructor used to initialize inputFileName and outputFileName
	def __init__ (self,inputFileName):
		self.inputFileName=inputFileName
		self.outputFileName=inputFileName+".nostop"
	
	
	#class methods
	#method accepts takes inputFileName opens it, removes stop words and writes the result to outputFileName
	def removeStopWords(self):
		nonStopWords=[]
		inputFile=open(self.inputFileName,'r')
		outputFile=open(self.outputFileName,'w')
		listOfStopwords=stopwords.words('english')
		for line in inputFile:
			print line
			splitWords=line.split(" ") # split each line into list of words
			for word in splitWords:
				print word
				if word != '':
					if(word.lower() not in listOfStopwords):
						nonStopWords.append(word.lower())
		
		#write non stop words to file
		for word in nonStopWords:
			outputFile.write(word+' ')
		outputFile.close()
	
	#getter for outputfilename		
	def getOutputFilePath(self):
		return self.outputFileName

	#setter for inputfilename and outputfilename				
	def setInputFilePath(self,inputFileName):
		self.inputFileName=inputFileName
		self.outputFileName=inputFileName+".nostop"
		
	

