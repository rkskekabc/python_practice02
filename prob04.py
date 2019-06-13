# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.

for i in range(1, 100):
    count = 0
    num = i
    while num != 0:
        num2 = num % 10
        if (num2 != 0) and (num2 % 3 == 0):
            count += 1
        num = int(num / 10)

    if count > 0:
        print(i, '짝'*count)