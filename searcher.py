def indexOfMin(lyst):
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex == currentIndex
        currentIndex += 1
    return minIndex


def sequentialSearch(target, lyst):
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1


def binarySearch(target, sortlyst):
    left = 0
    right = len(sortlyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortlyst[midpoint]:
            return midpoint
        elif target < sortlyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


class SavingsAccount(object):
    """构造器"""

    def __init__(self, name, pin, balance=0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __lt__(self, other):
        return self._name < other._name

    def __gt__(self, other):
        return self._name > other._name

    def __eq__(self, other):
        return self._name == other._name
