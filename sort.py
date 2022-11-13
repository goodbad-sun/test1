def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


"""选择排序"""


def selectSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = 1
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1


def bubblesort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1


def bubblesortwithtweak(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped:
            return
        n -= 1


def insertSort(lyst):
    """插入排序，第i轮找到的最大值应该插入到第i项"""
    i = 1
    while i < len(lyst):
        itemtoinsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemtoinsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemtoinsert
        i += 1
