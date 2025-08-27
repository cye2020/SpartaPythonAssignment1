"""
Problem 7: moving_average 함수 테스트
이동 평균 구하기(슬라이딩 윈도우)
"""

import pytest
from src.challenge.problem7 import moving_average


class TestMovingAverage:
    """moving_average 함수 테스트"""
    
    # 테스트 케이스 1: 기본 케이스 입력
    @pytest.mark.parametrize("data, k, expected, description", [
        (
            [10, 20, 30, 40, 50],
            3, 
            [20.0, 30.0, 40.0],
            "합을 만들 수 있는 경우"
        ),
    ])
    @pytest.mark.basic
    @pytest.mark.problem7
    def test_basic_cases(self, data, k, expected, description):
        """기본 테스트 케이스"""
        result = moving_average(data, k)
        assert result == expected, f"Failed: {description}"

    # 테스트 케이스 2: 엣지 케이스 입력
    @pytest.mark.parametrize("data, k, expected, description", [
        (
            [1, 2, 3],
            0,
            [],
            "k가 0인 경우"
        ),
        (
            [1, 2, 3],
            -2,
            [],
            "k가 음수인 경우"
        ),
        (
            [1, 2, 3],
            5,
            [],
            "k가 리스트 길이보다 큰 경우"
        ),
        (
            [5, 7, 9],
            1,
            [5.0, 7.0, 9.0],
            "k가 1인 경우"
        ),
        (
            [1, 2, 3, 4],
            4,
            [2.5],
            "k가 리스트 길이와 같은 경우"
        ),
    ])
    @pytest.mark.edge
    @pytest.mark.problem7
    def test_edge_cases(self, data, k, expected, description):
        """엣지 테스트 케이스"""
        result = moving_average(data, k)
        assert result == expected, f"Failed: {description}"
    
    # 테스트 케이스 3: 코너 케이스 입력
    @pytest.mark.parametrize("data, k, expected, description", [
        (
            [-1, -2, -3, -4],
            2,
            [-1.5, -2.5, -3.5],
            "음수 값이 포함된 경우"
        ),
        (
            [1, 2, 2],
            2,
            [1.5, 2.0],
            "중복 값이 포함된 경우"
        ),
        (
            [0, 0, 10, 20],
            2,
            [0.0, 5.0, 15.0],
            "0이 포함된 경우"
        )
    ])
    @pytest.mark.corner
    @pytest.mark.problem7
    def test_corner_cases(self, data, k, expected, description):
        """코너 테스트 케이스"""
        result = moving_average(data, k)
        assert result == expected, f"Failed: {description}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])