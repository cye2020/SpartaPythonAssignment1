"""
Problem 3: sum_of_digits 함수 테스트
문자열 속 숫자 합 구하기
"""

import pytest
from src.intermediate.problem3 import sum_of_digits


class TestSumOfDigits:
    """sum_of_digits 함수 테스트"""
    
    # 테스트 케이스 1: 기본 케이스 입력
    @pytest.mark.parametrize("text, expected, description", [
        ("a1b23c004", 10, "알파벳과 숫자가 섞인 경우"),
        ('Hello', 0, "숫자가 없는 경우"),
        ("9-9=0", 18, "특수문자 포함"),
    ])
    @pytest.mark.basic
    @pytest.mark.problem3
    def test_basic_cases(self, text, expected, description):
        """기본 테스트 케이스"""
        result = sum_of_digits(text)
        assert result == expected, f"Failed: {description}"

    # 테스트 케이스 2: 엣지 케이스 입력
    @pytest.mark.parametrize("text, expected, description", [
        ("00000", 0, "0만 있는 경우"),
        ("2468", 20, "짝수만 있는 경우"),
        ("ver1fy0007", 8, ""), # 해결: 기본 1과 유사
        ("1\n2\t3", 6, "특수문자가 있는 경우"),
    ])
    @pytest.mark.edge
    @pytest.mark.problem3
    def test_edge_cases(self, text, expected, description):
        """엣지 테스트 케이스"""
        result = sum_of_digits(text)
        assert result == expected, f"Failed: {description}"
    
    # 테스트 케이스 3: 코너 케이스 입력
    @pytest.mark.parametrize("text, expected, description", [
        ("a9"*50, 450, "많은 경우"),
    ])
    @pytest.mark.corner
    @pytest.mark.problem3
    def test_corner_cases(self, text, expected, description):
        """코너 테스트 케이스"""
        result = sum_of_digits(text)
        assert result == expected, f"Failed: {description}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])