# 뒤집힌 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 알고리즘: 기초
# 작성자: 김수민
# 작성일: 2026. 08. 05. 08:42:14

def solution(my_string):
    answer = ''
    for i in my_string:
        print(i)
        answer = my_string[::-1]
    return answer

print(solution("jaron"))