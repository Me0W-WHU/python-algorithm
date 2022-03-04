https://leetcode-cn.com/problems/rotate-array/
### solution 1: extend & slice

- This is quite straightforward in Python, but probably not in C++

### solution 2: slice & concat  
- fastest solution in python

### solution 3: reverse'em!

- O(1) space complexity. Probably the best solution, but not very intuitive.
    - Yeah, theoretically. but the reality in Python is that solution 3 might consume even more space than solution 1 & 2.

1. Originally

you get: -------> --->

2. Reverse all

you get: <--- <-------

3. Reverse two parts respectively

you get: ---> ------->

And there you are! ; )

### solution 4: loop swaping

- A solution just as good as solution 3. More complicated but also more intuitive.
- Depending on n and k, you might need to take multiple loops, the number of the loops can be denoted as follows:

$$
l = gcd(n, k)
$$

- ... And a concise implementation of gcd (greatest common divisor) algorithm is included in this solution:
```python
def gcd(a: int, b: int) -> int:
    while a != 0:
        a, b = b % a, a
    return b
```

---
- Don't forget to do the following operation in advance:
```python
k = k % n
```

- Use this line to assign one list to another:

```python
nums[:] = temp[:]
```