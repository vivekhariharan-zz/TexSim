#!/usr/bin/env python
#Finds the similarity of two files that have been stemmed and filtered of stop words
# author: Vivek Hariharan

from sets import Set
import math
class SimilarityFinder:

	inputFileName1=""
	inputFileName2=""
	uniqueWords=Set()
	tfDictionarys={}
	idfDictionary={}
	vectors={}
	#default constructor
	def __init__(self):
		pass
	
	#parameterized constructor
	def __init__(self,inputFileName1, inputFileName2):
		self.inputFileName1=inputFileName1
		self.inputFileName2=inputFileName2
	
	#calls methods to compute cosine sim
	def findSimilarity(self):
		inputFile1=open(self.inputFileName1,'r')
		inputFile2=open(self.inputFileName2,'r')
		
		self.computeStatistics(inputFile1,1)
		self.computeStatistics(inputFile2,2)
		
		self.formVectors(1)
		self.formVectors(2)
		vector1=self.vectors[1]
		vector2=self.vectors[2]
		return self.computeSimilarity(vector1,vector2)
		
	#computes the tf of words in the files	
	def computeStatistics(self,inputFile,dictionaryCount):
		#find frequency count of words in first files
		tempDictionary={}
	
		for line in inputFile:
			splitWords=line.split(" ")
			for word in splitWords:
				#added to unique set of words
				if word not in self.uniqueWords:
					self.uniqueWords.add(word)
				#used to compute inverse document frequency	
				if word not in self.idfDictionary:
					self.idfDictionary[word]=1
				else:
					self.idfDictionary[word]=self.idfDictionary[word]+1	
				#used to compute term frequency	
				if word not in tempDictionary:
					tempDictionary[word]=1
				else:
					tempDictionary[word]=tempDictionary[word]+1	
		self.tfDictionarys[dictionaryCount]=tempDictionary
		
		
					
	#computes the cosine similarity from the tfidf vectors 				
	def computeSimilarity(self,vector1,vector2):
		modVector1=0.0
		modVector2=0.0
		dotProduct=0.0
		for term in vector1:
			modVector1+=term*term
		modVector1=math.sqrt(modVector1)
		for term in vector2:
			modVector2+=term*term
		modVector1=math.sqrt(modVector2)
		
		#length of both vectors should be same
		for index in range(len(vector1)):
			dotProduct+=vector1[index]*vector2[index]
		
		return dotProduct/(modVector1 * modVector2)
	
	
	#forms the vectors from the computed statistics
	def formVectors(self, tfDictionaryCount):
		tempVector=[]
		tfDictionary=self.tfDictionarys[tfDictionaryCount]
		#computes tf*idf value, if frequency is 0 value 0 is set
		for word in self.uniqueWords:
			if word not in tfDictionary:
				tempVector.append(float(0))
			else :
				tempVector.append(float(tfDictionary[word])/float(self.idfDictionary[word]))
		
		self.vectors[tfDictionaryCount]=tempVector
			
				
