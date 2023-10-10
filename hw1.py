"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than the other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple
import collections


def major_and_minor_elem(given_list: List[int]) -> Tuple[int, int]:
    least_common = collections.Counter(given_list).most_common()[-1][0]
    most_common = collections.Counter(given_list).most_common()[0][0]
    return most_common, least_common

