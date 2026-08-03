# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 김수민
# 작성일: 2026. 08. 04. 08:56:54

def solution(n, k):
    answer = 0
    answer = n * 12000 + k * 2000
    if n >= 10:
        k2 = int(n / 10) # n = 64 => n / 10 = 6 ... 4 => k2 = 6
        answer = answer - 2000 * k2        
    return answer