def greedy_cal(string: str) -> int:
    '''
    입력받은 string을 greedy 방법으로 가장 큰 뺄셈이 되도록 한다.

    '''

    # 1. - 기준으로 쪼개서 string 형태로 list에 저장
    tmp_list = string.split("-")
    equated_list = [sum(map(int, x.split("+"))) for x in tmp_list]

    num = equated_list[0]
    for i in range(1, len(equated_list)):
        num -= equated_list[i]
    print(num)


if __name__== "__main__":
    greedy_cal(input())
