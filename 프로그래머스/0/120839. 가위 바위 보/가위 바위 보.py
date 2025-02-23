def solution(rsp):
    result = []
    a = []
    a=list(rsp)
    for i in range(len(a)):
        if int(rsp[i]) == 2:
            result.append("0")
        elif int(rsp[i]) == 0:
            result.append("5")
        else:
            result.append("2")
    s = "".join(result)
    return s
