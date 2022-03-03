def is_palindrome_recursive(word, low_index, high_index):
    if word == "" or word[low_index] != word[high_index]:
        return False
    if low_index < high_index:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True

word = "ANA"
print(is_palindrome_recursive(word, 0, len(word) - 1))
# saída: True

word = "SOCOS"
print(is_palindrome_recursive(word, 0, len(word) - 1))
# saída: True

word = "REVIVER"
print(is_palindrome_recursive(word, 0, len(word) - 1))
# saída: True

word = "COXINHA"
print(is_palindrome_recursive(word, 0, len(word) - 1))
# saída: False

word = "AGUA"
print(is_palindrome_recursive(word, 0, len(word) - 1))
# saída: False