# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 김수민
# 작성일: 2026. 08. 05. 08:34:57

def solution(numbers):
    answer = 0
    for i in numbers:
        answer+= i
    answer = round(answer / len(numbers), 1)
    return answer