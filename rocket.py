import time
import os
def rocket(len):
    i = 0
    while (len-4>i):
        print(str(len-1)+":하늘하늘하늘하늘하늘하늘하늘하늘하늘하늘하늘하늘하늘하늘하늘하늘")
        for j in range(len-5-i):
            print(str(len-2-j)+":")
        print(str(i+3)+":   로   ")
        print(str(i+2)+": 켓켓켓 ")
        print(str(i+1)+":푸슝푸슝푸")
        for k in range(i):
            print(str(i-k)+":")
        print("0:땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅땅")
        time.sleep(1)
        os.system("CLS")
        i +=1
while True:
    user_input = int(input("높이 입력: "))
    rocket(user_input)