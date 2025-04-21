#Parity Sum Difference Querry
def parity_queries(arr, queries):
    n = len(arr)
    prefix_even = [0] * (n + 1)
    prefix_odd = [0] * (n + 1)
    
    for i in range(1, n+1):
        num = arr[i-1]
        if num % 2 == 0:
            prefix_even[i] = prefix_even[i-1] + num
            prefix_odd[i] = prefix_odd[i-1]
        else:
            prefix_even[i] = prefix_even[i-1]
            prefix_odd[i] = prefix_odd[i-1] + num
    
    results = []
    for query in queries:
        L, R = query
        sum_even = prefix_even[R+1] - prefix_even[L]
        sum_odd = prefix_odd[R+1] - prefix_odd[L]
        results.append(sum_even - sum_odd)
    
    return results


#Number of Students Unable to Eat Lunch 
def countStudents(students, sandwiches):
    count_0 = students.count(0)
    count_1 = students.count(1)
    for sandwich in sandwiches:
        if sandwich == 0:
            if count_0 > 0:
                count_0 -= 1
            else:
                return count_1  
        elif sandwich == 1:
            if count_1 > 0:
                count_1 -= 1
            else:
                return count_0  

    return 0  
N = int(input())
students = list(map(int, input().split()))
sandwiches = list(map(int, input().split()))

result = countStudents(students, sandwiches)
print(result)