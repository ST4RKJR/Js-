#Longest Subsequence with Limited Sum
def answerQueries(nums, queries):
    nums.sort()
    prefix = []
    sum_ = 0
    for num in nums:
        sum_ += num
        prefix.append(sum_)
    
    result = []
    for q in queries:
        count = 0
        for p in prefix:
            if p > q:
                break
            count += 1
        result.append(count)
    
    return result

#Find the Diagonal Sum
def calculate_diagonal_sum(matrix):
    n = len(matrix)
    total = sum(matrix[i][i] + matrix[i][n - i - 1] for i in range(n))
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]
    return total
