from typing import List

def compress_ranges(nums: List[int]) -> str:
    """ 숫자 구간 압축하는 함수
    
    Args:
        nums (List[int]): 정수 리스트
    
    Returns:
        str: 압축된 구간 문자열
    """
    answer = []
    nums.append(1)
    start = end = nums[0]
    for x in nums[1:]:
        if x == end + 1:
            end = x
        else:
            answer.append(f"{start}-{end}" if start != end else f"{start}")
            start = end = x
    answer = ','.join(answer)
    return answer


def compress_ranges_v1(nums: List[int]) -> str:
    """
    반환값 예: "1-3,5,7-9"
    """
    answer = [] 
    nums.append(1)
    start = end = nums[0]
    for x in nums[1:]:
        if x == end + 1:
            end = x
        else:
            answer.append(f"{start}-{end}" if start != end else f"{start}")
            start = end = x
    answer = ','.join(answer)
    return answer


def compress_ranges_v2(nums: List[int]) -> str:
    """
    반환값 예: "1-3,5,7-9"
    """
    # 여기에 코드를 작성하세요
    cursor = float('inf')
    groups: List[list] = []
    for num in nums:
        if num == cursor:
            groups[-1].append(num)
        else:
            cursor = num
            groups.append([num])
        cursor += 1
    
    answer = ','.join(['-'.join(map(str, sorted(set([group[0], group[-1]])))) for group in groups])
    return answer


class Problem8Solutions:
    """Problem 8 솔루션들을 관리하는 클래스"""
    
    # 솔루션들
    SOLUTIONS = [compress_ranges_v1, compress_ranges_v2]
    
    # 메타데이터
    INFO = {
        compress_ranges_v1: {
            "name": "Two Pointers",
            "description": "두 포인터를 이용한 방식",
            "pros": "효율적이고 직관적임",
            "cons": "약간 장황할 수 있음"
        },
        compress_ranges_v2: {
            "name": "Grouping", 
            "description": "그룹화를 이용한 방식",
            "pros": "코드가 간결함",
            "cons": "조금 덜 직관적일 수 있음"
        },
    }
    
    DEFAULT = compress_ranges_v1
    
    @classmethod
    def get_solution_name(cls, func):
        """솔루션 함수의 이름을 반환"""
        return cls.INFO.get(func, {}).get("name", "Unknown Solution")
    
    @classmethod
    def get_solutions(cls):
        """모든 솔루션 함수 리스트를 반환"""
        return cls.SOLUTIONS.copy()