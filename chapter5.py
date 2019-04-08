import math
import random
from matplotlib import pyplot as plt
from collections import Counter

# subtract mean from each element
def de_mean(x):
    x_bar = sum(x) / len(x)
    return [x_i - x_bar for x_i in x]

def sum_of_squares(x):
    return sum([x_i ** 2 for x_i in x])

# average squared deviation from the mean (almost ... why n-1??)
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

# average deviation from the mean (kinda)
def standard_deviation(x):
    return math.sqrt(variance(x))

# dot product
def dot(x, y):
    return sum([x[i]*y[i] for i, _ in enumerate(x)])

# avg product of variance
# (x1 - x_avg)*(y1 - y_avg) + (x2 - x_avg)*(y2 - y_avg) ... / (n - 1)
# high x, high y -> pos
# high x, low y -> neg
# neither -> close to 0
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

# avg product of num standard deviations from mean
# (x1 - x_avg)/std_dev(x) * (y1 - y_avg)/std_dev(y) ... / (n-1)
def correlation(x, y):
    return covariance(x, y) / (standard_deviation(x) * standard_deviation(y))

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    histogram = Counter(data)
    k = histogram.keys()
    v = histogram.values()
    ys2 = [float(v2) / num_points for v2 in v]
    plt.bar(k, ys2)

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial distribution vs. Normal Approximation")
    plt.show()

def main():
    days_spent_car_shopping = [60, 0, 21, 90, 10, 7]
    car_price = [16000, 24000, 15000, 15900, 20000, 22900]
    #print "standard deviation of days shopping:", standard_deviation(days_spent_car_shopping) # 35.78
    #print "standard deviation of car price:", standard_deviation(car_price) # $3,893.93
    #print "covariance:", covariance(days_spent_car_shopping, car_price) # -99887
    #print "correlation:", correlation(days_spent_car_shopping, car_price) # -0.72

    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    #plt.show()
    plt.clf()

    plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
    plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
    plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
    plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
    plt.legend(loc=4)
    plt.title("Various Normal cdfs")
    #plt.show()
    plt.clf()

    make_hist(0.75, 100, 1000)

main()
 