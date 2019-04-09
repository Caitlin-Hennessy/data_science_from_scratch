import random
import math

# derivative at x is limit of this function as h -> 0
def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def step(v, direction, step_size):
    return tuple(v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction))

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

def sum_of_squares(v):
    return sum([v_i**2 for v_i in v])

def distance(v1, v2):
    return math.sqrt(sum(((u1 - u2)**2 for u1 in v1 for u2 in v2)))

def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f

def negate(f):
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.0000001):
    # The approach where we choose the best step size out of assorted powers of 10
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0 # starting point
    target_fn = safe(target_fn)
    value = target_fn(theta)

    steps_taken = []

    while True:
        gradient = gradient_fn(theta)
        next_thetas = {step(theta, gradient, -step_size) : step_size for step_size in step_sizes}
        print next_thetas
        next_theta = min(next_thetas, key=lambda theta_tuple: target_fn(list(theta_tuple)))
        print "min", next_theta
        steps_taken.append(next_thetas[next_theta])
        next_value = target_fn(next_theta)
        if abs(value - next_value) < tolerance:
            return theta, steps_taken
        else:
            theta, value = next_theta, next_value

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.0000001):
    return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)


def main():
    """
    v = [random.randint(-10, 10) for i in range(3)]
    tolerance = 0.0000001
    while True:
        gradient = sum_of_squares_gradient(v)
        next_v = step(v, gradient, -0.01)
        if distance(next_v, v) < tolerance:
            break
        v = next_v
    print "next_v", next_v
    """
    theta, steps_taken = minimize_batch(sum_of_squares, sum_of_squares_gradient, [100, 200, 300])
    print list(theta)
    print steps_taken
main()