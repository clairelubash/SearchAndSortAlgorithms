def count(arr):

    k = max(arr) + 1
    counts = [0] * k

    for i in arr:
        counts[i] += 1

    index = 0

    for i in range(len(counts)):

        while counts[i] > 0:
            arr[index] = i
            index += 1
            counts[i] -= 1
    
    return(arr)

arr = [int(x) for x in input('Enter numbers separated by spaces: ').split(' ')]
print('Sorted list:', count(arr))