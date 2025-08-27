"""
Problem 5: merge_inventory 함수 테스트
입고 반영한 재고 합치기
"""

import pytest
from src.intermediate.problem5 import Problem5Solutions
from copy import deepcopy

class TestMergeInventoryBasic:
    """기본 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem5Solutions.SOLUTIONS)
    @pytest.mark.parametrize("current, arrival, expected, description", [
        (
            {"apple": 5, "banana": 2, "milk": 1},
            {"banana": 3, "bread": 4, "milk": 2}, 
            {"apple": 5, "banana": 5, "milk": 3, "bread": 4},
            "기본 케이스"
        ),
    ])
    @pytest.mark.basic
    @pytest.mark.problem5
    def test_basic_cases_all_solutions(self, solution_func, current, arrival, expected, description):
        current_data = deepcopy(current)
        arrival_data = deepcopy(arrival)
        result = solution_func(current_data, arrival_data)
        solution_name = Problem5Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


class TestMergeInventoryEdge:
    """엣지 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem5Solutions.SOLUTIONS)
    @pytest.mark.parametrize("current, arrival, expected, description", [
        (
            {},
            {"a": 1},
            {"a": 1},
            "빈 딕셔너리에 하나 추가하는 경우"
        ),
        (
            {"a": 1},
            {},
            {"a": 1},
            "빈 딕셔너리를 추가하는 경우"
        ),
        (
            {"a": 1},
            {"b": 2},
            {"a": 1, "b": 2},
            "서로 다른 키를 가진 딕셔너리를 합치는 경우"
        ),
        (
            {"a": 0},
            {"a": 0},
            {"a": 0},
            "값이 0인 항목을 합치는 경우"
        ),
        (
            {"a": 5},
            {"a": -2},
            {"a": 3},
            "값이 음수인 항목을 합치는 경우"
        ),
    ])
    @pytest.mark.edge
    @pytest.mark.problem5
    def test_edge_cases_all_solutions(self, solution_func, current, arrival, expected, description):
        current_data = deepcopy(current)
        arrival_data = deepcopy(arrival)
        result = solution_func(current_data, arrival_data)
        solution_name = Problem5Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"

class TestMergeInventoryCorner:
    """코너 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem5Solutions.SOLUTIONS)
    @pytest.mark.parametrize("current, arrival, expected, description", [
        (
            {"item"+str(i): i for i in range(1000)},
            {"item"+str(i): i for i in range(500, 1500)},
            {**{"item"+str(i): i for i in range(500)}, **{"item"+str(i): i*2 for i in range(500, 1000)}, **{"item"+str(i): i for i in range(1000, 1500)}},
            "매우 큰 딕셔너리를 합치는 경우"
        ),
    ])
    @pytest.mark.corner
    @pytest.mark.problem5
    def test_corner_cases_all_solutions(self, solution_func, current, arrival, expected, description):
        current_data = deepcopy(current)
        arrival_data = deepcopy(arrival)
        result = solution_func(current_data, arrival_data)
        solution_name = Problem5Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])