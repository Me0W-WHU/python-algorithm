- Use a head and tail pointer to indicate current search area.
- Design the loop condition carefully according to your definition of head and tail pointer. The search should end when the length of the search area is 0.
    - Generally speaking, you should not allow the loop to stop when there's one element left. Because some cases won't hit this condition and it often requires unnecessary extra checks
- You **must not** move the head pointer to an accessed element by any circumstances, as this may cause that element to be accessed over and over again and lead to an endless loop. It's fine to move the tail pointer to the accessed element though.
- The // operation in python is for integer division.

```python
3 // 2
# output: 1
```

- When calculating the mid pointer, use the following expression to avoid overflow (in C/C++ environment) as well as speeding up the program.

```python
mid = head + (tail - head) // 2
```