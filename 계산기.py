def ad_calc(exp):
    res = 0
    num = ""
    for idx in range(len(exp)):
        if (exp[idx] == '+') or (exp[idx] == '-'):
            res += int(num)
            num = exp[idx]
        else:
            num += exp[idx]
            if idx == len(exp) -1:
                res += int(num)
    return res
while True:
    user_input = input("식을 입력하세요: ")
    print(ad_calc(user_input))