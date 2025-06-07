
def factAdd(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    return sum

print("Enetr the number :")
num=int(input())

ans=factAdd(num)
print("Sum of Factors of number is :",ans)