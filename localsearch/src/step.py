import numpy as np


def compute_error_for_line_given_points(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2 / N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2 / N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def gradient_descent(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]


if __name__ == "__main__":
    points = np.genfromtxt("./data/data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    num_iterations = 1000
    print(
        f"Starting gradient descent at b = {initial_b}, m = {initial_m}, error = {compute_error_for_line_given_points(initial_b, initial_m, points)}"
    )
    print("...Running...")
    [b, m] = gradient_descent(
        points, initial_b, initial_m, learning_rate, num_iterations
    )
    print(
        f"After {num_iterations} iterations b = {b}, m = {m}, error = {compute_error_for_line_given_points(b, m, points)}"
    )