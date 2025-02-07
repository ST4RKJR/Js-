import sys
sys.setrecursionlimit(20000)

def recurse_for_last_occurence(s,ch,idx):
    if idx < 0:
        return -1
    if s[idx] == ch:
        return idx 
    else:
        recurse_for_last_occurence(s,ch,idx-1)


def lastOccurrence(s, ch):
    return recurse_for_last_occurence(s,ch,len(s)-1)
