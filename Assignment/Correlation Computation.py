def calculate_correlation(x, y, n):

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    std_x = (sum((x[i] - mean_x) ** 2 for i in range(n))) ** 0.5
    std_y = (sum((y[i] - mean_y) ** 2 for i in range(n))) ** 0.5

    correlation = covariance / (std_x * std_y)
    return correlation