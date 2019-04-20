import math
import random
import csv
import dateutil.parser
from matplotlib import pyplot as plt
from collections import Counter
from chapter6 import inverse_normal_cdf, standard_deviation

def bucketize(point, bucket_size):
	return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
	return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=''):
	histogram = make_histogram(points, bucket_size)
	plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
	plt.title(title)
	plt.show()

random.seed(0)
uniform = [200 * random.random() - 100 for _ in range(10000)]
normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]

#plot_histogram(uniform, 10, "Uniform Histogram")
#plot_histogram(normal, 10, "Normal Histogram")

def random_normal():
	return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

#plot_histogram(ys1, 0.1, 'ys1')
#plot_histogram(ys2, 0.1, 'ys2')

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title('Joint distribution')
#plt.show()
plt.clf()

def get_column(data, i):
	return [r[i] for r in data]

'''
Create plot-of-plots showing correlations between all pairs of columns in data
'''
def scatter_plot_matrix(data):
#	_, num_columns = shape(data)
	num_columns = len(data[0])
	fig, ax = plt.subplots(num_columns, num_columns)

	for i in range(num_columns):
		for j in range(num_columns):
			if i != j:
				ax[i][j].scatter(get_column(data, j), get_column(data, i))
			else: 
				ax[i][j].annotate('series ' + str(i), (0.5, 0.5),
								xycoords='axes fraction',
								ha='center', va='center')
			if i < num_columns-1: 
				ax[i][j].xaxis.set_visible(False)
			if j > 0:
				ax[i][j].yaxis.set_visible(False)
	ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
	ax[0][0].set_ylim(ax[0][1].get_ylim())
	plt.show()

#data = [[1, 1, 2, 9], [2, 2, 4, 8], [3, 3, 6, 7]]
#scatter_plot_matrix(data)

'''
Clean data parsing with error catching
'''
def try_or_none(f):
	def f_or_none(x):
		try: return f(x)
		except: return None
	return f_or_none

def parse_row(input_row, parsers):
	return [try_or_none(parser)(value) if parser is not None else value
			for value, parser in zip(input_row, parsers)]

def parse_rows_with(reader, parsers):
	for row in reader:
		yield parse_row(row, parsers)

#data = []
#with open('comma_delimited_stocks.txt', 'rb') as f:
#	reader = csv.reader(f)
#	for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
#		data.append(line)

#print data

def mean(x):
	return float(sum(x))/len(x)

data = [[63, 160, 150],
		[67, 170.2, 160],
		[70, 177.8, 171]]

def scale(data_matrix):
	num_rows, num_cols = len(data_matrix), len(data_matrix[0])
	means = [mean(get_column(data_matrix, j)) for j in range(num_cols)]
	stdevs = [standard_deviation(get_column(data_matrix, j)) for j in range(num_cols)]
	return means, stdevs

'''
Converts each data item in matrix to number of stdevs from mean
Where stdev, mean are based off of each column
'''
def rescale(data_matrix):
	means, stdevs = scale(data_matrix)
	def rescaled(i, j):
		if stdevs[j] > 0:
			return (data_matrix[i][j] - means[j]) / stdevs[j]
		else:
			return data_matrix[i][j]
	return [[rescaled(i, j) for j in range(len(data_matrix[0]))] for i in range(len(data_matrix))]

print rescale(data)