def is_armstrong(n):
    result = 0
    length = len(str(n))
    for i in n:
        value = int(i) ** length
        result += value
    return result
start = int(input())
end = int(input())

for i in range(start,end+1):
    output = is_armstrong(str(i))
    if int(i) == output:
        print(i)