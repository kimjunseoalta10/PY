# for i in range(1,21) :
#     if(i%2==0) :
#         print(i, end=" ")

# n=2
# for i in range(1,10) :
#     print(n,"*",i,"=",n*i)

# sum=0
# for i in range(1,11) :
#     sum+=i
#     print("i의 값 :", i, "=> 합계 : ",  sum)

# sum=0
# for i in range(1,101) :
#     if i%2==0 :
#         sum+=i
# print(sum)

# sum=1
# for i in range(1,11) :
#     sum*=i
# print(sum)

# t=0
# for i in range(1,101) :
#     if(i%5==0) :
#         print(i,end=" ")
#         t+=1
#     if(t==7) :
#         print("")
#         t=0

# a=int(input("정수를 입력하시오: "))
# i=1
# while i<=a :
#     if a%i==0 :
#         print(i,end=" ")
#     i+=1

# a=0
# b=1
# c=0
# print(a,b,end=" ")
# for i in range(3,21) :
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c

# t=0
# for i in range(1,41) :
#     print("-",end="")
#     t+=1
#     if(t==10) :
#         print("+",end="")
#         t=0

# t=0
# i=0
# while i<40 :
#     print("-",end="")
#     t+=1
#     i+=1
#     if(t==10) :
#         print("+",end="")
#         t=0

# t=0
# for i in range(1,41) :
#     print("-",end="")
#     t+=1
#     if(t%10==5) :
#         print("+",end="") 

# for i in range(10,101,10) :
#     print('%.d %.1f %.1f %.1f' %(i, i*0.393701, i*0.032808, i*0.010936))

# for i in range(1, 1001) :
#     print(i, end = ' ')
#     if i ==10 :
#         break

# score = [92,86,68,120,56,72]
# for s in score:
#     if(s<0 or s>100) :
#         break
#     print(s)
# print("성적 처리 끝")

# print("3+4?")
# while True :
#     a=int(input("정답을 입력하세요.: "))
#     if a==7 :
#         break
# print("참 잘했어요")

# while True :
#     a=input("신호등 색상 입력 : ")
#     if(a=="green") :
#         break
# print("길을 건너세요")

# sum=0
# i=1
# while True :
#     sum+=i
#     if(sum>50) :
#         break
#     i+=1
# print("합이 50보다 커지는 수는 ", i,"이고 합은 ", sum,"이다")

for dan in range(2,10):
    print(dan, "단")
    for hang in range(2,10):
        print(dan,"*", hang, "=", dan*hang)
    print()