from functools import cmp_to_key

# Custom comparison function
def compare(a, b):
    if a + b > b + a:
        return -1  # a should come before b
    elif a + b < b + a:
        return 1  # b should come before a
    else:
        return 0  # a and b are considered equal


# In Python, when you're writing a comparison function for sorting (often using cmp_to_key), you need to return:

# -1 if the first element should come before the second element,
# 1 if the first element should come after the second element,
# 0 if both elements are considered equal in terms of sorting.

# problem https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18
