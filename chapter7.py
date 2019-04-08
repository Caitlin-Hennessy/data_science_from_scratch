import math
from chapter6 import normal_cdf, inverse_normal_cdf

def normal_approximation_to_binomial(n, p):
    # n = number of trials per sample
    # p = probability of outcome being 1
    # num samples is NOT an input to this. as num samples -> inf, outcome of 
    # many samples will approximate this curve
    mu = p * n
    sigma = sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# normal_cdf(x, mu, sigma) = integral of normal_pdf
# probability that value on line is <= x, given normal dist w/mu and sigma

# note: input/output are actual numbers, not z-values
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

# inverse_normal_cdf = normal upper bound = probability (Z <= z)

def normal_lower_bound(p, mu=0, sigma=1): # probability (Z >= z)
    # or -inverse_normal_cdf(p, mu, sigma)
    return inverse_normal_cdf(1-p, mu, sigma)

def normal_two_sided_bounds(p, mu=0, sigma=1):
    tail_probability = (1-p)/2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = inverse_normal_cdf(tail_probability, mu, sigma)
    return lower_bound, upper_bound

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_cdf(x, mu, sigma)

def estimated_parameters(N, n):
    # N = number of trials, n = number of 1's
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_test_statistic(N_A, n_a, N_B, n_b):
    p_A, sigma_A = estimated_parameters(N_A, n_a)
    p_B, sigma_B = estimated_parameters(N_B, n_b)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


def main():
    print inverse_normal_cdf(0.84) # -> close to 1 bc 84 = 50 + 68/2
    print normal_lower_bound(0.84)
    print normal_two_sided_bounds(0.68)

    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    print normal_two_sided_bounds(0.95, mu_0, sigma_0)

    print normal_cdf(500, mu_0, sigma_0)
main()



