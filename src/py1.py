# This is a sample Python script.
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def ex1():
    input1 = int(input("성적을 입력하시오:"))
    if (input1 >= 60):
        print("합격입니다")


def ex2():
    input1 = int(input("정수를 입력하시오:"))
    if (input1 <= 0):
        print("에러")
        return
    if (input1 % 2 == 0):
        print("짝수입니디")
    else:
        print("홀수입니디")


def ex3():
    input1 = int(input("점수를 입력하시오:"))
    if (input1 >= 90):
        print("장학금 대상자 입니다")
    print("수고하셨습니다")


def ex4():
    input1 = int(input("나이를 입력하시오:"))
    if (input1 >= 15):
        print("영화를 볼 수 있습니다")
    else:
        print("영화를 볼 수 없습니다")


def ex5():
    print("=== 짝수홀수 판별 프로그램")
    input1 = int(input("정수를 입력하시오:"))

    if (input1 <= 0):
        print("판별할 수 없는 수를 입력하셨습니다")
        print("양의 정수만 짝수/홀수 판별 가능합니다")
        return
    print(f"정수 {input1}를 입력했군요")
    if (input1 % 2 == 0):
        print("당신이 입력한 수는 짝수입니다")
    else:
        print("당신이 입력한 수는 홀수입니다")


def ex6():
    print("=== 짝수홀수 판별 프로그램")
    input1 = int(input("정수를 입력하시오:"))

    if (input1 <= 0):
        print("판별할 수 없는 수를 입력하셨습니다")
        print("양의 정수만 짝수/홀수 판별 가능합니다")
        sys.exit()

    print(f"정수 {input1}를 입력했군요")
    if (input1 % 2 == 0):
        print("당신이 입력한 수는 짝수입니다")
    else:
        print("당신이 입력한 수는 홀수입니다")


def ex7():
    input1 = int(input("점수가 몇 점 이에요?:"))
    if (input1 >= 90):
        print("장학금 대상자 입니다")
        print("축하합니다")
    else:
        print("수고하셨습니다")
        print("다음 학기를 노려봅시다.")


def ex8():
    year = int(input("몇 년도에 태어났나요?"))
    age = 2023 - year + 1
    if (15 <= age < 20):
        print("당신은 청소년 입니다")


def ex9():
    from datetime import date
    today = date.today()
    year = int(input("몇 년도에 태어났나요?"))
    age = today.year - year + 1
    if (15 <= age < 20):
        print("당신은 청소년 입니다")


def ex10():
    input1 = input("아이디를 입력하시오")
    if (input1 == "ilovepython"):
        print("환영합니다")
    else:
        print("아이디를 찾을 수 없습니다")


def ex11():
    input1 = int(input("시험점수가 몇 점 이에요?:"))
    if (input1 >= 90):
        print("시험을 아주 잘 봤군요. 축하해요.")
    elif (input1 >= 80):
        print("시험을 괜찮게 봤군요. 수고했어요")
    elif (input1 >= 70):
        print("시험을 좀 못봤군요. 다음에는 잘 봐요.")
    else:
        print("완전히 망했군요")


def cheakyun(input):
    if (input % 400 == 0):
        return True
    if (input % 100 != 0 and input % 4 == 0):
        return True
    return False


def ex12():
    input1 = int(input("윤년채크"))
    result = cheakyun(input1)
    if (result):
        print("윤년입니다")
    else:
        print("윤년이아닙니다")


def ex13():
    input1 = int(input("정수 입력 ->"))
    if input1 > 0:
        print("양수입니다")
    if input1 == 0:
        print("0입니다")
    if input1 < 0:
        print("음수입니다")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    ex13()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

r1 = 10
r2 = 15
r3 = 20
pi = 3.14
rlist = [r1, r2, r3]


def 원넓이구하기(r):
    return r*r*pi


def 원둘레구하기(r):
    return r*2*pi


for i in range(3):
    print("반지름이 %3d인 원의 둘레는 %8.2f 입니다." % (rlist[i], 원둘레구하기(rlist[i])))
    print("반지름이 %3d인 원의 넓이는 %8.2f 입니다." % (rlist[i], 원넓이구하기(rlist[i])))

#6
def f(x):
    return 2*x + 5


for i in range(15, 26, 5):
    print(f"f({i})= {f(i)}")

#7
def algo(input):
    if input >= 90:
        return("A")
    elif input >= 80:
        return("B")
    elif input >= 70:
        return("C")
    else:
        return("D")
while True:
    inp = input("점수 입력 :")
    result = algo(int(inp))
    print(f"당신의 점수 {inp}")
    print(f"당신의 학점 {result}")

#8
def algo(input):
    if input % 2 == 0: 
        return("짝수")
    else:
        return("홀수")
while True:
    inp = input("양의 정수 입력")
    result = algo(int(inp))
    print(f"{result}입니다")
import time
n = 1
while n <= 5:
    print("파이썬 재밌네")
    time.sleep(1)
    n = n+1
print("파이썬 쉽네")

import time
n = 1
while n <= 10:
    print(n)
    n = n+1
    time.sleep(1)
print("숫자 세기 끝")

n = 100
while n <= 150:
    print(n)
    n += 5

print("종료합니다")