def is_palindrome_iterative(word):
    if word == "":
        return False
    for index in range(len(word) // 2):
        if word[index] != word[-index - 1]:
            return False
    return True
