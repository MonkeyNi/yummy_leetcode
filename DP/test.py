m=5
n=4

for l in range(2,n+1):
    for i in range(n-l+1):
        j = i+l-1
        print(f' [{i}][{j}]')
