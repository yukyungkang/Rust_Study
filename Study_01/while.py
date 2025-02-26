# while 조건 반복문
# 조건이 거짓이되면 끝난다.
num = 0
while num < 3: #num이 3보다 작으면 들어간다
    print('안녕 거북이', num)
    num = num + 1 #num +1을 해서 다시 저장했다

#조건 반복하기
#조건1: while의 코드블록을 5번만 반복하게 하세요
#조건2: 반복할 때마다 몇 번째 바퀴인지 출력하세요
#조건3: 전부 다 돌면 '경주 끝!'을 외치세요
count = 0
while count < 5:
    count = count + 1
    print(count, '번째 바퀴입니다.')
print('경주 끝!')

#input: 입력을 받는 함수
# 문자열로 가져온다
name = input('이름이 뭔가요?')
print(name,'안녕!')

#나라 이름 맞추기
# 1. 영국의 수도를 묻고 입력을 받아 answer에 저장해
# 2. 정답인 '런던'을 맞힐 때까지 반복해서 질문해
# 3. 정답을 맞히면 반복을 멈춰
answer = ""  # 초기 변수 설정
while answer != "런던":  # 사용자가 "런던"을 입력할 때까지 반복
    answer = input("영국의 수도는 어디인가요? ")  # 사용자 입력 받기
print("정답입니다! 🎉")  # 정답을 맞히면 반복 종료 후 출력

# continue
count = 0
while count < 3:
    count = count +1
    if count == 2:
        continue
    print(count)
# break
count = 0
while count < 3:
    count = count +1
    if count == 2:
        break
    print(count)

#무한 반복하기
# 실수로 할경우 control+c를 사용하면 멈춭다
#while True:
    #print('ctrl+c를 누르세요')

#수도 맞추기 2(힌트 버전)
# 1. 영국의 수도를 묻고 입력을 받아 answer에 저장해
# 2. 틀립 답을 말하면 어느 나라의 수도인지 말해줘
# 3. 보기에 없는 답을 말하면 보기에서 고르도록 안내헤
# 4. 정답인 '런던'을 맞힐 때까지 반복해서 질문해
# 5. 정답을 맞히면 break를 사용해 반복을 멈춰

while True:
    answer = input("런던, 파리, 서울 중 영국의 수도는 어디일까요? ")

    if answer == "런던":
        print("정답입니다. 런던은 영국의 수도입니다.")
        break
    elif answer == "파리":
        print("파리는 프랑스의 수도입니다.")
    elif answer == "서울":
        print("서울은 대한민국의 수도입니다.")
    else:
        print("보기에 있는 도시 중에서 골라주세요.")








