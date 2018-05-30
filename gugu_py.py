while(1):
    num = int(input("input number"))
    if (num >= 1)and(num<=9):
        for i in range(1,10):
            print(num,"*",i,"=",num*i)
    elif (10<=num<100):
        if num/10 == 0:
            s = 1
        else:
            s = int(num/10)
        if num%10 == 0:
            e = 1
        else:
            e = num%10
        if s < e:
            for i in range(s,e+1):
                for j in range(1,10):
                    print(i,"*",j,"=",i*j)
        else:
            for i in range(s,e-1,-1):
                for j in range(1,10):
                    print(i,"*",j,"=",i*j)
    else:
        break
