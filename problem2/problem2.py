#2b
#Parse the data and plot into 2D
import sys
import matplotlib.pyplot as plt


def parse_data1(input_file):
	with open(input_file) as myfile:
		lines = [line.rstrip('\n') for line in open(input_file)]
		eruptions = [line.split()[1] if len(line.split()) > 1 else line.split()[0] for line in lines]
	return eruptions

def parse_data2(input_file):
	with open(input_file) as myfile:
		lines = [line.rstrip('\n') for line in open(input_file)]
		waiting = [line.split()[2] if len(line.split()) > 1 else line.split()[0] for line in lines]
	return waiting

def get_normalized1(data_set):
	normalized = []
	floats = [float(x) for x in data_set]
	min_value = min(floats)
	print min_value
	max_value = max(floats)
	print max_value
	for element in floats:
		element = (element - min_value)/(max_value - min_value)
		normalized.append(element)
	return normalized

def get_normalized2(data_set):
	normalized = []
	floats = [float(x) for x in data_set]
	min_value = min(floats)
	print min_value
	max_value = max(floats)
	print max_value
	for element in floats:
		element = (element - min_value)/(max_value - min_value)
		normalized.append(element)
	return normalized


def main():
	fname1 = sys.argv[1]

	eruptions = parse_data1(fname1)
	waiting = parse_data2(fname1)
	new_data_eruption = get_normalized1(eruptions)
	new_data_waiting = get_normalized2(waiting)

	print new_data_eruption, new_data_waiting

main()

