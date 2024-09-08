#Ez sort

print("Enter Number of List: ")
l = list(map(int, input().split()))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] <= l[j]:
            l[i],l[j] = l[j],l[i]

# print(l)
for i in range(len(l)):
    print(f'{i+1} : {l[i]}')