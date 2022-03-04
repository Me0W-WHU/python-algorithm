from typing import List


def gcd(a: int, b: int) -> int:
    while a != 0:
        a, b = b % a, a
    return b


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    d = gcd(n, k)
    for i in range(0, d):
        temp = nums[i]
        for j in range(1, n // d):
            nums[i] = nums[(i + j * k) % n]
            nums[(i + j * k) % n] = temp
            temp = nums[i]


nums1 = [1, 2, 3, 4, 5, 6, 7]
rotate(nums1, 3)
print(nums1)
