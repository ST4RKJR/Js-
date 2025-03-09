#Generate Binary Strings
N = int(input())
for i in range(2**N):
    print(bin(i)[2:].zfill(N))


