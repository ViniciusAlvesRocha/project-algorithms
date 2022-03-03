from challenges.quicksort import quicksort


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_string = [ord(character) for character in first_string]
    second_string = [ord(character) for character in second_string]
    first_string = quicksort(first_string, 0, len(first_string) - 1)
    second_string = quicksort(second_string, 0, len(second_string) - 1)
    return first_string == second_string
