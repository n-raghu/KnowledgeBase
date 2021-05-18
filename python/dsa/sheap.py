

mylist = [69, 36, 96, 18, 16, 99, 88]


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
  
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        print(f'i={i}, n={n}, arr={arr}', end='')
        heapify(arr, n, i)
        print('', arr)

    print('Second Ops Start')

    # One by one extract elements
    for i in range(n-1, 0, -1):
        print(f'arr[i]={arr[i]}, arr[0]={arr[0]}')
        arr[i], arr[0] = arr[0], arr[i]   # swap
        print('after swap', arr)
        heapify(arr, i, 0)
