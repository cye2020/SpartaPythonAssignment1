"""
Problem 6: two_sum 함수 테스트
두 수의 합(인덱스 반환)
"""

import pytest
from src.challenge.problem6 import Problem6Solutions
from copy import deepcopy

class TestTwoSumBasic:
    """기본 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem6Solutions.SOLUTIONS)
    @pytest.mark.parametrize("nums, target, expected, description", [
        (
            [2, 7, 11, 15],
            9, 
            [(0, 1)],
            "합을 만들 수 있는 경우"
        ),
        (
            [2, 7, 11, 15],
            10,
            [(-1, -1)],
            "합을 만들 수 없는 경우"
        )
    ])
    @pytest.mark.basic
    @pytest.mark.problem6
    def test_basic_cases_all_solutions(self, solution_func, nums, target, expected, description):
        nums_data = deepcopy(nums)
        target_data = deepcopy(target)
        result = solution_func(nums_data, target_data)
        solution_name = Problem6Solutions.get_solution_name(solution_func)
        assert result in expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


class TestTwoSumEdge:
    """엣지 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem6Solutions.SOLUTIONS)
    @pytest.mark.parametrize("nums, target, expected, description", [
        (
            [3, 3],
            6,
            [(0, 1)],
            "같은 숫자가 두 개 있는 경우"
        ),
        (
            [0, 4, 3, 0],
            0,
            [(0, 3)],
            "0이 포함된 경우"
        ),
        (
            [-1, 0, 1, 2],
            1,
            [(1, 2), (0, 3)],
            "음수가 포함된 경우"
        ),
        (
            [-5, -2, -3, -4],
            -7,
            [(0, 1)],
            "모든 숫자가 음수인 경우"
        ),
        (
            [5, 5, 1],
            10,
            [(0, 1)],
            "중복된 수와 다른 수가 섞여있고 하나만 정답인 경우"
        ),
        (
            [1, 2, 3, 4],
            7,
            [(2, 3)],
            '맨 끝 두 수의 합이 타겟인 경우'
        ),
        (
            [],
            5,
            [(-1, -1)],
            "빈 리스트인 경우"
        ),
        (
            [7],
            7,
            [(-1, -1)],
            "원소가 하나인 경우"
        ),
        (
            [1, 2, 3, 4, 5],
            6,
            [(0, 4), (1, 3)],
            "양수인 리스트에서 다양한 답이 있는 경우"
        )
    ])
    @pytest.mark.edge
    @pytest.mark.problem6
    def test_edge_cases_all_solutions(self, solution_func, nums, target, expected, description):
        nums_data = deepcopy(nums)
        target_data = deepcopy(target)
        result = solution_func(nums_data, target_data)
        solution_name = Problem6Solutions.get_solution_name(solution_func)
        assert result in expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"

class TestTwoSumCorner:
    """코너 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem6Solutions.SOLUTIONS)
    @pytest.mark.parametrize("nums, target, expected, description", [
        (
            [1, 3, 1, 2, 1],
            2,
            [(0, 2)],
            "반복된 숫자가 많은 경우"
        ),
        (
            [10**6, 3, 10**6-3],
            10**6,
            [(1, 2)],
            "매우 큰 수가 포함된 경우"
        )
    ])
    @pytest.mark.corner
    @pytest.mark.problem6
    def test_corner_cases_all_solutions(self, solution_func, nums, target, expected, description):
        nums_data = deepcopy(nums)
        target_data = deepcopy(target)
        result = solution_func(nums_data, target_data)
        solution_name = Problem6Solutions.get_solution_name(solution_func)
        assert result in expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])