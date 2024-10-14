x = [i for i in range(1,11)] #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if(x[i] < x[j]):
            x[i],x[j] = x[j],x[i] #sort

a = 10
while(True):
    if(a > 0):
        a-=1
        print('Running')
    elif(a == 0):
        print('Break')
        break;
else:
    print('Else Conditional')

print('Success program')