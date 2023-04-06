import random
# print("random.random()")
# print(random.randrange(1,7))
# print(random.randint(1,6))
# print(random.choice([10,20,30]))

# a=random.randrange(0,24)
# if(0<=a<12) :
#     print("좋은 아침입니다. 지금 시각은", a, "시 입니다.")
# else :
#     print("좋은 오후입니다. 지금 시각은", a, "시 입니다.")
# b=random.choice(["true", "false"])
# if b=="true" :
#     print("현재 날씨가 화창합니다.")
#     if 6<=a<=8 :
#         print("종달새가 노래를 한다.")
#     else :
#         print("종달새가 노래를 하지 않는다.")
# if b=="false" :
#     print("현재 날씨가 화창하지 않습니다.")
#     print("종달새가 노래를 하지 않는다.")

# x=0
# while x<3:
#     print("안녕하세요.")
#     x+=1

# student = 1
# while student<=3 :
#     print(student, "번 학생의 성적을 처리한다.")
#     student+=1

# n=int(input('원하는 단은? '))
# i=1
# while i<=9 :
#     print(n,"*",i,"=",n*i)
#     i+=1

# num=1
# sum=0
# while num<=10 :
#     sum += num
#     print("num의 값 : %d => 합게 : %d" %(num, sum))
#     num+=1

# num=150
# sum=0
# while num<=300 :
#     if(num%2==1) :
#         sum+=num
#     num+=1
# print(sum)

# num=-5
# print("섭씨 화씨")
# while num<=5 :
#     print( num, num*9.0/5.0+32.0)
#     num+=1

# n=int(input())
# num =1
# sum = 1
# while num<=n :
#     sum*=num
#     num+=1
# print(n,"! = ", sum,sep="")

# n=1
# while n<=20 :
#     if(n%2==0) :
#         print(n, end=' ')
#     n+=1

# num=10
# while num<=50 :
#     if(num%3!=0) :
#         print(num, end=' ')
#     num+=1

# a=""
# while a!="python" :
#     a=input("암호 입력 :")
# print("로그인 성공")

# num=random.randint(1,100)
# a=""
# t=0
# while a!=num :
#     a=int(input("숫자를 맞춰 보세요 : "))
#     if a>num :
#         print("높음")
#     if a<num :
#         print("낮음")
#     t+=1
# print("축하합니다. 시도횟수 =", t)

# for i in [1,2,3] :
#     print("안녕하세요")

# for i in range(10) :
#     print(i, end =" ")

# for i in range(1,11) :
#     print(i, end=" ")

# for i in range(1, 10, 2) :
#     print(i, end =" ")

# for i in range(20, 0, -2) :
#     print(i, end=" ")

# a=10
# for num in range(1,5,2) :
#     a+=num
# print(a)

for i in range(1,4) :
    print(i,"번째 학생의 성적 처리")