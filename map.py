#map_function

li = [1,2,3,4,5,6,7,8,9,10]

def fun(x):
    return x**x 
print(list(map(fun,li)))