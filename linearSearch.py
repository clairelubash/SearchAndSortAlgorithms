def lin(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return(i)
    return(-1)

arr = [10,200,3000]
x = 10

ans = lin(arr, x)

if ans != -1: 
    print('Item is found at index %d' % ans)
else: 
    print('Item is not in array')