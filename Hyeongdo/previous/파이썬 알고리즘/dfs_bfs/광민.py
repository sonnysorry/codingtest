# 변수 = 변수형(input('아래 창에 표시할 내용'))
# 문자 입력 시 변수형 str, 정수 입력시 변수형 int, 실수 입력시 변수형 float
a = str(input('enter name : '))
b = int(input("enter birth year : "))
# 아래에 입력을 하면 각각 a, b 변수에 값이 입력됨.
# c 변수 만들고 2021 에서 b 변수에 저장된 연도 값을 뺴준다.
c = 2021 - b
# 그리고 출력
# 문자 출력일 때는 , 쓰거나 + 쓰면됨.
print("Welcome, " + a + "!")
# + 쓰면 문자열 + 정수 덧셈으로 구분해서 오류 발생할 수 있기 떄문에
# 문자열로 변환해주는 구문인 str(c) 해주는 게 좋음
# 아니면 , 써서 사용해도 됨.
# print("You are", c,  "years old in 2021" )
print("You are" + str(c) +  "years old in 2021" )