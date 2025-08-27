from typing import Dict
from collections import Counter

def grade_pass_fail(scores: Dict[str, int], threshold=60) -> Dict[str, int]:
    """ 합격 / 불합격 집계하는 함수
    
    Args:
        scores (Dict[str, int]): 학생 이름과 점수 딕셔너리
        threshold (int, optional): 합격 기준 점수. Defaults to 60.
    
    Returns:
        Dict[str, int]: 합격자 수와 불합격자 수를 담은 딕셔너리
    """
    answer = {'pass': 0, 'fail': 0}
    for score in scores.values():
        if score >= threshold:
            answer['pass'] += 1
        else:
            answer['fail'] += 1
    return answer


def grade_pass_fail_v1(scores: Dict[str, int], threshold=60) -> Dict[str, int]:
    """
    반환값 예: {'pass': 2, 'fail': 2}
    """
    # 여기에 코드를 작성하세요
    answer = {'pass': 0, 'fail': 0}
    for score in scores.values():
        if score >= threshold:
            answer['pass'] += 1
        else:
            answer['fail'] += 1
    return answer


def grade_pass_fail_v2(scores: Dict[str, int], threshold=60) -> Dict[str, int]:
    """
    반환값 예: {'pass': 2, 'fail': 2}
    """
    # 여기에 코드를 작성하세요
    answer = {'pass': 0, 'fail': 0}
    grades = dict(Counter('pass' if score >= threshold else 'fail' for score in scores.values()))
    answer.update(grades)
    return answer


def grade_pass_fail_v3(scores: Dict[str, int], threshold=60) -> Dict[str, int]:
    """
    반환값 예: {'pass': 2, 'fail': 2}
    """
    # 여기에 코드를 작성하세요
    answer = {'pass': 0, 'fail': 0}
    grades = [1 if score >= threshold else 0 for score in scores.values()]
    answer['pass'] = sum(grades)
    answer['fail'] = len(grades) - answer['pass']
    return answer

class Problem4Solutions:
    """Problem 4 솔루션들을 관리하는 클래스"""
    
    # 솔루션들
    SOLUTIONS = [grade_pass_fail_v1, grade_pass_fail_v2, grade_pass_fail_v3]
    
    # 메타데이터
    INFO = {
        grade_pass_fail_v1: {
            "name": "For Loop",
            "description": "전통적인 for 루프 방식",
            "pros": "가독성 좋음, 이해하기 쉬움",
            "cons": "다소 장황함"
        },
        grade_pass_fail_v2: {
            "name": "Counter", 
            "description": "Counter를 쓴 방식",
            "pros": "간결함",
            "cons": "초보자에게 어려울 수 있음"
        },
        grade_pass_fail_v3: {
            "name": "List Comprehension", 
            "description": "리스트 컴프리헨션을 쓴 방식",
            "pros": "간결함",
            "cons": "가독성이 떨어질 수 있음"
        }
    }
    
    # 기본 함수 지정
    DEFAULT = grade_pass_fail_v1
    
    @classmethod
    def get_solution_name(cls, func):
        """솔루션 이름 반환"""
        return cls.INFO.get(func, {}).get("name", "Unknown Solution")
    
    @classmethod
    def get_all_solutions(cls):
        """모든 솔루션 반환"""
        return cls.SOLUTIONS.copy()