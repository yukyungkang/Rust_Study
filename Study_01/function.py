# ✅ 파이썬 함수의 3가지 종류
# 1️⃣ 내장 함수 (Built-in Function)
#    - 파이썬이 기본적으로 제공하는 함수로, 별도의 설정 없이 바로 사용 가능
#    - 예: print(), len(), sum(), max(), min(), range() 등
#
# 2️⃣ 모듈 함수 (Module Function)
#    - 특정 기능을 묶어서 제공하는 모듈 내의 함수
#    - 사용하려면 import 키워드를 사용하여 모듈을 불러와야 함
#    - 예: math.sqrt(), random.randint(), datetime.datetime.now() 등
#
# 3️⃣ 사용자 정의 함수 (User-defined Function)
#    - 사용자가 직접 정의하여 사용하는 함수
#    - def 키워드를 사용하여 생성하고, 필요할 때 호출하여 사용
#    - 예: def my_function(): ...

# ✅ 1. 함수 정의 및 호출 (문자열 출력)
def my_func():
    print("토끼야 안녕!")  # 함수 실행 시 출력될 문장

# 함수 호출
my_func()
# 출력: 토끼야 안녕!


# ✅ 2. 두 개의 숫자를 더하는 함수
def add(num1, num2):
    return num1 + num2  # 두 숫자의 합을 반환

print(add(2, 3))
# 출력: 5


# ✅ 3. 두 개의 숫자를 더하고 곱하는 함수
def add_mul(num1, num2):
    return num1 + num2, num1 * num2  # 더한 값과 곱한 값을 반환

print(add_mul(2, 3))
# 출력: (5, 6) (튜플 형태로 반환됨)

# ✅ 효율적인 판결 함수 만들기
# 하트 여왕을 도와 카드 병사들에게 유죄 판결을 내리는 함수
# 반복되는 코드를 줄이고 효율적으로 사용할 수 있음

def judge_cards(name):
    """입력받은 카드 종류(name)에 대해 1~3 유죄 판결을 출력하는 함수"""

    # 1️⃣ 반복문을 사용하여 중복 제거
    # 기존 방식: print("하트 1 유죄!") 같은 코드를 여러 번 작성해야 했음
    # -> 반복문을 활용하면 자동으로 1~3까지 출력 가능
    for i in range(1, 4):
        print(name, f"{i} 유죄!")  # 카드 이름과 함께 유죄 판결 출력


# 2️⃣ 함수 호출을 통해 간결한 코드 유지
# 기존에는 카드마다 print()를 여러 번 작성해야 했음
# -> 함수 한 번 정의 후 여러 번 호출하여 코드 재사용성 증가

judge_cards("하트")  # "하트" 카드 병사에게 유죄 판결
judge_cards("클로버")  # "클로버" 카드 병사에게 유죄 판결
judge_cards("스페이드")  # "스페이드" 카드 병사에게 유죄 판결

# 3️⃣ 확장성과 유지보수 용이
# 새로운 카드가 추가되더라도 judge_cards("새로운 카드")만 호출하면 되므로 유지보수가 쉬움
# 예: judge_cards("다이아")를 추가하면 "다이아 1~3 유죄!"가 자동으로 출력됨

# ✅ 파이썬에서 모듈(Module)이란?
# - 비슷한 함수들을 모아둔 파일을 의미함.
# - 함수처럼 파이썬에서 기본 제공하는 모듈도 있고, 사용자가 직접 만들 수도 있음.
# - 또한, 다른 개발자들이 만들어 놓은 모듈도 활용할 수 있음.

# ✅ 모듈의 장점
# - 다양한 사람들이 만든 모듈을 가져와서 사용하면 빠르게 개발할 수 있음.
# - 파이썬이 널리 사용되는 이유 중 하나는 다양한 외부 모듈이 존재하기 때문.

# ✅ 모듈을 사용하려면?
# - import 키워드를 사용하여 모듈을 불러와야 함.
# - 불러온 후, 모듈 안에 있는 함수를 사용할 수 있음.
# - 사용법: import 모듈이름 → 모듈이름.함수명()
# ✅ 랜덤(Random) 모듈이란?
# - 무작위(랜덤) 값을 생성하는 기능을 제공하는 모듈.
# - 동전 던지기, 추첨, 랜덤 숫자 생성 등에 사용됨.
# - 사용하려면 먼저 import 해야 함: import random

# ✅ random.choice() 함수
# - 리스트, 튜플과 같은 순서가 있는 데이터에서 랜덤하게 하나의 값을 선택함.
# - 사용 예: random.choice(리스트)

import random  # 랜덤 모듈 불러오기

animals = ['체셔고양이', '오리', '도도새']  # 랜덤 선택할 리스트

# 리스트에서 하나의 값을 랜덤하게 선택
print(random.choice(animals))


# ✅ random.sample() 함수
# - 리스트에서 지정한 개수만큼 **중복 없이** 랜덤하게 선택함.
# - 사용 예: random.sample(리스트, 개수)

# 리스트에서 두 개의 값을 랜덤하게 선택 (중복 없음)
print(random.sample(animals, 2))


# ✅ random.randint() 함수
# - 지정한 범위 내에서 랜덤한 정수를 반환함.
# - 사용 예: random.randint(시작값, 끝값) (시작값과 끝값도 포함됨)

# 5부터 10 사이의 정수 중 하나를 랜덤하게 선택
print(random.randint(5, 10))
# ✅ 랜덤 모듈을 사용하여 제비뽑기 판결 내리기
# - random.choice()를 사용해 cards 리스트에서 임의로 카드 병사 한 명을 뽑아서 유죄 판결을 내린다.

import random  # 랜덤 모듈 불러오기

# 1️⃣ 카드 리스트 정의
# 카드 리스트는 '하트', '클로버', '스페이드' 3가지 카드 종류가 들어 있음
cards = ['하트', '클로버', '스페이드']

# 2️⃣ 랜덤으로 카드 한 장 선택
# random.choice()를 사용해 cards에서 임의로 한 개의 값을 선택
chosen_card = random.choice(cards)

# 3️⃣ 선택된 카드에 대해 유죄 판결을 내리기
print(chosen_card, '유죄!')  # 선택된 카드와 함께 유죄 판결 출력

# ✅ 왜 모듈을 사용할까?
# - "있는 바퀴를 다시 만들지 마라"는 말처럼, 이미 검증된 기능을 다시 개발할 필요 없음.
# - 자동차를 만들 때 바퀴부터 새로 만들지 않고, 이미 만들어진 부품을 조립하듯이
#   파이썬에서는 모듈을 활용하여 빠르고 효율적으로 개발 가능.

# ✅ 모듈을 사용하면 좋은 점
# 1️⃣ **시간 절약**: 처음부터 함수를 만들 필요 없이 가져다 쓰면 됨.
# 2️⃣ **노력 절감**: 이미 검증된 코드를 사용하므로 개발이 편리함.
# 3️⃣ **품질 보장**: 많은 사람들이 사용하며 검증된 코드이므로 신뢰성이 높음.



# 1️⃣ 기존 방식: 직접 랜덤 숫자를 생성하는 함수를 만든다면?
# - 직접 만든다면 복잡한 알고리즘이 필요하고, 오류 발생 가능성이 높음.

# 2️⃣ 모듈 사용 방식: random.randint() 함수 활용
# - 이미 검증된 random 모듈을 사용하면 간단하게 랜덤 숫자를 생성 가능.
