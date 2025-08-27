def sum_of_digits(text: str) -> int:
    """ 문자열 속 숫자 합 구하는 함수
    Args:
        text (str): 문자열
    
    Returns:
        int: 숫자들의 합
    """
    answer = sum(int(char) for char in text if char.isdigit())
    return answer