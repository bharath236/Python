n = input()
reverse = ""
for i in n:
    reverse = i + reverse

if n == reverse:
    print(n , "is palindrome")
else:
    print(n,"is not an palindrome")