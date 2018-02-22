import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.interpolate import Rbf


def radix_sort(list1):
    list2 = list(list1)
    t1 = time.time()
    max1 = max(list2)
    exp = 1
    while max1 // exp > 0:
        counting_sort(list2, exp)
        exp *= 10
    t2 = time.time()
    return (t2 - t1) * 1000


def counting_sort(list1, exp):
    t1 = time.time()
    n = len(list1)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = int(list1[i] // exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(list1[i] // exp)
        output[count[index % 10] - 1] = list1[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(list1)):
        list1[i] = output[i]

    t2 = time.time()
    return (t2 - t1) * 1000


def heap_sort(list1):
    list2 = list(list1)
    t1 = time.time()
    n = len(list2)
    for i in range(n, -1, -1):
        heapify(list2, n, i)

    for i in range(n - 1, 0, -1):
        list2[i], list2[0] = list2[0], list2[i]
        heapify(list2, i, 0)
    t2 = time.time()
    return (t2 - t1) * 1000


def heapify(list2, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list2[i] < list2[left]:
        largest = left

    if right < n and list2[largest] < list2[right]:
        largest = right

    if largest != i:
        list2[i], list2[largest] = list2[largest], list2[i]
        heapify(list2, n, largest)


def quick_sort(list2):
    # list2 = list(list1)
    t1 = time.time()
    quick_sort_helper(list2, 0, len(list2) - 1)
    t2 = time.time()
    return (t2 - t1) * 1000


def quick_sort_helper(list2, first, last):
    if first < last:
        split_point = partition(list2, first, last)
        quick_sort_helper(list2, first, split_point - 1)
        quick_sort_helper(list2, split_point + 1, last)


def partition(list2, first, last):
    pivot = list2[first]
    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and list2[left] <= pivot:
            left = left + 1

        while list2[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = list2[left]
            list2[left] = list2[right]
            list2[right] = temp

    temp = list2[first]
    list2[first] = list2[right]
    list2[right] = temp
    return right


def merge_sort(list1):
    list2 = list(list1)
    t1 = time.time()
    if len(list2) > 1:
        mid = len(list2) // 2
        left = list2[:mid]
        right = list2[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list2[k] = left[i]
                i = i + 1
            else:
                list2[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            list2[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            list2[k] = right[j]
            j = j + 1
            k = k + 1
    t2 = time.time()
    return (t2 - t1) * 1000


def insertion_sort(list1):
    list2 = list(list1)
    t1 = time.time()
    for i in range(1, len(list2)):
        value = list2[i]
        while i > 0 and list2[i - 1] > value:
            list2[i] = list2[i - 1]
            i = i - 1
        list2[i] = value
    t2 = time.time()
    return (t2 - t1) * 1000


insertionSortTime = list()
mergeSortTime = list()
quickSortTime = list()
heapSortTime = list()
radixSortTime = list()
for i in range(50, 1001, 50):
    list1 = np.random.random_integers(0, i, i)
    insertionSortTime = np.append(insertionSortTime, insertion_sort(list1))
    mergeSortTime = np.append(mergeSortTime, merge_sort(list1))
    quickSortTime = np.append(quickSortTime, quick_sort(list1))
    heapSortTime = np.append(heapSortTime, heap_sort(list1))
    radixSortTime = np.append(radixSortTime, radix_sort(list1))

numberOfTime = range(50, 1001, 50)
plt1 = plt
plt2 = plt

# ax1 = plt1.subplot(531)
plt1.scatter(numberOfTime, insertionSortTime, alpha=.3, label="Insertion Sort")
plt1.xlabel("number Of Item In List")
plt1.ylabel("Time")
plt1.legend()

# ax2 = plt1.subplot(533)
plt1.scatter(numberOfTime, mergeSortTime, alpha=.3, label="Merge Sort")
plt1.xlabel("number Of Item In List")
plt1.ylabel("Time")
plt1.legend()

# ax3 = plt1.subplot(537)
plt1.scatter(numberOfTime, quickSortTime, alpha=.3, label="QuickSort Sort")
plt1.xlabel("number Of Item In List")
plt1.ylabel("Time")
plt1.legend()

# ax4 = plt1.subplot(539)
plt1.scatter(numberOfTime, heapSortTime, alpha=.3, label="Heap Sort")
plt1.xlabel("number Of Item In List")
plt1.ylabel("Time")
plt1.legend()

# ax5 = plt1.subplot(5, 3, 13)
plt1.scatter(numberOfTime, radixSortTime, alpha=.3, label="Radix Sort")
plt1.xlabel("number Of Item In List")
plt1.ylabel("Time")
plt1.legend()

plt1.show()

rbf1 = Rbf(numberOfTime, insertionSortTime)
y1 = rbf1(numberOfTime)
# ax1 = plt2.subplot(531)
plt2.plot(numberOfTime, y1, alpha=.3, label="Insertion Sort")
plt2.xlabel("number Of Item In List")
plt2.ylabel("Time")
plt2.legend()

rbf2 = Rbf(numberOfTime, mergeSortTime)
y2 = rbf2(numberOfTime)
# ax2 = plt2.subplot(533)
plt2.plot(numberOfTime, y2, alpha=.3, label="Merge Sort")
plt2.xlabel("number Of Item In List")
plt2.ylabel("Time")
plt2.legend()

rbf3 = Rbf(numberOfTime, quickSortTime)
y3 = rbf3(numberOfTime)
# ax3 = plt2.subplot(537)
plt2.plot(numberOfTime, y3, alpha=.3, label="QuickSort Sort")
plt2.xlabel("number Of Item In List")
plt2.ylabel("Time")
plt2.legend()

rbf4 = Rbf(numberOfTime, heapSortTime)
y4 = rbf4(numberOfTime)
# ax4 = plt2.subplot(539)
plt2.plot(numberOfTime, y4, alpha=.3, label="Heap Sort")
plt2.xlabel("number Of Item In List")
plt2.ylabel("Time")
plt2.legend()

rbf5 = Rbf(numberOfTime, radixSortTime)
y5 = rbf5(numberOfTime)
# ax5 = plt2.subplot(5, 3, 13)
plt2.plot(numberOfTime, y5, alpha=.3, label="Radix Sort")
plt2.xlabel("number Of Item In List")
plt2.ylabel("Time")
plt2.legend()

plt2.show()
print("radix = {}".format(radixSortTime))
print("insertion = {}".format(insertionSortTime))
print("heap = {}".format(heapSortTime))
print("quick = {}".format(quickSortTime))
print("merge = {}".format(mergeSortTime))