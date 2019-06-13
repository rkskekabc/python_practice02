# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.


def mysum(*num):
    returnnum = 0
    for i in num:
        returnnum += int(i)

    return returnnum

print(mysum(1, 2, 3))