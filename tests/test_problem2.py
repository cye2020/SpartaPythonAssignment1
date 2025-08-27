"""
Problem 2: count_words 함수 테스트
문장 속 단어 개수 세기
"""

import pytest
from src.basic.problem2 import count_words


class TestCountWords:
    """count_words 함수 테스트"""
    
    # 테스트 케이스 1: 기본 케이스 입력
    @pytest.mark.parametrize("text, expected, description", [
        ("  hello   world  python  ", 3, "많은 공백이 섞인 경우"),
        ('hello', 1, "단일 단어"),
        ("", 0, "빈 문자열"),
    ])
    @pytest.mark.basic
    @pytest.mark.problem2
    def test_basic_cases(self, text, expected, description):
        """기본 테스트 케이스"""
        result = count_words(text)
        assert result == expected, f"Failed: {description}"

    # 테스트 케이스 2: 엣지 케이스 입력
    @pytest.mark.parametrize("text, expected, description", [
        ("   ", 0, "공백만 있는 경우"),
        ("a\nb\tc", 3, "특수 문자 포함"),
        ("  a \n  b\t   ", 2, "공백과 특수 문자 혼합"),
        ("Hello, world!", 2, "공백 하나로 구분"),
        ("데이터 분석 입문", 3, "한글 단어"),
        ("Hello,world", 1, "쉼표로 연결된 한 단어")
    ])
    @pytest.mark.edge
    @pytest.mark.problem2
    def test_edge_cases(self, text, expected, description):
        """엣지 테스트 케이스"""
        result = count_words(text)
        assert result == expected, f"Failed: {description}"
    
    # 테스트 케이스 3: 코너 케이스 입력
    @pytest.mark.parametrize("text, expected, description", [
        ("  mixed  \n \t spaces\t ok ", 3, "혼합된 공백과 특수 문자"),
    ])
    @pytest.mark.corner
    @pytest.mark.problem2
    def test_corner_cases(self, text, expected, description):
        """코너 테스트 케이스"""
        result = count_words(text)
        assert result == expected, f"Failed: {description}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])