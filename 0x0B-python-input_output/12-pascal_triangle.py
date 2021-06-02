
#!/usr/bin/python3
"""
For this function you have to put a file and a text as arguments.

Use this function wizely.
"""


def pascal_triangle(n):
    """
    Function that writes over a file
    """
    if n <= 0:
        return []
    
    for i in range(0, n + 1):
        n = 1
        for j in range(0, i + 1):
            print("{} ".format(n), end='')
            n = n * (i - j) / (j + 1)
        print()
        