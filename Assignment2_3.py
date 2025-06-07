
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print("Enetr the number :")
num=int(input())

ans=factorial(num)
print("Factorial of number is :",ans)