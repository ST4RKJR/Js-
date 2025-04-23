def max_sum(arr):
    n = len(arr)
    # Initialize arrays for DP
    dp_no_delete = [0] * n
    dp_one_delete = [0] * n

    dp_no_delete[0] = arr[0]
    dp_one_delete[0] = float('-inf')
    max_result = arr[0]

    for i in range(1, n):
        dp_no_delete[i] = max(dp_no_delete[i - 1] + arr[i], arr[i])
        dp_one_delete[i] = max(dp_no_delete[i - 1], dp_one_delete[i - 1] + arr[i])
        max_result = max(max_result, dp_no_delete[i], dp_one_delete[i])

    return max_result
