from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """ 두 수의 합이 target이 되는 인덱스 쌍을 찾는 함수
    
    Args:
        nums (List[int]): 정수 리스트
        target (int): 목표 합
    
    Returns:
        Tuple[int, int]: 두 수의 인덱스 쌍, 없으면 (-1, -1)
    """
    num_dict = {}
    answer = (-1, -1)
    for i, num in enumerate(nums):
        if num_dict.get(target - num) is not None:
            answer = (num_dict[target - num], i)
            break
        else:
            num_dict[num] = i
    return answer

def two_sum_v1(nums: List[int], target: int) -> Tuple[int, int]:
    """
    반환값 예: (0, 1)  # nums[0] + nums[1] = 9
    """
    # 여기에 코드를 작성하세요
    num_dict = {}
    answer = (-1, -1)
    for i, num in enumerate(nums):
        if num_dict.get(target - num) is not None:
            answer = (num_dict[target - num], i)
            break
        else:
            num_dict[num] = i
    return answer

def two_sum_v2(nums: List[int], target: int) -> Tuple[int, int]:
    """
    반환값 예: (0, 1)  # nums[0] + nums[1] = 9
    """
    # 여기에 코드를 작성하세요
    for i in range(len(nums)):
        try:
            j = nums.index(target - nums[i], i + 1)
            answer = (i, j)
            break
        except ValueError:
            pass
    else:
        answer = (-1, -1)
    return answer


class Problem6Solutions:
    """Problem 6 솔루션들을 관리하는 클래스"""
    
    # 솔루션들
    SOLUTIONS = [two_sum_v1, two_sum_v2]
    
    # 메타데이터
    INFO = {
        two_sum_v1: {
            "name": "Hash Map",
            "description": "해시 맵을 사용한 방식",
            "pros": "시간 복잡도 O(n)",
            "cons": "추가 공간 필요"
        },
        two_sum_v2: {
            "name": "Brute Force with Index",
            "description": "내장 index() 메서드를 사용한 완전 탐색 방식",
            "pros": "코드가 간결함",
            "cons": "시간 복잡도 O(n^2)"
        }
    }
    
    DEFAULT = two_sum_v1
    
    
    @classmethod
    def get_solution_name(cls, func):
        """솔루션 이름 반환"""
        return cls.INFO.get(func, {}).get("name", "Unknown Solution")
    
    @classmethod
    def get_all_solutions(cls):
        """모든 솔루션 반환"""
        return cls.SOLUTIONS.copy()