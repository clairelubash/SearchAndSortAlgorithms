def merge(arr):

    lows, highs = [], []

    while len(arr) >= 2:
        low, high = min(arr), max(arr)
        lows.append(low), highs.append(high)
        arr.remove(low), arr.remove(high)
    
    highs.reverse()

    return(lows + arr + highs)

arr = [int(x) for x in input('Enter numbers separated by spaces: ').split(' ')]
print('Sorted list:', merge(arr))