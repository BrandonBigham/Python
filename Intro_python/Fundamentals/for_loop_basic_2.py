# def big(arr):
#     for x in range(0,len(arr),1):
#         if arr[x] > 0:
#             arr[x] = "big"
#     return (arr)
# print(big([-3,1,2,-4,5]))

# def positive(arr):
#     sum = 0
#     for x in range(0,len(arr),1):
#         if arr[x] > 0:
#             sum+= 1
#     arr[len(arr)-1] = sum
#     return(arr)
# print(positive([1,2,3,4,5,6,7,8,9,0,0]))

# def total(arr):
#     sum = 0
#     for x in range(len(arr)):
#         sum += arr[x]
#     return (sum)
# print(total([1,2,3,4,5]))

# def average(arr):
#     sum = 0
#     for x in range(len(arr)):
#         sum += arr[x]
#     return (sum/len(arr))
# print(average([1,2,3,4,5]))

# def length(arr):
#     sum = 0
#     for x in range(0,len(arr),1):
#         sum+= 1
#     return(sum)
# print(length([1,2,3,4,5,6,7,8,9,0,0]))

# def minimum(arr):
#     min = arr[0]
#     for x in range(0,len(arr),1):
#         if min > arr[x]:
#             min = arr[x]
#     return(min)
# print(minimum([1,2,3,4,5,6,7,8,9,0,0]))

# def maximum(arr):
#     max = arr[0]
#     for x in range(0,len(arr),1):
#         if max < arr[x]:
#             max = arr[x]
#     return(max)
# print(maximum([1,2,3,4,5,6,7,8,9,0,0]))

def analysis(arr):
    dictionary = {'sum':'0', 'average':'0', 'min':'0', 'max':'0', 'length':'0'}
    sum = 0
    length = 0
    min = arr[0]
    max = arr[0]
    for x in range(0,len(arr),1):
        if min > arr[x]:
            min = arr[x]
        if max < arr[x]:
            max = arr[x]
        sum += arr[x]
        length += 1
    average = sum/len(arr)
    dictionary['sum'] = sum
    dictionary['average'] = average
    dictionary['min'] = min
    dictionary['max'] = max
    dictionary['length'] = length
    return (dictionary)
print(analysis([1,2,3,4,5,6,7,8,9,0]))