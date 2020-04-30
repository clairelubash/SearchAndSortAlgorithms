def bin_iter(arr, start, end, item):

    while start <= end:
        mdpt = int(start + (end - start) / 2)
  
        if arr[mdpt] == item: 
            return(mdpt)

        elif arr[mdpt] > item: 
            end = mdpt - 1 
  
        else: 
            start = mdpt + 1

    return(-1)


def bin_rec(arr, start, end, item): 

    if start > end:
        return(-1)

    else:
        mdpt = int(start + (end - start) / 2)
  
        if arr[mdpt] == item: 
            return mdpt 

        elif arr[mdpt] > item: 
            return bin_rec(arr, start, mdpt - 1, item) 
  
        else: 
            return bin_rec(arr, mdpt + 1, end, item)       


arr = [2, 3, 4, 10, 40] 
x = 10
  
ans_rec = bin_rec(arr, 0, len(arr) - 1, x) 
ans_iter = bin_iter(arr, 0, len(arr) - 1, x) 


if ans_iter != -1: 
    print('Item is found iteratively at index %d' % ans_iter)
if ans_rec != -1: 
    print('Item is found recursively at index %d' % ans_rec)
else: 
    print('Item is not in array')

