# a = "Hello Python Programming...!"
# print(a.upper()) 전부 대문자

# a="Hello Python Programming...!"
# print(a.lower()) 전부 소문자

# print("TraninA10".isalnum()) alnum 알파벳과 숫자 alpha 알파벳 identifier 식별자 decimal 정수 
# print("10".isdigit()) digit 숫자 space 공백 lower 소문자 upper 대문자

# a="안녕안녕하세요".find("안녕") 왼쪽에서 처음 안녕의 위치
# b="안녕안녕하세요".rfind("안녕") 오른쪽에서 처음 안녕의 위치
# print(a)
# print(b)

# import datetime 시간 모듈
# now=datetime.datetime.now() 변수안에 현재시간 대입
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

# number=input("정수입력>")
# last_character=number[-1] 마지막 숫자
# last_number=int(last_character)
# if last_number==0 \
#     or last_number ==2 \
#     or last_number ==4 \
#     or last_number ==6 \
#     or last_number ==8 :
#     print("짝수입니다")
# if last_number==1 \
#     or last_number ==3 \
#     or last_number ==5 \
#     or last_number ==7 \
#     or last_number ==9 :
#     print("홀수입니다.")

# number=input("정수 입력> ")
# last=number[-1]
# if last in "02468" :
#     print("짝수입니다")
# if last in "13579" :
#     print("홀수입니다")