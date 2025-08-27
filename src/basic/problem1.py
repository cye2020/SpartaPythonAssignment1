from typing import List

def sum_even(numbers: List[int]) -> int:
    """ 짝수의 합 구하는 함수
    
    Args:
        numbers (List[int]): 정수 리스트
    
    Returns:
        int: 짝수들의 합
    """
    answer = sum(num for num in numbers if num % 2 == 0)
    return answer