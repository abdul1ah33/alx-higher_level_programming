def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    if size == 0:
        return None

    left = 0
    right = size - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and (mid == size - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        # If the left neighbor is greater, then the peak is in the left half
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1

    return None

# Test cases
print(find_peak([1, 2, 4, 6, 3]))  # Output: 6
print(find_peak([4, 2, 1, 2, 3, 1]))  # Output: 3 or 4
print(find_peak([2, 2, 2]))  # Output: 2
print(find_peak([]))  # Output: None
print(find_peak([-2, -4, 2, 1]))  # Output: 2
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4 or 3
