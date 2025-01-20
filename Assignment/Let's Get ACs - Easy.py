n,q = map(int,input().split())
string = input()
for i in range(q):
    x, y = map(int,input().split())
    cout = 0
    for j in range(x,y):
        if string[j]=="C" and string[j-1]=="A":
            cout+=1
    print(cout)