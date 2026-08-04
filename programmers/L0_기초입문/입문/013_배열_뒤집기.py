# 배열 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120821
# 알고리즘: 기초
# 작성자: 김수민
# 작성일: 2026. 08. 05. 08:40:30

def solution(num_list):
    answer = []
    for i in num_list:
        print(i)
        answer = num_list[::-1]
    return answer