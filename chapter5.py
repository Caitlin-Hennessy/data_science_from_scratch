import math

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

def main():
    days_spent_car_shopping = [60, 0, 21, 90, 10, 7]
    car_price = [16000, 24000, 15000, 15900, 20000, 22900]
    print "standard deviation of days shopping:", standard_deviation(days_spent_car_shopping) # 35.78
    print "standard deviation of car price:", standard_deviation(car_price) # $3,893.93
    print "covariance:", covariance(days_spent_car_shopping, car_price) # -99887
    print "correlation:", correlation(days_spent_car_shopping, car_price) # -0.72
main()
 