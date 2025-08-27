from typing import Dict
from collections import defaultdict


def merge_inventory_v1(current: Dict[str, int], arrival: Dict[str, int]) -> Dict[str, int]:
    """ 입고 반영한 재고 합치는 함수
    
    Args:
        current (Dict[str, int]): 현재 재고
        arrival (Dict[str, int]): 입고된 재고
    
    Returns:
        Dict[str, int]: 합쳐진 재고
    """
    for item, qty in arrival.items():
        current[item] = current.get(item, 0) + qty
    return current

def merge_inventory_v2(current: Dict[str, int], arrival: Dict[str, int]) -> Dict[str, int]:
    """
    반환값 예: {'apple': 5, 'banana': 5, 'milk': 3, 'bread': 4}
    """
    # 여기에 코드를 작성하세요
    answer = defaultdict(int, current)
    for item, qty in arrival.items():
        answer[item] += qty
    return dict(answer)


def merge_inventory(current: Dict[str, int], arrival: Dict[str, int]) -> Dict[str, int]:
    """
    반환값 예: {'apple': 5, 'banana': 5, 'milk': 3, 'bread': 4}
    """
    # 여기에 코드를 작성하세요
    for item, qty in arrival.items():
        current[item] = current.get(item, 0) + qty
    return current


class Problem5Solutions:
    """Problem 5 솔루션들을 관리하는 클래스"""
    
    # 솔루션들
    SOLUTIONS = [merge_inventory_v1, merge_inventory_v2]
    
    # 메타데이터
    INFO = {
        merge_inventory_v1: {
            "name": "Dict Get",
            "description": "dict.get() 메서드를 사용한 방식",
            "pros": "간결하고 직관적임",
            "cons": "없음"
        },
        merge_inventory_v2: {
            "name": "DefaultDict",
            "description": "collections.defaultdict를 사용한 방식",
            "pros": "코드가 깔끔해짐",
            "cons": "defaultdict 개념을 알아야 함"
        }
    }
    
    DEFAULT = merge_inventory_v1
    
    @classmethod
    def get_solution_name(cls, func):
        """솔루션 이름 반환"""
        return cls.INFO.get(func, {}).get("name", "Unknown Solution")
    
    @classmethod
    def get_all_solutions(cls):
        """모든 솔루션 반환"""
        return cls.SOLUTIONS.copy()