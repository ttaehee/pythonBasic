#숫자맞추기 게임 - while 문

#컴  1~100 난수 생성

#시도한 횟수가 10회넘으면

#메시지: 당신은 바보입니까?
def start_game():
    import random
    com = random.randint(1,100)
    try_count = 0 # 시도횟수

    correct = False #답 맞춤여부

    #반복조건. 숫자가 다른경우
    user = 0
    while user != com:
        try_count += 1 # try_count = try_count + 1
        user = input("1~100사이 숫자 입력 ")
        user = int(user)
        print( f"{try_count}번째 시도")
        if com == user:
            correct = True #정답
            print("추카추카 정답입니다!!")
        elif com < user:
            print("낮춰주세요")
        else:
            print("높여주세요")
        if correct == False and try_count > 10:
            print("당신은 바보입니까?")
