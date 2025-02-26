#튜플, 딕셔너리
# 튜플은 리스트와 같으나 값을 변경 할 수 없다.(숫자, 문자, 리스트를 또 저장하는 것이 가능)
# 튜풀은 소괄호를 사용한다.
my_tuple = () #튜플에 값을 지정하지 않은 상태
print(my_tuple)

my_tuple2 = (1, -2, 3.14) #숫자로만 입력
print(my_tuple2)

my_tuple3 = '앨리스', 10, 1.0, 1.2 #소괄호 없이 문자와 숫자 작성
print(my_tuple3)

#값이 한개인 튜플을 입력 할 경우 반드시 콤마가 같이 되어야 한다.
my_int = (1) #그냥 정수 1이 된다
print(type(my_int))
my_tuple = (1,) #튜플이란걸 표현하고 싶으면 콤마가 들어가야한다.
print(type(my_tuple))

#튜플도 index를 이용하여 값을 가져올 수 있다
clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1]) #튜플에서 하트 2를 가져오는 코드
#튜플은 한번 지정한 값은 바꿀 수 없다.

#패킹과 언패킹
clovers = '클로버1', '하트2', '클로버3' #여러개의 값을 하나로 패킹한다.
print(clovers)
alice_blue = (240, 248, 255)
r,g,b = alice_blue
print('R:', r, 'G:', g, 'B:', b) #각각의 변수에 숫자가 들어가는 언패킹

#dodo에는 박하맛 alice에는 딸기맛을 저장
#패킹과 언패킹을 사용해 둘의 사탕을 교환하자
dodo = '박하맛'
alice = '딸기맛'
print('도도새:', dodo, '앨리스:', alice)
dodo, alice = alice, dodo
print('도도새:', dodo, '앨리스:', alice)
