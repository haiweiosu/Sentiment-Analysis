import csv
import sys
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
import re
import string
import operator

# 1(a)
positive = []
negative = []

def parse_dataset(input_file):
	with open(input_file) as f:
		element = [line.rstrip('\n') for line in open(input_file)]
		element = [line.split('\t')[1] if len(line.split('\t')[1]) >= 1 else line.split()[0] for line in element]
		pluscount = 0
		negcount = 0
		for e in element:
			if e == '1':
				pluscount += 1
				positive.append(e)
			elif e == '0':
				negcount += 1
				negative.append(e)
	return pluscount, negcount, positive, negative


#1(b)
#If lower casing every word in the input file, it may disguish some emotional part of being capitalized
#For example, in one of Amazon customer review, customer said:"TAKES MOVING IT ABOUT AFTERTRYING DIFFERENT SIZES.""
#Obviously, this customer wants to express and highlight the part he/she wanted to express. It certainly contained
#some personal emotions. If lowercase all letters, it won't have the same expression as it was before.

#Lemmatization words can be eaisly analyze similar word with similar "look". However, the drawbacks of lemmatization
#is that you can't search for format of words, unless you create additional index. Source: http://www.ideaeng.com/stemming-lemmatization-0601

#strip punctuation can works only if the characters this method removes doesn't change the original sentence expression.
#For example, multiple exclamation points could reflec strong emotional expression for a person. It may represent strong
#like or dislike emotions. However, if adopting strip punctuation method, it decrases the emotional expression. 

#strip stop words may also not the best to process sentiment analysis. Since words 'and' and 'or' sometimes contains logic relationship
#between things that people trying to list. If delete them, it may cause confusion on things listed. 

#1(c)
training_set_plus = []
training_set_neg = []
testing_set_plus= []
testing_set_neg = []
training_set1 = []
training_set2 = []
a = []
b = []
c = []
d = []
e = []
f = []
def parse_dataset_into_training_set(input_file1, input_file2, input_file3):

	amazon = pd.read_csv(input_file1, sep="\t", header=None, names=['Sentence', 'Label']).dropna()
	imdb = pd.read_csv(input_file2, sep="\t(?=[01])", header=None, names=['Sentence', 'Label'], engine='python').dropna()
	yelp = pd.read_csv(input_file3, sep="\t", header=None, names=['Sentence', 'Label']).dropna()

	index1 = 0
	index2 = 0
	temp_neg_value = amazon.iloc[0].Label
	temp_pos_value = amazon.iloc[1].Label

	while index1 < 1000:
		if amazon.iloc[index1].Label == temp_pos_value:
			training_set_plus.append(amazon.iloc[index1].Sentence)
			index1 += 1
		else:
			index1 += 1

	a = training_set_plus[:400]

	while index2 < 1000:
		if amazon.iloc[index2].Label == temp_neg_value:
			training_set_neg.append(amazon.iloc[index2].Sentence)
			index2 += 1
		else:
			index2 += 1

	b = training_set_neg[:400]

	index1 = 0
	index2 = 0
	temp_neg_value = imdb.iloc[0].Label
	temp_pos_value = imdb.iloc[4].Label
	training_set_plus_imdb = []
	training_set_neg_imdb = []

	while index1 < 1000:
		if imdb.iloc[index1].Label == temp_pos_value:
			training_set_plus_imdb.append(imdb.iloc[index1].Sentence)
			index1 += 1
		else:
			index1 += 1

	c =  training_set_plus_imdb[:400]

	while index2 < 1000:
		if imdb.iloc[index2].Label == temp_neg_value:
			training_set_neg_imdb.append(imdb.iloc[index2].Sentence)
			index2 += 1
		else:
			index2 += 1

	d = training_set_neg_imdb[:400]

	index1 = 0
	index2 = 0
	temp_neg_value = yelp.iloc[1].Label
	temp_pos_value = yelp.iloc[0].Label
	training_set_plus_yelp = []
	training_set_neg_yelp = []

	while index1 < 1000:
		if yelp.iloc[index1].Label == temp_pos_value:
			training_set_plus_yelp.append(yelp.iloc[index1].Sentence)
			index1 += 1
		else:
			index1 += 1

	e = training_set_plus_yelp[:400]

	while index2 < 1000:
		if yelp.iloc[index2].Label == temp_neg_value:
			training_set_neg_yelp.append(yelp.iloc[index2].Sentence)
			index2 += 1
		else:
			index2 += 1

	f = training_set_neg_yelp[:400]

	training_set1 = a + c + e
	training_set2 = b + d + f
	training_set = training_set1 + training_set2

	return training_set

