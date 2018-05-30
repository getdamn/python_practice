def ad_calc(str):
    res = 0
    num = 0
    op = 0
    for i in range(len(str)):
        if str[i] == '+':
            if op == '+':
                res += num
            elif op == '-':
                res -= num
            else:
                res = num
            op = "+"
            num = 0
        elif str[i] == '-':
            if op == '+':
                res += num
            elif op == '-':
                res -= num
            else:
                res = num
            op = '-'
            num = 0
        else:
            num = num*10 + int(str[i])
            if i == (len(str)-1):
                if op == '+':
                    res += num
                elif op == '-':
                    res -= num
    return res
while True:
    exp = input("식 입력(+ -만) : ")
    print(ad_calc(exp))