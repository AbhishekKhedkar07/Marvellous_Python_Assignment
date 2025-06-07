def digit(n):
    ans=0
    while(n>0):
        n=n//10
        ans=ans+1
    return ans
print("Enter the number ")
num=int(input())
val=digit(num)
print("Digit in number are :",val)