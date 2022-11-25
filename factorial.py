def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
num = int(input())

if num <0:
    print("please enter a valid number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print("the factorial of ", num, "is" , factorial(num))