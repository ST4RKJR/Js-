array = [1,2,7,9,11]
target = 22
left = 0
right = 1
n = len(array)
while right < n:
    diff = array[right] - array[left]
    if diff == target:
        print("YES")
        break
    elif diff < target:
        right += 1
    else:
        left += 1
    print("NO")
    break
    
    
    