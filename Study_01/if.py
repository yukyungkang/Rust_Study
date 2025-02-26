#if 기본 구조
if True: #if 조건: 조건이 참이면 들어가고 거짓이면 넘어 간다
    print('참입니다.') #실행할 명령
if False:
    print('참입니다.') #출력되지 않는다.

#정수에 따라 합격여부를 출력하는 코드
score = 90
if score > 80:
    print('합격입니다.')

# if와 함께 사용할 수 있는 else와 elif가 있다

# else 예시
score = 60
if score > 80: # 80 점 이상인가?
    print('합격입니다.')
else: #거짓이면 아래 내용을 출력해
    print('불합격입니다.')

# elif 예시
score = 75
if 80 < score <= 100: #sore가 80보다 크거나 100보다 작거나 같은
    print('학점은 A입니다.')
elif 60 < score <= 80: #elif는 else와 if에 줄임말 이다. 참이면 아래를 출력한다
    print('학점은 B입니다.')
elif 40 < score <= 60:  # 다른 프로그램에서는 흔하지 않지만 중복으로 사용이 가능하다
    print('학점은 C입니다.')
else: #거짓이면 아래 내용을 출력해
    print('학점은 F입니다.')

#자동 입장 만들기
# 조건1: 20세 이상 8000원, 10~19세 5000원, 10세 미만 2500원
# 조건2: for를 사용해 ages에 저장되어 있는 나이를 검사하세요
# 조건3: 나이에 따라 total_price에 입장료를 더하세요
total_price = 0
ages = [22, 21, 17, 32, 4, 28, 19, 8]
for age in ages:
    if age >= 20:
        total_price = total_price + 8000
    elif age >= 10:
        total_price = total_price + 5000
    else:
        total_price = total_price + 2500
print('총 입장료는', total_price, '원입니다.')
# 들여쓰기가 있는 경우 For와 if의 코드 블록을 구분하기 위함이다 헷깔리지 않게 기억하는 것이 좋다.

#여러 조건 판단하기
games = 12 #Games에 12가 저장이되어 있다
points = 25 #points에 25가 저장되어 있다
if games >=10 and points >=20: #games 점수가 10보다 크거나 같냐? 그리고 points가 20보다 크거나 같냐?
    print('MVP로 선정되었습니다.')
#and의 경우 두개 모두 참이되어야 참이 된다.
# 조건1 and 조건2
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#or의 경우 두개 조건중 하나라도 참이면 참이된다
#조건1 or 조건2
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#not의 경우 결과를 뒤집는다.
print(not True)
print(not False)

#도둑잡기
# 조건1: for를 사용해 suspects를 검사하세요
# and로 인상착의가 동시에 일치하는 범인을 찾으세요
suspects = [['거위', '새', '암컷'], ['푸들','개','수컷'],['비글','개','암컷']]
for suspect in suspects:
    if suspect[1] == '개' and suspect[2] == '암컷':
        print('범인은',suspect[0], '입니다.')



