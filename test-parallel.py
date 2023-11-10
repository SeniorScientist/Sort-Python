import random
import time
import multiprocessing

THRESHOLD = 16


def run_length(array) -> int:
    """
    run_length does calculate an appropriate unit value for sort.

    :param array: array for sort
    :return: unit value
    """ 
    runLength = len(array)
    remainder = 0
    while runLength > THRESHOLD:
        if runLength % 2 == 1:
            remainder = 1
        runLength = runLength // 2
    return runLength + remainder


def insertion_sort(obj) -> list:
    """
    insertion_sort does sort the array using insertion sort algorithm

    :param obj[0]: array for sort 
    :param obj[1]: flag for determining the direction of sort
    :return: sorted array
    """
    array = obj[0]
    reverse = obj[1]
    for index in range(1, len(array)):
        temp = array[index]
        index2 = index - 1
        if reverse is False:
            while index2 >= 0 and array[index2] > temp:
                array[index2 + 1] = array[index2]
                index2 -= 1
            array[index2 + 1] = temp
        else:
            while index2 >= 0 and array[index2] < temp:
                array[index2 + 1] = array[index2]
                index2 -= 1
    return array


def merge_sort(array, mid, reverse) -> list:
    """
    merge_sort does sort the array using merge sort algorithm

    :param array: array for sort
    :param mid: middle index of array
    :param reverse: flag for determining the direction of sort
    :return: sorted array
    """
    leftArray = array[:mid]
    rightArray = array[mid : len(array)]
    leftIndex, rightIndex = 0, 0
    if reverse is False:
        # if left array's first value is bigger than right array's last value, swap the position of both arrays
        if leftArray[leftIndex] > rightArray[len(rightArray) - 1]:
            array[mid : len(array)] = leftArray
            array[0:mid] = rightArray
        else:
            try:
                # sort the array with merge sort algorithm
                while True:
                    if leftArray[leftIndex] < rightArray[rightIndex]:
                        array[leftIndex + rightIndex] = leftArray[leftIndex]
                        leftIndex += 1
                    else:
                        array[leftIndex + rightIndex] = rightArray[rightIndex]
                        rightIndex += 1
            except:
                array[leftIndex + rightIndex : len(array)] = (
                    leftArray[leftIndex:] + rightArray[rightIndex:]
                )
    else:
        if leftArray[leftIndex] < rightArray[len(rightArray) - 1]:
            array[mid : len(array)] = leftArray
            array[0:mid] = rightArray
        else:
            try:
                while True:
                    if leftArray[leftIndex] > rightArray[rightIndex]:
                        array[leftIndex + rightIndex] = leftArray[leftIndex]
                        leftIndex += 1
                    else:
                        array[leftIndex + rightIndex] = rightArray[rightIndex]
                        rightIndex += 1
            except:
                array[leftIndex + rightIndex : len(array)] = (
                    leftArray[leftIndex:] + rightArray[rightIndex:]
                )
    return array


def merge(obj) -> list:
    """
    merge does merge the sorry by splitting & joining the array in a unit.
    
    :obj[0]: array for sort
    :obj[1]: unit length
    :obj[2]: flag for determining the direction of sort
    :return: merged array
    """
    array = obj[0]
    runLength = obj[1]
    reverse = obj[2]
    mergeSize = runLength
    arrLength = len(array)
    while mergeSize < len(array):
        left = 0
        for left in range(0, arrLength, 2 * mergeSize):
            mid = left + mergeSize
            right = min(arrLength, left + (2 * mergeSize))
            if mid < right:
                array[left:right] = merge_sort(array[left:right], mid - left, reverse)
        mergeSize = mergeSize * 2
    return array


def sort(array, reverse=False) -> list:
    """
    sort does sort array with reverse flag

    :array: array for sort
    :reverse: flag for determining the direction of sort
    :return: sorted array
    """
    # Use 'multiprocessing.cpu_count()' to determine the number of available CPU cores.
    cpu_count = multiprocessing.cpu_count()
    runLength = run_length(array)
    arrLength = len(array)
    # perform insertion sort on each run
    start = 0
    input = []
    for start in range(0, arrLength, runLength):
        end = min(arrLength, start + runLength)
        input.append([array[start:end], reverse])
    # create pool with n processes for insertion sort
    pool = multiprocessing.Pool(processes=cpu_count)
    array = pool.map(insertion_sort, input)
    pool.close()
    array = [x for y in array for x in y]

    # calculate the item count per pool
    remainder = 0
    if arrLength % runLength != 0:
        remainder = 1

    repeatedCount = arrLength // runLength + remainder
    remainder = 0
    if repeatedCount % cpu_count != 0:
        remainder = 1
    countPerPool = repeatedCount // cpu_count + 1
    
    input = []
    left = 0
    while left < arrLength:
        right = left + countPerPool * runLength
        if right > arrLength:
            right = arrLength
        input.append([array[left:right], runLength, reverse])
        left += countPerPool * runLength
    # create pool with n processes for merge
    pool = multiprocessing.Pool(processes=cpu_count)
    array = pool.map(merge, input)
    pool.close()
    array = [x for y in array for x in y]
    array = merge([array, countPerPool * runLength, reverse])

    return array


if __name__ == "__main__":
    # install random array having 1 million integers
    array = [random.randint(0, 100000) for i in range(1000000)]
    # time track
    start_time = time.perf_counter()
    array = sort(array, True)
    finish_time = time.perf_counter()
    print(
        "Program finished in {} seconds - using multiprocessing".format(
            finish_time - start_time
        )
    )