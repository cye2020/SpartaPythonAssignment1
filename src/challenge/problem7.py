from typing import List

def moving_average(data: List[int], k: int) -> List[float]:
    """ 이동 평균 구하는 함수 (슬라이딩 윈도우)
    
    Args:
        data (List[int]): 정수 리스트
        k (int): 윈도우 크기
        
    Returns:
        List[float]: 이동 평균 리스트
    """
    answer = []
    if len(data) >= k > 0:
        answer = [round(sum(data[i: i+k]) / k, 1) for i in range(len(data) - k + 1)]
    return answer