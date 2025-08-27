# Pytest로 여러 케이스 테스트 해보기

## 폴더 구조

```Plain Text
PROJECT_DIR
├── pytest.ini
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── basic
│   │   ├── __init__.py
│   │   ├── problem1.py
│   │   └── problem2.py
│   ├── challenge
│   │   ├── __init__.py
│   │   ├── problem6.py
│   │   ├── problem7.py
│   │   └── problem8.py
│   └── intermediate
│       ├── __init__.py
│       ├── problem3.py
│       ├── problem4.py
│       └── problem5.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_problem1.py
    ├── test_problem2.py
    ├── test_problem3.py
    ├── test_problem4.py
    ├── test_problem5.py
    ├── test_problem6.py
    ├── test_problem7.py
    └── test_problem8.py
```

## Quick Start

```bash
# (최초 1회) 세팅
conda create -y -n ENV_NAME python=3.10.12
conda activate ENV_NAME
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# (매번) 실행
conda activate ENV_NAME
pytest -v -m "problem7"

```

## 세팅(Setup) — 최초 1회만

```bash
# 1) 가상환경 생성
conda create -y -n ENV_NAME python=3.10.12

# 2) 가상환경 활성화
conda activate ENV_NAME

# 3) pip 최신화
python -m pip install --upgrade pip setuptools wheel

# 4) 의존성 설치 (둘 중 택1)
# [권장] 전체 의존성
python -m pip install -r requirements.txt
# [간단] 빠르게 확인만: pytest만 설치
# python -m pip install pytest

```

## 실행

```bash
# 1) 환경 활성화
conda activate ENV_NAME

# 2) 테스트 실행
pytest -v -m "problem7"
pytest -v -m "problem8 and basic"
pytest -v -m "problem1 and edge"
pytest -v -m "problem4 and corner"
```

## pytest 설정 파일

pytest.ini 파일 내용

```ini
[pytest]
# pytest 기본 설정
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# 소스 코드 경로
pythonpath = src

# 기본 실행 옵션
addopts = -vv --tb=short

# 마커 정의
markers =
    basic: 기본 케이스
    edge: 엣지 케이스
    corner: 코너 케이스
    problem1: 문제 1
    problem2: 문제 2
    problem3: 문제 3
    problem4: 문제 4
    problem5: 문제 5
    problem6: 문제 6
    problem7: 문제 7
    problem8: 문제 8
```

## init 파일 예시

basic 폴더의 init 파일

```python
# 테스트 할 함수들을 import 한다.
from .problem1 import sum_even
from .problem2 import count_words
```
