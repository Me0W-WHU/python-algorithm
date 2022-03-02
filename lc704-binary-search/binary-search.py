from typing import List


def search(nums: List[int], target: int) -> int:
    head = 0
    tail = len(nums)
    while head != tail:
        p = head + (tail - head) // 2
        if nums[p] == target:
            return p
        elif nums[p] > target:
            tail = p
        elif nums[p] < target:
            head = p + 1
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
