#횟수 반복하기
print('안녕 거북이 0')
print('안녕 거북이 1')
# 하나씩 할 수 없으니 for 문을 이용한다
# 리스트, 문자, 숫자 등의 범위를 반복할 수 있다
# for 문을이용하여 반복적인 것을 쉽게할 수 있다
for num in range(10):
    print('안녕 거북이', num)
#파이선에서 반복을 하기위해서는 두가지 방법이 있다. 횟수를 반복 for와 조건 반복 while
for num in range(10): # for 변수 in 리스트
    print('안녕 거북이', num) #실행할 명령(print) <-코드 블록
# 리스트에 있는 값을 하나씩 가져와서 실행 하는 방식 리스트에 있는 값을 다 가져 가져때까지 반복
for num in [0,1,2]:
    print(num)

characters = ['앨리스', '도도새', '3월토끼']
for character in characters:
    print(character)

players = ['공작부인', '흰 토끼', '하트잭', '모자장수']
for player in players:
    print(player, '퇴장!')

#문자열 반복하기
# 문자를 가져와서 변수에 저장하여 실행한다.
for a in 'Hello': #for 변수 in 문자열
    print(a) #실행할 명령
    # 한 글짜식 내려오면서 Hello가 노출

#들여쓰기
# 들여쓰기는 앞에 4칸정도 띄어쓴다
# 들여쓰기는 코드 블록을 구분한다
nums = [0, 1, 2]
for num in nums:
    print(num) #num 0>1>2 순서로 출력한다. 그리고 아래 nums를 출력
print(nums)

nums = [0, 1, 2]
for num in nums:
    print(num)
    print(nums)
    #num과 nums가 하나의 코드 블록에 있어 num 1 다음 nums[0,1,2] 가 같이 출력된다.
    # 첫번쨰 프린트인 num을 통해 리스트를 갔다 다음 프린트인 nums로 이동 다시 첫번쨰 프린트로 반복해서 반복이 끝날떄싸지 한다.

#순서열 만들기
for num in range(3):
    print(num)

for y in range(1, 10):
    print(2, 'x', y, '=', 2 * y)

total = 0  # 합을 저장할 변수
for num in range(1, 11):  # 1부터 10까지 반복
    total += num  # total에 num 값을 더함
print(f"1부터 10까지의 합은 {total}입니다.")

# 계산 과정까지 출력 (
total = 0  # 합을 저장할 변수
for num in range(1, 11):  # 1부터 10까지 반복
    total += num  # total에 num 값을 더함
    print(total, "+", num, "=", total)  # 계산 과정을 출력
print(f"1부터 10까지의 합은 {total}입니다.")
# 현재 코드에서 중간 계산 과정이 생략되는 이유는 변수 total이 이미 더해진 상태에서 출력되기 때문

# 중간 과정까지 출력
total = 0  # 합을 저장할 변수
for num in range(1, 11):  # 1부터 10까지 반복
    print(total, "+", num, "=", total + num)  # 더하기 연산 수행 전의 값을 출력
    total += num  # total에 num 값을 더함
print(f"1부터 10까지의 합은 {total}입니다.")

total = 1  # 곱셈의 초기값은 1

for num in range(1, 11):  # 1부터 10까지 반복
    print(total, "x", num, "=", total * num)  # 곱하기 연산 수행 전 값을 출력
    total *= num  # total에 num 값을 곱함

print(f"1부터 10까지의 곱한 값은 {total}입니다.")

#for롸 리스트 인덱스를 사용해 roses의 '하얀장미'를 모두 '빨간장미'로 바꾸기
roses = ['하얀장미','하얀장미','하얀장미']
for i in range(3):
    roses[i] = '빨간장미'
print(roses)









