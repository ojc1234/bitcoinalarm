import webbrowser
import math
import sys
f1 = 1.1
f2 = 1.2345
f3 = 1.234567890123456789012345
print(sys.getsizeof(f1))
print(sys.getsizeof(f2))
print(sys.getsizeof(f3))
print(f3)
num = 2020
print("\065", num)
print("이진수:", bin(num))
chr1 = ['a', 'b', 'c']
for i in chr1:
    print(f"{i}|", bin(ord(i)))
print("")
c1 = 'a'
c2 = "b"
name = "Gil dong"
name2 = "Gil dong"
a = "Funny"
b = "Python"
c = a+b
print(c)

for c in text:
    print(c, "->", ord(c))
letter = "Hello Python"
encode = ""
해독문 = ""
for ch in letter:
    num = ord(ch)
    encode += chr(num+1)
print("원문", letter)
print("암호문", encode)
for ch in encode:
    num = ord(ch)
    해독문 += chr(num-1)
print("해독문", 해독문)
지름 = 30
print(f"{(지름/8)*(지름/8)*math.pi}")
array = "KIM"
for i in array:
    print("문자", i, "-->", ord(i), "-->", bin(ord(i)))

url = "http://www.naver.com"
webbrowser.open(url)
year = int(input("몇 년도에 태어났나요"))
age = 2019 - year + 1
print(f"그럼 올해{age}살이 겠군요")
import calendar
print("이번달 달력을 보여줄께요\n")
calendar.prmonth(2023, 3)
year = int(input("몇 년도에 태어났어요?"))
month = int(input("몇 월에 태어났어요?"))

print("\n당신이 태어난 달의 달력입니다.\n")
calendar.prmonth(year, month)

