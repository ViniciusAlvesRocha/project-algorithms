def find_duplicate(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False

    for num in nums:
        if type(num) is str:
            return False

    if len([num for num in nums if num < 0]) > 0:
        return False

    nums = quicksort(nums, 0, len(nums) - 1)
    try:
        if len(set(nums)) == 1:
            return nums[0]
    except ValueError:
        return False

    if len(nums) == len(set(nums)):
        return False

    for index, num in enumerate(nums):
        if num == nums[index + 1]:
            return num

def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)
        return array


def partition(array, low, high):
    i = low - 1
    pivot = array[high]  # pivot

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

# print(find_duplicate(["a", "b"]))