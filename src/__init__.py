"""
파이썬 함수 과제 패키지
"""

__version__ = "1.0.1"


from .basic import sum_even, count_words
from .intermediate import sum_of_digits, grade_pass_fail, Problem4Solutions, merge_inventory, Problem5Solutions
from .challenge import two_sum, Problem6Solutions, moving_average, compress_ranges, Problem8Solutions
__all__ = [
    "sum_even", 
    "count_words",
    "sum_of_digits",
    "grade_pass_fail",
    "Problem4Solutions",
    "merge_inventory",
    "Problem5Solutions",
    "two_sum",
    "Problem6Solutions",
    "moving_average",
    "compress_ranges",
    "Problem8Solutions"
]