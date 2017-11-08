# -*- coding: utf-8 -*-
"""
some sort algorithms
"""

def quick_sort(nums):
    pass


def quick_sort_dutch_flag(nums):
    if not nums or len(nums) <= 1:
        return
    _dutch_sort(nums, 0, len(nums) - 1)

def _dutch_sort(nums, left, right):
    next_left, next_right = _dutch_flag_partition(nums, left, right)
    if next_left > left:
        _dutch_sort(nums, left, next_left)
    if next_right < right:
        _dutch_sort(nums, next_right, right)


def _dutch_flag_partition(nums, left, right):
    if left >= right:
        return left, right
    i = left - 1
    j = right + 1
    k = left
    pivot = nums[left]
    while i < k < j:
        if nums[k] < pivot:
            i = i + 1
            nums[i], nums[k] = nums[k], nums[i]
        elif nums[k] > pivot:
            j = j - 1
            nums[j], nums[k] = nums[k], nums[j]
        else:
            k += 1

    return i, j




def merge_sort(nums):
    pass


def heap_sort(nums):
    pass


if __name__ == '__main__':
    nums = [0]
    quick_sort_dutch_flag(nums)
    print nums