# print("IDLE에서 파이썬 코드를")
# print("작성해서 출력해 보는")
# print("예제입니다.")

# print("안녕하세요"[0])
# print("안녕하세요"[1])
# print("안녕하세요"[2])
# print("안녕하세요"[3])
# print("안녕하세요"[4]) 순서대로 출력

# print("안녕하세요"[-1])
# print("안녕하세요"[-2])
# print("안녕하세요"[-3])
# print("안녕하세요"[-4])
# print("안녕하세요"[-5]) 반대로 출력

# print("안녕하세요"[1:4]) a:b a부터 b-1까지

# print("안녕하세요"[1:]) 1부터 끝까지
# print("안녕하세요"[:3]) 0부터 3-1까지

# print(len("안녕하세요")) 문자열 길이

# print(type(20)) 괄호 안 종류 int
# print(type(3402.204)) flaot
# print(type("안녕하세요")) str

# print(0.52273e2) e2=10**2
# print(0.52273e-2) e-2=10**-2

# print("안녕"+"하세요"*3) 안녕하세요하세요하세요
# print(("안녕"+"하세요")*3) 안녕하세요안녕하세요안녕하세요
# print("안녕"+("하세요"*3)) 안녕하세요하세요하세요

# string = input("입력> ")
# print("자료:", string)
# print("자료형:",type(string)) 입력받는값이 숫자일 경우에서 자료형은 str이다

# string_a=input("입력A>") 325
# int_a=int(string_a)
# string_b=input("입력B>") 45
# int_b=int(string_b)
# print("문자열 자료:", string_a+string_b) 32545
# print("숫자 자료:", int_a+int_b) 370

# output_a="{:d}".format(52)
# output_b="{:5d}".format(52) 빈칸3칸 52
# output_c="{:10d}".format(52) 빈칸 8칸 52
# output_d="{:05d}".format(52) 00052
# output_e="{:05d}".format(-52) -0052
# print("# 기본")
# print(output_a)
# print("#특정 칸에 출력하기")
# print(output_b)
# print(output_c)
# print("#빈칸을 0으로 채우기")
# print(output_d)
# print(output_e)

# a="{:+5d}".format(52) 기호뒤로밀기
# b="{:+5d}".format(-52) 기호뒤로밀기
# c="{:=+5d}".format(52) 기호앞으로밀기
# d="{:=+5d}".format(-52) 기호앞으로밀기
# e="{:+05d}".format(52) 0으로 채우기
# f="{:+05d}".format(-52) 0으로 채우기
# print("#조합하기")
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)