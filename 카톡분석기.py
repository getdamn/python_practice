class human:
    file_input = open("data.txt", 'r', encoding='utf-8')  # 에러나서 인코딩 방식을 바꾸었습니다.
    line = file_input.readlines()
    def __init__(self):
        user_input=("입력:")
        if user_input == 1:
            all_people
    def all_people(self):
        #텍스트를 한 줄씩 리스트로 받는다.
        name_dict = {} #결과로 출력할 dict를 초기화 한다.
        for i in range(len(line)): #한 줄 씩 받은 리스트가 끝날 때 까지 반복문을 돌린다.
            word = line[i].split('"') #XXXX-XX-XX "이름" blabla 이므로 "단위로 쪼갰다.
            if (len(word) > 1) and (len(word[0]) > 8): #out of range를 방지 하기 위해서
                if (word[0])[4] == "-": #xxxx-xx-xx라서
                    name = word[1]  #2번째 요소를 입력받으면 이름을 받을수 있을 것이다라고 생각 했습니다.
                    if name in  name_dict: #초기화한 dict 안에 이름이 있으면 카운트를 하구
                        name_dict[name] += 1
                    else: #없으면 추가.
                        name_dict[name] = 1
        ranking = []#랭킹에 name_dict 저장한 후 버블솔트 했슴다
        max_val = 0
        tmp_val = []
        for key in name_dict.keys():
            ranking.append([key,name_dict[key]])
        for i in range(len(name_dict)):
            max_val = 0
            for j in range(i,len(name_dict)):
                if ranking[j][1] > max_val:
                    max_val = ranking[j][1]
                    tmp_val = ranking[i]
                    ranking[i]= ranking[j]
                    ranking[j] = tmp_val
        for i in range(len(ranking)):
            if i == 0:
                print("☆★",i + 1, "등: ",ranking[i][0], ':', ranking[i][1],"★☆")
            else:
                print(i+1,"등: ",ranking[i][0],':',ranking[i][1])

        for key in name_dict.keys():
            print(key,':',name_dict[key])#반환 값으로 dict를 반환합니다.
    def input_most(self,text):
        name_dict = {}
        for i in range(len(line)):
            word = line[i].split('"')
            if len(word) > 2:
                words_intext = word[3].split(' ')
                for j in range(len(words_intext)):
                    if text == words_intext[j]:
                        name = line[i].split('"')[1]
                        if name in name_dict:
                            name_dict[name] += 1
                        else:
                            name_dict[name] = 1

        max = 0
        maxnum_man = ''
        for key in name_dict.keys():
            if name_dict[key] > max:
                max = name_dict[key]
                maxnum_man = key
        print(maxnum_man,':',max,"번")
human1 = human()
human1.all_people()
human1.input_most("안녕")