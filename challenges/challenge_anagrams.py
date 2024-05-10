def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first = change_in_list(first_string)
    second = change_in_list(second_string)

    merge_sort(first)
    merge_sort(second)

    if first == second:
        return ("".join(first), "".join(second), True)

    else:
        return ("".join(first), "".join(second), False)


def change_in_list(word):
    word_list = [letter.lower() for letter in word]
    return word_list


def merge_sort(letters, start=0, end=None):
    if end is None:
        end = len(letters)

    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(letters, start, mid)
        merge_sort(letters, mid, end)
        merge(letters, start, mid, end)


def merge(letters, start, mid, end):
    left = letters[start:mid]
    right = letters[mid:end]

    left_index, right_index = 0, 0

    for index in range(start, end):
        if left_index >= len(left):
            letters[index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            letters[index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            letters[index] = left[left_index]
            left_index = left_index + 1

        else:
            letters[index] = right[right_index]
            right_index = right_index + 1
