# Format :
# <word> <nb of entries>
# <next word> <nb of occurences>
# ...
# start of title is written _start_
# end of title is written _end_

import argparse
import nltk
from nltk.tokenize import RegexpTokenizer

parser = argparse.ArgumentParser(description='Parse and preprocess data for the program.')
parser.add_argument('input', help='input file')
parser.add_argument('output', help='output file')

args = parser.parse_args()

startwords = {}
middlewords = {}

tokenizer = RegexpTokenizer(r'\w+')

def addStart(wd):
	startwords[wd] = startwords.get(wd, 0) + 1

def addBigram(wd1, wd2):
	wddict = middlewords.get(wd1, {})
	wddict[wd2] = wddict.get(wd2, 0) + 1
	middlewords[wd1] = wddict

def addEnd(wd):
	addBigram(wd, "_end_")

#Parse
with open(args.input, "r") as file:
	for l in file:
		l = l.rstrip()
		if l.isspace():
			continue
		words = tokenizer.tokenize(l)
		if not words:
			continue
		addStart(words[0])
		addEnd(words[-1])
		bigrams = nltk.bigrams(words)
		for b in bigrams:
			addBigram(b[0], b[1])

#Save formatted data
with open(args.output, "w") as file:
	#Write start words
	file.write('_start_ ' + str(len(startwords)) + '\n')
	for k, v in startwords.items():
		file.write(k + ' ' + str(v) + '\n')
	#Write middle words
	for w, d in middlewords.items():
		file.write(w + ' ' + str(len(d)) + '\n')
		for k, v in d.items():
			file.write(k + ' ' + str(v) + '\n')
