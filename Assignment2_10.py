def Dsum(n):
    ans=0
    digit=0
    while(n>0):
        digit=n%10
        n=n//10
        ans=ans+digit
    return ans
print("Enter the number ")
num=int(input())
val=Dsum(num)
print("SUm of Digit in number are :",val)