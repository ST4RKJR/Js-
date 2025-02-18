def recursive_bubble(seq, n=None, i=0):
    if n is None:
        n = len(seq)
    
    if n == 1:
        return
    
    if i < n - 1:
        if seq[i] > seq[i + 1]:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
        recursive_bubble(seq, n, i + 1)
    else:
        recursive_bubble(seq, n - 1, 0)

T = 2
test_cases = [
    ([4, 1, 3, 9, 7], 5),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10)
]

for seq, n in test_cases:
    recursive_bubble(seq, n)
    print(seq)
    
    
def recursive_bubble(lst):
    # if times == 0:
    #     return lst
    # lst = recurse(lst,0)
    # lst = recurse(lst,times-1)
    # return lst
    if len(lst) == 1 :
        return lst 
    recurse(lst)
    
    lst = recursive_bubble(lst[:-1]) + [lst[-1]]
    return lst

    # def bubble_times(lst,times):
    #     if times == 0:
    #         return lst
    #     recurse(lst)
    #     return bubble_times(lst,times-1)
    

    # return bubble_times(lst,len(lst))

def recurse(lst,index=0):
    if index+1 >= len(lst):
        return lst
    if lst[index] > lst[index+1]:
        lst[index],lst[index+1] = lst[index+1],lst[index]
    return recurse(lst,index+1)
    
    
    