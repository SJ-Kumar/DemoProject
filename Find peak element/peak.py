def findPeakelement(arr, lowerrange, upperrange, n):
    mid = lowerrange + (upperrange - lowerrange)/2
    mid = int(mid)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
    elif (mid > 0 and arr[mid + 1] > arr[mid]):
        return findPeakelement(arr, (mid + 1), upperrange, n)

    else:
        return findPeakelement(arr, lowerrange, (mid - 1), n)


arr = [3,6,19,34,98,105]
n = len(arr)
print("The peak value in the given array is", arr[findPeakelement(arr, 0, n - 1, n)])