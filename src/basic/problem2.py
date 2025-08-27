def count_words(text: str) -> int:
    """ 문장 속 단어 개수 세는 함수
    Args:
        text (str): 문자열
    
    Returns:
        int: 단어 개수
    """
    answer = len(text.split())
    return answer