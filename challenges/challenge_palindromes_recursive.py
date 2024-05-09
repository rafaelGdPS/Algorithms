def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if high_index <= low_index:
        return True
    elif word[low_index].lower() == word[high_index].lower():
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
