import argparse
import random

parser = argparse.ArgumentParser(description='Generate random titles according to data')
parser.add_argument('input', help='input file for data')
parser.add_argument('nb', type=int, nargs='?', default=1, help='number of titles to generate')

args = parser.parse_args()

#Entrée = poids cumulés, valeurs correspondantes

words = {}

#Parse data
with open(args.input, 'r') as file:
	line = file.readline()
	while line:
		spl = line.split(' ')
		weights = []
		values = []
		wsum = 0
		for i in range(int(spl[1])):
			ent = file.readline().split(' ')
			values.append(ent[0])
			wsum += int(ent[1])
			weights.append(wsum)
		words[spl[0]] = (weights, values)
		line = file.readline()


def genNext(word):
	weights, values = words[word]
	number = random.randint(0, weights[-1] - 1)
	index = 0
	while number >= weights[index]:
		index += 1
	return values[index]

def makeTitle():
	word = genNext('_start_')
	title = word
	word = genNext(word)
	while word != '_end_':
		title += ' ' + word
		word = genNext(word)
	return title

for i in range(args.nb):
	print(makeTitle())