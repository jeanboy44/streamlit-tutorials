# streamlit-tutorials
Streamlit의 기본 사용법을 예제와 함께 제공합니다. 이 레포지토리의 일부 예제는 아래의 강의에서 제공된 내용을 바탕으로 제작되었습니다.
https://www.udemy.com/course/learn-streamlit-python/?couponCode=OF83024D

## 설치 환경
python version: 3.12

## 설치 방법
1. uv 설치: https://github.com/astral-sh/uv 참고
1. python 3.12.3 설치
    ```
    uv python install 3.12.3
    ```
1. 가상 환경 생성
    ```
    uv venv --python 3.12.3
    ```
1. 가상 환경 실행
    ```
    source .venv/bin/activate
    ```
1. 필수 패키지 설치
    ```
    uv pip install -r requirements.txt
    ```

## 실행 방법 1. 로컬 환경
#### 예시 어플리케이션
```
(.venv) streamlit run simple_app.py
```

#### 메인 어플리케이션
```
(.venv) streamlit run app.py
```

## 실행 방법 2. Docker 활용
이 방법으로 실행할 경우, 위에 설명된 python 환경 설정은 필요하지 않으며, Docker가 설치되어 있어야 합니다.

1. 도커 이미지 빌드
    ```
    docker build -t streamlittutorials:latest -f Dockerfile .
    ```

1. 빌드된 이미지 확인
    ```
    docker images
    ```

1. 컨테이너 실행
    - 8502:8501 = \<host port number\>:\<container port number\>
    ```
    docker run -p 8502:8501 -d --restart always streamlittutorials:latest
    ```

1. 서비스 접속
    - https://localhost:8502/