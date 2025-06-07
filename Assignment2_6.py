print("Enter the number :")
num=int(input())

for i in range(num+1):
    for j in range (num+1):
        if(j>i):
            print(" * ",end="")
    print("")