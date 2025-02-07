def solution(n, k):
    per = 12000 * n
    drink = 2000 * k
    if n >= 10:
        drink = drink - (2000 * (n // 10))
    answer = per + drink
    return answer