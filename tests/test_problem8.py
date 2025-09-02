"""
Problem 8: compress_ranges 함수 테스트
숫자 구간 압축하기
"""

import pytest
from src.challenge.problem8 import Problem8Solutions
from copy import deepcopy

class TestCompressRangesBasic:
    """기본 케이스 테스트"""
    @pytest.mark.parametrize("solution_func", Problem8Solutions.SOLUTIONS)
    @pytest.mark.parametrize("nums, expected, description", [
        (
            [1, 2, 3, 5, 7, 8, 9], 
            "1-3,5,7-9",
            "연속된 구간과 단일 숫자가 혼합된 경우"
        ),
        (
            [1, 3, 5, 7, 9],
            "1,3,5,7,9",
            "연속된 구간이 없는 경우"
        ),
        (
            [1, 2, 3, 4],
            "1-4",
            "모든 숫자가 연속된 구간인 경우"
        )
    ])
    @pytest.mark.basic
    @pytest.mark.problem8
    def test_basic_cases(self, solution_func, nums, expected, description):
        nums_data = deepcopy(nums)
        result = solution_func(nums_data)
        solution_name = Problem8Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


class TestCompressRangesEdge:
    """엣지 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem8Solutions.SOLUTIONS)
    @pytest.mark.parametrize("nums, expected, description", [
        (
            [],
            '',
            "빈 리스트인 경우"
        ),
        (
            [42],
            '42',
            "두 자리수 이상의 숫자가 있는 경우"
        ),
        (
            [0, 2, 3, 4, 10, 11, 15],
            "0,2-4,10-11,15",
            "0이 포함된 경우"
        ),
        (
            [-2, -1, 0, 1, 3],
            "-2-1,3",
            "음수 값으로 시작하는 경우"
        ),
        (
            [-5, -3, -2, -1],
            '-5,-3--1',
            '음수 값으로 끝나는 경우'
        ),
    ])
    @pytest.mark.edge
    @pytest.mark.problem8
    def test_edge_cases(self, solution_func, nums, expected, description):
        nums_data = deepcopy(nums)
        result = solution_func(nums_data)
        solution_name = Problem8Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


class TestCompressRangesCorner:
    """코너 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem8Solutions.SOLUTIONS)
    @pytest.mark.parametrize("nums, expected, description", [
        (
            [5, 6],
            "5-6",
            "두 개의 연속된 숫자만 있는 경우"
        ),
        (
            [5, 7],
            "5,7",
            "두 개의 비연속된 숫자만 있는 경우"
        ),
    ])
    @pytest.mark.corner
    @pytest.mark.problem8
    def test_corner_cases(self, solution_func, nums, expected, description):
        nums_data = deepcopy(nums)
        result = solution_func(nums_data)
        solution_name = Problem8Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])