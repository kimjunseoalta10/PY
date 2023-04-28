# list_a = [1,2,3]

# print("# 리스트 뒤에 요소 추가하기")
# list_a.append(4)          append는 뒤에 추가 그러나 1개씩만 가능
# list_a.append(5)
# print(list_a)
# print()
# print("# 리스트 중간에 요소 추가하기")
# list_a.insert(0, 10)        insert는 (배열 위치, 숫자)
# print(list_a)

# list_a = [1,2,3]
# list_a.extend([4,5,6])      extend는 뒤에 여러개 생성
# print(list_a)

# list_a = [0,1,2,3,4,5]
# print("# 리스트의 요소 하나 제거하기")

# del list_a[1]
# print("del list_a[1]:", list_a)          del,pop[배열 위치] 삭제
# list_a.pop(2)
# print("pop(2):",list_a)

# list_b = [0,1,2,3,4,5,6]
# del list_b[3:6]           del[시작위치 : 끝 위치-1] 시작위치부터 끝위치-1까지 삭제
# print(list_b)

# list_b = [0,1,2,3,4,5,6]
# del list_b[:3]           처음부터 2까지 삭재
# print(list_b)

# list_b = [0,1,2,3,4,5,6]
# del list_b[3:]            3부터 끝까지 삭제
# print(list_b)

# list_b = [1,2,1,2]
# list_b.remove(2)          remove(숫자) 그 숫자가 list에 가장 먼저 나오는 부분 삭제
# print(list_b)

# list_b = [0,1,2,3,4,5,6]
# list_b.clear()            list 안에 있는 모든 것을 삭제
# print(list_b)

# list_a=[273,32,103,57,52]
# print(273 in list_a)              숫자 in 리스트 true or false
# print(99 in list_a)
# print(100 in list_a)
# print(52 in list_a)

# list_a=[273,32,103,57,52]
# print(273 not in list_a)              숫자 not in 리스트 true or false
# print(99 not in list_a)
# print(100 not in list_a)
# print(52 not in list_a)

# array = [273,32,103,57,52]
# for element in array :             for 반복자 in 반복할 수 있는것:
#     print(element)