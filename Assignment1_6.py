def chknum(n):
    if(n==0):
        print("Number is Zero")
    elif(n<0):
        print("Number is Negative")
    elif(n>0):
        print("Number is Positive")
    else:
        print("Invalid Input...")

num=int(input("Enter the number "))
chknum(num)