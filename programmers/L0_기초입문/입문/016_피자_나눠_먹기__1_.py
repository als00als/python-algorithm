# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 김수민
# 작성일: 2026. 08. 05. 09:17:33

def solution(n):
    answer = 0
    if n < 7: # n = 1
        answer = n / n # answer = 1
    else: # 7 or 15
        if n % 7 != 0 : # 15 
            answer += (n // 7) + 1 # answer = 1
        else: # 7
            answer = n // 7 # answer = 1
    return answer