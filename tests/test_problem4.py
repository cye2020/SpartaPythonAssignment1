"""
Problem 4: grade_pass_fail 함수 테스트
합격/불합격 집계하기
"""

import pytest
from src.intermediate.problem4 import Problem4Solutions

class TestGradePassFailBasic:
    """기본 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem4Solutions.SOLUTIONS)
    @pytest.mark.parametrize("scores, threshold, expected, description", [
        (
            {"Alice": 85, "Bob": 52, "Chris": 60, "Dana": 59},
            None, 
            {"pass": 2, "fail": 2},
            "기본 케이스"
        ),
    ])
    @pytest.mark.basic
    @pytest.mark.problem4
    def test_basic_cases_all_solutions(self, solution_func, scores, threshold, expected, description):
        """모든 솔루션에 기본 케이스 적용"""
        if threshold is None:
            result = solution_func(scores)
        else:
            result = solution_func(scores, threshold)
        solution_name = Problem4Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


class TestGradePassFailEdge:
    """엣지 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem4Solutions.SOLUTIONS)
    @pytest.mark.parametrize("scores, threshold, expected, description", [
        (
            {"A": 60, "B": 61, "C": 59},
            None,
            {"pass": 2, "fail": 1},
            "threshold의 -1, 0, 1 차이"
        ),
        (
            {"A": 60, "B": 61, "C": 59},
            61,
            {"pass": 1, "fail": 2},
            "경계에서 하나 올린 경우"
        ),
        (
            {"A": 60, "B": 61, "C": 59},
            59,
            {"pass": 3, "fail": 0},
            "경계에서 하나 내린 경우"
        ),
        (
            {},
            None,
            {"pass": 0, "fail": 0},
            "빈 딕셔너리인 경우"
        )
    ])
    @pytest.mark.edge
    @pytest.mark.problem4
    def test_edge_cases_all_solutions(self, solution_func, scores, threshold, expected, description):
        """모든 솔루션에 엣지 케이스 적용"""
        if threshold is None:
            result = solution_func(scores)
        else:
            result = solution_func(scores, threshold)
        solution_name = Problem4Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


class TestGradePassFailCorner:
    """코너 케이스 테스트"""
    
    @pytest.mark.parametrize("solution_func", Problem4Solutions.SOLUTIONS)
    @pytest.mark.parametrize("scores, threshold, expected, description", [
        (
            {"Low": -5, "High": 105, "Zero": 0},
            None,
            {"pass": 1, "fail": 2},
            "비정상적인 점수도 규칙대로 분류하는 경우"
        ),
    ])
    @pytest.mark.corner
    @pytest.mark.problem4
    def test_edge_cases_all_solutions(self, solution_func, scores, threshold, expected, description):
        """모든 솔루션에 엣지 케이스 적용"""
        if threshold is None:
            result = solution_func(scores)
        else:
            result = solution_func(scores, threshold)
        solution_name = Problem4Solutions.get_solution_name(solution_func)
        assert result == expected, f"{solution_name} failed for {description}: expected {expected}, got {result}"


if __name__ == "__main__":
    pytest.main([__file__, '-v'])