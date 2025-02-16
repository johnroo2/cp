def binarySearch(array, find):

    l, r = 0, len(array) - 1

    while l < r:
        mid = (l + r) // 2
        
        if array[mid] == find:
            return mid
        elif array[mid] < find:
            l = mid + 1
        else:
            r = mid - 1
            
    return -1
            
            
array = [1, 2, 5, 7, 8, 10]
find = 4

print(binarySearch(array, find))