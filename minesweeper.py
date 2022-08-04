
def start_game():
    #필드(2차원 리스트 10*10)
    fields = list() # 저장타입? 2차원 리스트
    for i in range(10):
        fields.append([0]*10)
    fields

    # 10개의 지뢰를 임의의 위치에 저장
    import random
    nums = list(range(100))
    for i in random.sample(nums, 10):
        row = i // 10  #행 몫
        col = i % 10  #열 나머지
        fields[row][col] = 9  # 지뢰위치

    # 지뢰주변 8방위치 1증가
    if row < (len(fields)-1):
        fields[row+1][col] += 1 #남
    if row < (len(fields)-1) and col < (len(fields)-1):
        fields[row+1][col+1] += 1 #남동
    if col < (len(fields)-1):
        fields[row][col+1] += 1 #동
    if row > 0 and col < (len(fields)-1):
        fields[row-1][col+1] += 1 #북동
    if row > 0 :
        fields[row-1][col] += 1 #북
    if row > 0 and col > 0:
        fields[row-1][col-1] += 1 #북서
    if col > 0:
        fields[row][col-1] += 1 #서
    if row < (len(fields)-1) and col > 0:
        fields[row+1][col-1] += 1 #남서

    # 1. 오픈한 자리의 숫자를 보기위한 2차원리스트 만들기
    fields2 = []
    for i in range(10):
        fields2.append(["-"]*10)
    fields2
    findMineCounter = 0  # 찾은 지뢰갯수

    while findMineCounter != 10:

        # 2. 오픈할 좌표 입력받기
        row = int(input("행좌표 입력(0-9) : "))
        col = int(input("열좌표 입력(0-9) : "))

        # 3. fields의 오픈할 좌표값을 출력용 2차원배열에 복사
        fields2[row][col] = fields[row][col]

        # 4. 출력용 2차원배열 출력
        display(fields2)

        # 5. 만약 지뢰좌표이면 남은 지뢰수 표시
        if fields[row][col] >= 9:
            findMineCounter += 1
            print("** 지뢰를 찾았습니다 **")
            print(f"{10-findMineCounter}개 남았습니다.")
        # 6. 만약 모든지뢰 오픈하면 게임종료, 아니면 2번부터 다시
