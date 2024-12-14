class binarySearch:

    def findMatch(list, item):
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]
            if guess == item:
                return mid
            if item > guess:
                low = mid + 1
            else:
                high = mid - 1

        return None
    print(findMatch([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 70))
        