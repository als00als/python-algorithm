# 편지
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120898
# 알고리즘: 기초
# 작성자: 김수민
# 작성일: 2026. 08. 05. 08:46:47

def solution(message):
    answer = 0
    list = []
    for i in message:
        # print(i)
        list.append(i)
        answer = len(list) * 2
    return answer
