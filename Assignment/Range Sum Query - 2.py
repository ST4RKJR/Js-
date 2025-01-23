def range_sum_queries(lst, queries):
    n = len(lst)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
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