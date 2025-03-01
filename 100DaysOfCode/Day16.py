#Range Frequency Querry 
def numOfFreq(arr, queries):
    result = []
    for i, j, x in queries:
        result.append(arr[i:j+1].count(x))
    return result