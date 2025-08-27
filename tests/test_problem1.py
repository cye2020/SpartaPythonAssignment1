"""
Problem 1: sum_even 함수 테스트
짝수의 합 구하기
"""

import pytest
from src.basic.problem1 import sum_even


class TestSumEven:
    """sum_even 함수 테스트"""
    
    # 테스트 케이스 1: 기본 케이스 입력
    @pytest.mark.parametrize("numbers, expected, description", [
        ([3000, 7000, 2000, 8000, 5000, 10000, 11000], 46000, "큰 숫자들이 섞인 경우"),
        ([2, 4, 6], 12, "작은 짝수들"),
        ([1, 3, 5], 0, "홀수만 있는 경우"),
    ])
    @pytest.mark.basic
    @pytest.mark.problem1
    def test_basic_cases(self, numbers, expected, description):
        """기본 테스트 케이스"""
        result = sum_even(numbers)
        assert result == expected, f"Failed: {description}"

    # 테스트 케이스 2: 엣지 케이스 입력
    @pytest.mark.parametrize("numbers, expected, description", [
        ([], 0, "빈 리스트"),
        ([0], 0, "0만 있는 경우"),
        ([0, 1, 2, 3], 2, "0을 포함한 혼합"),
        ([-2, -3, -4], -6, "음수 포함"),
    ])
    @pytest.mark.edge
    @pytest.mark.problem1
    def test_edge_cases(self, numbers, expected, description):
        """엣지 테스트 케이스"""
        result = sum_even(numbers)
        assert result == expected, f"Failed: {description}"
    
    # 테스트 케이스 3: 코너 케이스 입력
    @pytest.mark.parametrize("numbers, expected, description", [
        ([10**6, 10**6 + 1], 10**6, "큰 수"),
        ([2], 2, "단일 짝수"),
        ([3], 0, "단일 홀수"),
    ])
    @pytest.mark.corner
    @pytest.mark.problem1
    def test_corner_cases(self, numbers, expected, description):
        """코너 테스트 케이스"""
        result = sum_even(numbers)
        assert result == expected, f"Failed: {description}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])