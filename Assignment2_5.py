
def chkPrime(n):
    cnt=0
    for i in range(2,n):
        if(n%i==0):
            cnt=cnt+1
    return cnt

print("Enetr the number :")
num=int(input())

ans=chkPrime(num)
if(ans>0):
    print("Number is Not prime")
else:
    print("Number is prime")