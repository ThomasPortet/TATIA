import argparse

parser = argparse.ArgumentParser(description='Generate random titles according to data')
parser.add_argument('nb', type=int, nargs='?', default=1, help='number of titles to generate')

args = parser.parse_args()

#Parse data
with open('data.txt', 'r') as file:
	#TODO