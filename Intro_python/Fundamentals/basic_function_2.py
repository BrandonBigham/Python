# def countdown(y):
#     arr = []
#     for x in range(y, -1, -1):
#         arr.append(x)
#     return(arr)
# print(countdown(7))

# def Print(x,y):
#     print(x)
#     return(y)
# print(2,7)
    
# def first_plus(arr):
#     sum = 0
#     sum += arr[0]
#     sum += len(arr)
#     return(sum)
# print(first_plus([2,5,7,9]))

def greater_than_second(arr):
    newarr = []
    if len(arr) < 2:
        return ("false")
    y = arr[1]
    for x in range(0,len(arr),1):
        if arr[x] > y:
            newarr.append(arr[x])
    return (newarr)
print(greater_than_second([5]))

# def length_value(size,value):
#     arr = []
#     for x in range(0,size,1):
#         arr.append(value)
#     return(arr)
# print(length_value(5,5))