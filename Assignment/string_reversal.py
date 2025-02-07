import sys
sys.setrecursionlimit(20000)

def rev_str(s,idx):
    if idx == len(s) -1:
        return s[idx]
    
    return rev_str(s,idx+1) + s[idx]    

s = input()
print(rev_str(s,0))