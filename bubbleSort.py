def bubble(arr):

    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return(arr)

arr = [int(x) for x in input('Enter numbers separated by spaces: ').split(' ')]
print('Sorted list:', bubble(arr))
