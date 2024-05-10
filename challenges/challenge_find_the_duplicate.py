def find_duplicate(nums):
    if not nums or len(nums) <= 1:
        return False

    new_list = sorted(nums)

    for num in new_list:
        if num < 0:
            return False
        new_list.remove(num)
        if find_num(new_list, num) != -1:
            return num
    return False


def find_num(nums, target):
    start = 0
    end = len(nums)

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
