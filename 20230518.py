# for i in range(1,6) :
#     for j in range(1, i+1) :
#         print("*", end="")
#     print()

# for i in range(1, 8) :
#     for j in range(1, 8) :
#         if(i==j or j==8-i) :
#             print("*", end="")
#         else :
#             print(" ", end="")
#     print()

# t=0
# s=0
# a=int(input("수 입력 : "))
# print("\t", end="")
# for i in range(1, a+1) :
#     for j in range(1, i+1) :
#         if(i%j==0) :
#             t+=1
#     if(t==2) :
#         print(i, end="\t")
#         s+=1
#     if(s==5) :
#         print()
#         print("\t", end="")
#         s=0
#     t=0

# for i in range(1,6) :
#     for j in range(i,5) :
#         print(" ", end="")
#     for k in range(1, i+1) :
#         print("*", end="")
#     print()

# price = [500, 5000, 8900, 1800, 2500]
# fruit = ["사과", "파인애플", "수박"]
# print(price, end=' ')
# print(type(price))
# print(fruit, end=' ')
# print(type(fruit))

# fruitprice = ['사과', 1500, '수박', 8900]
# print(fruitprice)
# print(type(fruitprice[0]), end=' ')
# print(type(fruitprice[1]), end=' ')
# print(type(fruitprice[2]), end=' ')
# print(type(fruitprice[3]), end=' ')

# a=[]
# b=list()
# print(type(a), end=' ')
# print(type(b))

# num=list(range(1,21,2))
# print(num)
# print(type(num))
# a=list("Korea")
# print(a)
# print(type(a))

# print(len(num))
# print(len(a))

# score = [88,95,70,100,99]
# print(score[0], end = ' ')
# print(score[1], end = ' ')
# print(score[2], end = ' ')
# print(score[3], end = ' ')
# print()
# print(score[-1], end = ' ')
# print(score[-2], end = ' ')
# print(score[-3], end = ' ')
# print(score[-4], end = ' ')

# score = [88,95,70,100,99]
# score[0]=10
# score[1]=20
# score[2]=30
# score[-2]=40
# score[-1]=50
# print(score)

# animals = ['토끼', '거북이', '사자', '호랑이']
# i=0
# while i<4 :
#     print(animals[i])
#     i+=1

# nums=[0,1,2,3,4,5,6,7,8,9]
# print(nums[2:5:1])
# print(nums[1:7:2])
# print(nums[0:5:2])

# nums=[0,1,2,3,4,5,6,7,8,9]
# print(nums[:5:1])
# print(nums[:7:2])
# print(nums[:5:2])

# nums=[0,1,2,3,4,5,6,7,8,9]
# print(nums[2::1])
# print(nums[1::9])
# print(nums[7::1])

# nums=[0,1,2,3,4,5,6,7,8,9]
# print(nums[2:5])
# print(nums[1:7])
# print(nums[0:5])

# fruits = ['사과', '오렌지', '딸기', '포도', '감', '키위', '멜론', '수박']
# print(fruits[0])
# print(fruits[1:4])
# print(fruits[2:])
# print(fruits[-1])
# print(fruits[-4:-2])
# print(fruits[-3])

my_list=list("PythonIsFun!")
print(my_list)
print(my_list[5:11])
print(my_list[-5:-2])
print(my_list[:4])
print(my_list[8:])