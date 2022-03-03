def is_palindrome_iterative(word):
    if word == "":
        return False
    if len(word) == 1:
        return True
    high_index = len(word) - 1
    for character in word:
        if character != word[high_index]:
            return False
        high_index -= 1
    return True