a = float(input("킬로미터 단위 거리 입력:"))
print("입력값:",a,"km")
print("변환값",a*0.621371,"miles")
tall = float(input("키가 몇 cm에요?"))
적정몸무게 = (tall-100)*0.9
과채중위험 = 적정몸무게 * 1.2
저채중위험 = 적정몸무게 * 0.8 
print("당신의 신장:",tall)
print("적정 몸무게:",적정몸무게)
print("과채중 위험 기준:",과채중위험)
print("저채중 위험 기준:",저채중위험)
print("=== 주차료 계산 프로그렘 ===")
a = int(input("주차시간 입력"))
주차요금 = ((a//15)-1)*1000
print("주차시간 시간:",a)
print("주차요금:",a)
import math
print("== 원의 둘레와 넓이 계산 ==")
r = int(input("원의 반지름 입력 :"))
print(f"원의 넓이는 {(r**2)*math.pi} 입니다.")
print(f"원의 둘레는 {(r*2)*math.pi} 입니다.")
#연습문제 7번
first = int(input("X를 입력하세요 > "))
sec = int(input("Y를 입력하세요 > "))
print(f"{first} 과 {sec} 를 곱한 값은 {first*sec} 입니다.")
#연습문제 8번
print("== 인치 --> 센치미터 변환 프로그램 ==")
i = float(input("인치 입력 : "))
print(f"{i} inch는 {i*2.54} cm 입니다.")
#연습문제 9번
print("== 센치미터 --> 인치 변환 프로그램 ==")
i = float(input("센티미터 입력 : "))
print(f"{i} cm는 {i/2.54} inch 입니다.")

#연습문제 10번
import calendar
calendar.prmonth(int(input("출생년도 : ")),int(input("출생 월 : ")))
#연습문제 11번
fir = int(input("숫자1 입력 :"))
sec = int(input("숫자2 입력 :"))
print(f"{fir} + {sec} = {fir+sec}")
print(f"{fir} * {sec} = {fir*sec}")
print(f"{fir} ^ {sec} = {pow(fir, sec)}")

import turtle

turtle.shape("triangle")
turtle.shapesize(10)
turtle.forward(200)
turtle.left(90)
turtle.right(90)
turtle.backward(300)
turtle.home()
turtle.clear()
turtle.exitonclick()

import turtle

t = turtle.Turtle()
t.shape("triangle")
t.shapesize(10)
turtle.fd(200)
turtle.right(90)
turtle.fd(200)
turtle.exitonclick()

import turtle

t1 = turtle.Turtle()
t1.shape("turtle")
t2 = turtle.Turtle()
t2.shape("turtle")

t1.color("red");t2.color("blue")
t1.fd(200);t1.rt(90)
t1.fd(200)

t2.left(90);t2.forward(200);t2.right(90);t2.fd(200)
turtle.exitonclick()

import turtle as t
t.shape("turtle")
t.shapesize(3)
num = int(input("몇각형을 그려줄까요?"))
t.color("blue")
t.width(3)
for i in range(num):
    t.forward(20)
    t.rt(360/num)
t.exitonclick()

import turtle as t
t.shape("turtle")
t.shapesize(3)
size = int(t.textinput("사각형","한 변의 길이"))
t.color("blue")
t.width(3)
for i in range(4):
    t.forward(size)
    t.rt(90)
t.exitonclick()
# 연습문제 4
import turtle as t
t.shape("turtle")
t.shapesize(3)
width = int(t.textinput("직사각형","가로 길이를 입력하세요"))
height = int(t.textinput("직사각형","세로 길이를 입력하세요"))
if width < 100 or width > 400:
    throw
if height < 100 or height > 400:
    throw
t.color("blue")
t.fillcolor("green")
t.begin_fill()
t.width(3)
for i in range(4):
    if i%2 == 0:
        t.forward(width)
    if i%2 == 1:
        t.forward(height)
    t.rt(90)
t.end_fill()
t.exitonclick()
#연습문제 5
import turtle as t
t.shape("turtle")
t.shapesize(3)
r = int(t.textinput("원넓이","반지름을 입력하세요"))
t.write(f"반지름이 {r}인 원의 넓이는{r**2*3.14}입니다")
t.fillcolor("green")
t.begin_fill()
t.left(90)
t.forward(40)
t.circle(200)
t.end_fill()
t.exitonclick()
#연습문제 7
import turtle as t
t.shape("turtle")
t.shapesize(3)
num = int(t.textinput("다각형","몇각형을 그려줄까요?"))
t.color("blue")
t.width(3)
for i in range(num):
    t.forward(20)
    t.rt(360/num)
t.exitonclick()
#무거운 연습문제
import turtle as t
t.shape("turtle")
t.speed(10)
t.shapesize(3)
t.color("blue")
t.width(5)
for i in range(3):
    t.circle(100)
    t.penup()
    t.forward(180)
    t.pendown()
t.penup()
t.home()
t.penup()
t.right(90)
t.forward(130)
t.left(90)
t.forward(80)
for i in range(2):
    t.pendown()
    t.circle(100)
    t.penup()
    t.forward(200)
    t.pendown()
t.exitonclick()
name = input("이름이 뭐예요? ")
print("=== 몸무게 제안 프로그램 ===")
tall = float(input("키 입력 -> "))
적정몸무게 = (tall-100)*0.9
print("키 %d cm에 대한 적정 몸무게는 %d kg 입니다."%(tall,적정몸무게))

a = int(input("첫 번째 정수 입력: "))
b = int(input("두 번째 정수 입력: "))
print("%d + %d = %d"%(a,b,a+b))
print("%d - %d = %d"%(a,b,a-b))
print("%d * %d = %d"%(a,b,a*b))
print("%d / %d = %5.1f"%(a,b,a/b))
a = 2019
b = 153
print("%5d + %4d = %5d"%(a,b,a+b))
print("%5o + %4o = %5o"%(a,b,a+b))
print("%5x + %4x = %5x"%(a,b,a+b))

a = 2019 / 13
b = 10 /3
print("%8.2f + %8.2f = %8.2f"%(a,b,a+b))
print("%8.2f - %8.2f = %8.2f"%(a,b,a-b))
print("%8.2f * %8.2f = %8.2f"%(a,b,a*b))
print("%8.2f / %8.2f = %8.2f"%(a,b,a/b))
#연습문제 7
inp = int(input("저축금액 입력: ")) #저축 금액 입력
이자 = input *0.0375 #이자 계산
세금 = 이자 * 0.15 #세금 계산
print("원금 {0:10,.0f}원".format(input)) #포멧 출력
print("이자 {0:10,.0f}원".format(이자))
print("세금 {0:10,.0f}원".format(세금))
print("최종 {0:10,.0f}원".format(input+이자-세금)) #최종금액 포멧출력


x = 10

inpt = int(input("한화 금액 입력 --> "))
dol = inpt // 1135
print("{0:0,d}".format(inp))
print("{0:0,.0f}".format(dol))
#8
inp = int(input("정수 입력 :")) #인풋
print("10진수:{0:16d}".format(inp)) #10진수 출력
print(" 2진수:{0:16b}".format(inp)) #2진수 출력
print(" 8진수:{0:16o}".format(inp)) #8진수 출력
print("16진수:{0:16x}".format(inp)) #16진수 출력
#9
first = int(input("정수 1 입력"))
sec =  int(input("정수 2 입력"))
print("{0:<5d} + {1:5d}= {2:>5d}".format(first,sec,first+sec)) #포멧출력
print("{0:<5d} - {1:5d}= {2:>5d}".format(first,sec,first-sec)) #포멧출력
print("{0:<5d} * {1:5d}= {2:>5d}".format(first,sec,first*sec)) #포멧출력
print("{0:<5d} / {1:5d}= {2:>5.2f}".format(first,sec,first/sec)) #포멧출력
#10
first = float(input("실수 1 입력"))
sec =  float(input("실수 2 입력"))
print("{0:<8.2f} + {1:8.2f}= {2:>8.2f}".format(first,sec,first+sec)) #실수 포멧 출력
print("{0:<8.2f} - {1:8.2f}= {2:>8.2f}".format(first,sec,first-sec)) #실수 포멧 출력
print("{0:<8.2f} * {1:8.2f}= {2:>8.2f}".format(first,sec,first*sec)) #실수 포멧 출력
print("{0:<8.2f} / {1:8.2f}= {2:>8.2f}".format(first,sec,first/sec)) #실수 포멧 출력

#ssfd
import turtle as t

t.shape('turtle')
t.shapesize(3)
for i in range(7):
    t.forward(100)
    t.right(360/7)
count = int(input("몇 까지 셀까요?"))
for i in range(1,count+1):
    print(f"count {i}")
print("end")

mincount = int(input("작은 양수 입력"))
maxcount = int(input("큰 양수 입력"))
for i in range(mincount,maxcount+1):
    print(f"count {i}")
print("end")



mincount = int(input("작은 양수 입력"))
maxcount = int(input("큰 양수 입력"))
i = mincount

while i <= maxcount:
    print(f"count {i}")
    i = i+1

print("end")

n=1
sum = 0
while n<=1000000:
    sum = sum + n
    n = n + 1
print("합계: ",sum)

sum = 0
for n in range(1,501):
    sum += n
print("합계: ",sum)



i = int(input("입력"))
sum = 0
for n in range(1,i+1):
    sum += n
print("합계: ",sum)

start = int(input("1입력"))
end = int(input("2입력"))
sum = 0
for n in range(start,end+1):
    sum += n
print("합계: ",sum)

import sys
start = int(input("1입력"))
end = int(input("2입력"))
sum = 0
if start > end:
    print("시작하는 수가 끝나는 수보다 크면 안됩니다.")
    sys.exit()
for n in range(start,end+1):
    sum += n
print("합계: ",sum)


## 포문연습

#7
start = 0
for i in range(30,71):
    start = start + i
print(start)

#9
import sys
inp  = int(input("구구단 몇단"))
if inp > 9:
    print("잘못된 값이 입력되었습니다")
    sys.exit()
for i in range (1,10):
    print(f"{inp} x {i} = {inp*i}")

#10 
first = int(input("정수 A입력"))
sec = int(input("정수 B입력"))

temp = 0

for i in range(first,sec+1):
    temp = temp + i

print(f"{first}부터 {sec}까지 더한 값 : {temp}")

#12
start = 0
for i in range(30,71):
    if (i % 3 == 0):
        start = start + i
print(start)

#15
import turtle as t

t.shape()
t.Pen()
for i in range(10,101,10):
    t.circle(i)


def next666(num):
    for i in range(num):
        num = num+ i
        if ("666" in str(num)):
            return num
inp = int(input())
temp = 666
for i in range(inp):
    temp = next666(temp)




ONETOTEN = range(1,101)
TWOBYTWO = []
for i in range(1,101):
    TWOBYTWO.append(object)(ONETOTEN)

for i in range(100):
    for i in range(100):
        print(TWOBYTWO)

size = int(input())
stack = []
for i in range(size):
    data = input()
    data = data.split(" ")
    num = int(data[1])
    if data[0] == "push":
        stack.append(num)
        pass
    if data[0] == "pop":
        stack.pop(num)
        print(num)
        pass
    if data[0] == "size":
        print(stack.count())

        pass
    if data[0] == "empty":
        if data.count() == 0:
            print(1)
        else:
            print(0)
        pass
    if data[0] == "top":
        print(data[-1])
        pass


####
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
import math as m
D = b**2 - 4*a*c
if D < 0:
    print("해없음")
if D == 0:
    x = (-b + m.sqrt(b**2-4*a*c))/2*a

    print(x)
if D > 0:
    x1 = (-b + m.sqrt(b**2-4*a*c))/2*a
    x2 = (-b - m.sqrt(b**2-4*a*c))/2*a

    print(x1,x2)
####
import math as m
for i in range(0,181,15):
    print(f"각도 {i},사인값:{round(m.sin(m.radians(i)),2)}")

size = int(input())
stack = []
for i in range(size):
    data1 = input()
    try:
        data = data1.split(" ")
        int(data[1])
    except:
        data = [data1,0]
    num = int(data[1])
    if data[0] == "push":
            stack.append(num)
    if data[0] == "pop":
        try:
            stack.pop(num)
            print(num)
        except:
            print(-1)

    if data[0] == "size":
        print(len(stack))
    if data[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if data[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
