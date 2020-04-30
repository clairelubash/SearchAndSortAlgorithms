def select(arr):

    for i in range(len(arr)):
        min_ = i
        for j in range(i+1, len(arr)):
            if arr[min_] > arr[j]:
                min_ = j
        arr[i], arr[min_] = arr[min_], arr[i]

    return(arr)

arr = [int(x) for x in input('Enter numbers separated by spaces: ').split(' ')]
print('Sorted list:', select(arr))