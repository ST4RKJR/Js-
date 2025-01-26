def remove_outliers(data_list):
    y = variance(data_list)
    for x in data_list:
        if abs(x - mean(data_list)) > 2*(y**0.5):
            data_list.remove(x)
    return data_list