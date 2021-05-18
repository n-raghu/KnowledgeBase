a = [69, 11, 88, 14, 16, 369, 199, 99, 116, 188]
b = [69, 11, 88, 14, 16, 369, 199, 99, 116, 188]


def partition(arr, low, high):
    i = low
    pivot = arr[high]
    #print('pivot', pivot)
    for j in range(low ,high):
        #print('b4', i, j, arr, end='')
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            #print('', 'arr[i]', arr[i], 'arr[j]', arr[j], end='')
            i += 1
        #print('')
        #print('a4', i, j, arr)
    arr[i], arr[high] = arr[high], arr[i]
    return i


def partition2(arr, low, high):
    i = low - 1
    pivot = arr[high]
    print('pivot', pivot)
    for j in range(low ,high):
        print('b4', i, j, arr, end='')
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print('', 'arr[i]', arr[i], 'arr[j]', arr[j], end='')
        print('')
        print('a4', i, j, arr)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def sort_quick(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        piv = partition(arr, low, high)
        sort_quick(arr, low, piv-1)
        sort_quick(arr, piv+1, high)
