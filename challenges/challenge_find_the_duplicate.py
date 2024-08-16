def find_duplicate(nums):
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
    new_list = sorted(nums)
    for num in range(len(new_list) - 1):
        if new_list[num] == new_list[num + 1]:
            return new_list[num]

    return False
