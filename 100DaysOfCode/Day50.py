#Merge By Parity
n , m = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

i,j = 0,0
merged = []

while i < len(arr) or j < len(brr):
    if j == len(brr) or (i < len(arr) and arr[i] <= brr[j]):
        merged.append(arr[i])
        i += 1
    else:
        merged.append(brr[j])
        j += 1


even = []
odd = []

for i in merged:
    if i % 2 == 0 :
        even.append(i)
    else:
        odd.append(i)

answer = even + odd
print(*answer)

#Non-overlappying Intervals
def remove_overlapping(intervals):
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    last_end = float('-inf')
    
    for interval in intervals:
        start, end = interval
        if start < last_end:
            # Overlapping, need to remove
            count += 1
        else:
            # No overlap, update last_end
            last_end = end

    return count