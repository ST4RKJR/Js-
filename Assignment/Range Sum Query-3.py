def range_sum_queries(lst, queries):
    prefix_sum = [0] * (len(lst) + 1)
    for i in range(len(lst)):
        prefix_sum[i + 1] = prefix_sum[i] + lst[i]
    
    results = []
    for L, R in queries:
        results.append(prefix_sum[R + 1] - prefix_sum[L])
    
    return results

lst = list(map(int, input().split()))
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

output = range_sum_queries(lst, queries)

print("\n".join(map(str, output)))