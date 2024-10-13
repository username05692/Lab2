def obr(N):
    if N <0:
        print("Число має бути більше нуля")
        exit()
    result = 1
    if N % 2 == 0:
        for i in range(2, N + 1, 2):
            result *= i
    else:
        for i in range(3, N + 1, 3):
            result *= i
    return result