def parse_dataset_into_testing_set(input_file1, input_file2, input_file3):

	amazon = pd.read_csv(input_file1, sep="\t", header=None, names=['Sentence', 'Label']).dropna()
	imdb = pd.read_csv(input_file2, sep="\t(?=[01])", header=None, names=['Sentence', 'Label'], engine='python').dropna()
	yelp = pd.read_csv(input_file3, sep="\t", header=None, names=['Sentence', 'Label']).dropna()

	index1 = 0
	index2 = 0
	temp_neg_value = amazon.iloc[0].Label
	temp_pos_value = amazon.iloc[1].Label

	while index1 < 1000:
		if amazon.iloc[index1].Label == temp_pos_value:
			training_set_plus.append(amazon.iloc[index1].Sentence)
			index1 += 1
		else:
			index1 += 1

	aa = training_set_plus[-100:]

	while index2 < 1000:
		if amazon.iloc[index2].Label == temp_neg_value:
			training_set_neg.append(amazon.iloc[index2].Sentence)
			index2 += 1
		else:
			index2 += 1

	bb = training_set_neg[-100:]

	index1 = 0
	index2 = 0
	temp_neg_value = imdb.iloc[0].Label
	temp_pos_value = imdb.iloc[4].Label
	training_set_plus_imdb = []
	training_set_neg_imdb = []

	while index1 < 1000:
		if imdb.iloc[index1].Label == temp_pos_value:
			training_set_plus_imdb.append(imdb.iloc[index1].Sentence)
			index1 += 1
		else:
			index1 += 1

	cc = training_set_plus_imdb[-100:]

	while index2 < 1000:
		if imdb.iloc[index2].Label == temp_neg_value:
			training_set_neg_imdb.append(imdb.iloc[index2].Sentence)
			index2 += 1
		else:
			index2 += 1

	dd = training_set_neg_imdb[-100:]

	index1 = 0
	index2 = 0
	temp_neg_value = yelp.iloc[1].Label
	temp_pos_value = yelp.iloc[0].Label
	training_set_plus_yelp = []
	training_set_neg_yelp = []


	while index1 < 1000:
		if yelp.iloc[index1].Label == temp_pos_value:
			training_set_plus_yelp.append(yelp.iloc[index1].Sentence)
			index1 += 1
		else:
			index1 += 1

	ee = training_set_plus_yelp[-100:]

	while index2 < 1000:
		if yelp.iloc[index2].Label == temp_neg_value:
			training_set_neg_yelp.append(yelp.iloc[index2].Sentence)
			index2 += 1
		else:
			index2 += 1

	ff = training_set_neg_yelp[-100:]

	testing_set_plus = aa + cc + ee
	testing_set_neg = bb + dd + ff
	testing_set = testing_set_plus + testing_set_neg

	return testing_set

#1(d)
#create a dictionary containing unique word in training set
#The reason why we can't use testing set to generate unique word is
#that we are using testing set to test our bag of word model. Therefore,
#we won't be able to see the content of testing test when generating the mdoel

unique_word1 = []
non_unique_word2 = []
count = 0
dictionary = {}
def uniqueWord (train_set, test_set):
	exclude = set(string.punctuation)
	lmtzr = WordNetLemmatizer()
	for element1 in train_set:
		temp_list1 = element1.decode('utf-8').split()
		for word1 in temp_list1:
			word1 = lmtzr.lemmatize(word1)
			word1 = ''.join(ch for ch in word1 if ch not in exclude)
			if not word1 in unique_word1:
				unique_word1.append(word1)

	for element2 in test_set:
		temp_list2 = element2.split()
		temp_list2 = element2.decode('utf-8').split()
		for word2 in temp_list2:
			non_unique_word2.append(word2)

	dictionary.setdefault("list", []).append("list_item")
	for element in unique_word1:
		dictionary.update({element:1})

	for e in non_unique_word2:
		if dictionary.has_key(e):
			dictionary[e] += 1

	sorted_dic = sorted(dictionary.items(), key = operator.itemgetter(1))

	return sorted_dic


#Problem2
#(a)
#Solution: Since both K-Mean and EM algorithms are iterative algorithms to
#assign points to clusters. Since K-means makes hard assignments of xi to clusters
#whereareas, EM provides soft valus to clusters, the reason is that K means is a 
#special cases for EM with ∑k  = sigma I and sigma goes to 0. 






def main():
	fname1 = sys.argv[1]
	fname2 = sys.argv[2]
	fname3 = sys.argv[3]
	training_set = parse_dataset_into_training_set(fname1, fname2, fname3)
	testing_set = parse_dataset_into_testing_set(fname1, fname2, fname3)

	print uniqueWord(training_set, testing_set)




main()






