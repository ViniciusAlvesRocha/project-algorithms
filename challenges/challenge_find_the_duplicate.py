def find_duplicate(nums):
    if validate_nums(nums) is False:
        return False

    nums = quicksort(nums, 0, len(nums) - 1)

    for index, num in enumerate(nums):
        if num == nums[index + 1]:
            return num


def validate_nums(nums):
    validations = {
        "validate_nums_is_zero_or_one": (
            lambda nums: True if len(nums) == 0 or len(nums) == 1 else False),
        "verify_nums_is_string": (
            lambda nums: True if len(
                [num for num in nums if type(num) is str]) > 0 else False),
        "nums_have_negative_number": (
            lambda nums: True if len(
                [num for num in nums if num < 0]) > 0 else False),
        "check_for_duplicate_number": (
            lambda nums: True if len(nums) == len(set(nums)) else False),
    }

    for item_validate in validations:
        if validations[item_validate](nums) is True:
            return False

    verify_list_with_repeated_numbers(nums)


def verify_list_with_repeated_numbers(nums):
    try:
        if len(set(nums)) == 1:
            return nums[0]
    except ValueError:
        return False


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
