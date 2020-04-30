def insert(arr):

    for i in range(1, len(arr)):
        curr = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > curr:
            arr[pos] = arr[pos-1]
            pos -= 1
        
        arr[pos] = curr
    
    return(arr)

arr = [int(x) for x in input('Enter numbers separated by spaces: ').split(' ')]
print('Sorted list:', insert(arr))