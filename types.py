
# Python’s built-in sorted: 0.009s
# Radix sort: 0.220s
# Quicksort: 0.247s
# Shell sort: 0.250s
# Merge sort: 0.435s
# Heap sort: 0.473s
# Counting sort: 1.945s
# Selection: 3.426s
# Insertion sort: 7.854s
# Bubble sort: 8.052s
# Cocktail shaker sort: 8.342s

# Bubble sort code

# Average time complexity: O(n²)
def bubble_sort(l: list):
    arr = l[::]
    is_sorted = True
    end = len(arr)
    while is_sorted:
        is_sorted = False
        for i in range(1, end):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                is_sorted = True
        end -= 1
    return arr

# Insertion Sort

# Average time complexity: O(n²)
def insertion(l: list):
    arr = l[::]
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

# Selection Sort

# Average time complexity: O(n²)
def selection(l: list):
    arr = l[::]
    for i in range(len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        if i != m:
            arr[i], arr[m] = arr[m], arr[i]
    return arr

# Quicksort

# O(nlog(n))
def quicksort(l:list):
    arr = l[::]
    if len(arr) <= 1:
        return arr
    l = [x for x in arr[1:] if x <= arr[0]]
    r = [x for x in arr[1:] if x > arr[0]]
    print("l", l)
    print("r", r)
    return quicksort(l) + arr[0:1] + quicksort(r)

# MergeSort

# O(nlog(n))
def merge_sort(l:list):
    arr = l[::]
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    print("array1", left)
    print("array2", right)
    return merge(merge_sort(left), merge_sort(right))

def merge(l, r):
    arr = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr.append(l[i])
            i += 1
        else:
            arr.append(r[j])
            j += 1
    while i < len(l):
        arr.append(l[i])
        i += 1
    while j < len(r):
        arr.append(r[j])
        j += 1
    print("arr", arr)
    return arr

# Counting Sort

# Average time complexity: O(n + k)
def countsort(l:list):
    arr = l[::]
    k = 0
    new_list = (max(arr) + 1) * [0]
    for j in arr:
        new_list[j] += 1
    for i in range(max(arr) + 1):
        if i != 0:
            new_list[i] += new_list[i - 1]
        while new_list[i] != k:
            arr[k] = i;
            k += 1
    return arr

# HeapSort

# Average time complexity: O(nlog(n))
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(l: list):
    arr = l[::]
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


# Radix Sort

# Average time complexity: O(nk)
def get_digit(num, i):
    """Return the (i)th index of num"""
    return (num // 10**i) % 10

def max_digits(arr):
    """Return the length of the longest element in array"""
    return len(str(max(arr)))

def radix_sort(l:list):
    """Sort an array of positive integers"""
    arr = l[::]
    max_len = max_digits(arr)
    for i in range(max_len):
        res = [[] for x in range(10)]
        for k in arr:
            digit = get_digit(k, i)
            res[digit].append(k)
        arr = [y for x in res for y in x]
    return arr

# Cocktail Shaker Sort

# Average time complexity: O(n²)
def shaker(l:list):
    arr = l[::]
    sort = True
    start = 0
    end = len(arr)
    while (sort):
        sort = False
        for i in range(start, end):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i-1], arr[i]
            sort = True
        if not sort:
            break
        for j in range(end - 1, start, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            sort = True
        start += 1
        end -= 1
    return arr

# Shell Sort

# Average time complexity: O(nlog(n))
def shell(l:list):
    arr = l[::]
    n = 0
    while (n < len(arr) // 3):
        n = n * 3 + 1
    while (n > 0):
        for i in range(int(n), len(arr)):
            tmp = arr[i]
            j = i
            while j >= n and arr[j - n] > tmp:
                arr[j] = arr[j-n]
                j -= n
                arr[j] = tmp
        n = (n - 1) // 3
    return arr




#timsort

def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)
    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)
    else:
        return mid


"""
Insertion sort that the heap sort uses if the array size is small or if
the size of the "run" is small
"""
def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array

def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def timsort(the_array):
    runs, sorted_runs = [], []
    l = len(the_array)
    new_run = [the_array[0]]
    for i in range(1, l):
        if i == l-1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i-1]:
            if not new_run:
                runs.append([the_array[i-1]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(the_array[i])
    for each in runs:
        sorted_runs.append(insertion_sort(each))
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    print(sorted_array)