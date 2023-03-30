'''
a=int(input("a입력:"))
b=int(input("b입력:"))
if a==3 and b==4 :
   print("OK")
if a==3 or b==4:
    print("Okay")'''
'''x=int(input("숫자입력:"))
if x>10 and x%2==0:
    print("10초과 짝수")'''
'''a=int(input("필기 성적을 입력하세요 :"))
b=int(input("실기 성적을 입력하세요 :"))
if(a>=80 and b>=80) :
    print("합격입니다!")
else :
    print("불합격!")'''
'''a=int(input("몇 살이세요?:"))
if(0<=a<7 or a>=65) :
    print("무료입니다.")
else :
    print("입장료는 3000원 입니다.")'''
'''age=int(input("나이:"))
height=int(input("키"))
if(age>=10 and height>=150) :
    print("놀이기구를 탈 수 있다")
else :
    print("놀이기구를 탈 수 없다")'''
'''a=input("아이디를 입력하세요: ")
b=int(input("회원 레벨을 입력하세요.: "))
if(a=="admin" or b==1) :
    print("관리자입니다")
else :
    print("관리자가 아닙니다")'''
'''a=int(input("정수를 입력하세요: "))
if(1<=a<=100) :
    print(a,"은(는) 1~100사이에 있다.")
else :
    print(a,"은(는) 1~100사이에 없다.")'''
'''month =3
if 3<=month<=5 :
    print("현재는 봄입니다.")
elif 6<=month<=8 :
    print("현재는 여름입니다.")
elif 9<=month<=11 :
    print("현재는 가을입니다.")
else :
    print("현재는 겨울입니다.")'''
'''a=int(input("구매금액: "))
if a<20000 :
    print("새벽배송이 불가능합니다.")
elif a>=50000 :
    print("무료배송입니다.")
else :
    print("배송비 2500원이 추가됩니다.")'''
'''a=int(input("점수를 입력하세요: "))
if a>=90 :
    print("A 등급입니다.")
elif a>=80 :
    print("B 등급입니다.")
elif a>=70 :
    print("C 등급입니다.")
else :
    print("F 등급입니다.")'''
'''a=int(input("첫 번째 수: "))
b=int(input("두 번째 수: "))
c=int(input("세 번째 수: "))
if a>b and a>c :
    print("가장 큰 수는 ", a, " 입니다")
elif b>a and b>c :
    print("가장 큰 수는 ", b, " 입니다")
else :
    print("가장 큰 수는", c, " 입니다")'''
'''a=int(input("온도를 입력하세요: "))
if a<0 :
    print("물의 상태는 고체입니다.")
elif 0<=a<100 :
    print("물의 상태는 액체입니다.")
else :
    print("물의 상태는 기체입니다.")'''
'''a=int(input("영어시험 점수를 입력하세요 : "))
b=int(input("수학시험 점수를 입력하세요 : "))
if a>=80 and b>=80 :
    print("최종 합격입니다.")
elif a>=80 or b>=80 :
    print("재시험 기회제공")
else :
    print("탈락입니다.")'''
'''a=int(input("서비스가 어떠셨나요(예: 1 또는 2 또는 3) : "))
b=int(input("음식값을 입력해 주세요(예:8000) : "))
if a==1 :
    print("팁 : ", int(b/5))
elif a==2 :
    print("팁 : ", int(b/10))
else :
    print("팁", int(b/20))'''
'''a=int(input("물건 구매가를 입력하세요 : "))
print("구매가 :", a)
if a>=300000 :
    print("할인율 : 10%")
    print("할인 금액 : ", int(a/10), "원")
    b=int(a/10)
    print("지불 금액 : ", a-b)
elif 10000<=a<50000 :
    print("할인율 : 5%")
    print("할인 금액 : ", int(a/20), "원")
    b=int(a/20)
    print("지불 금액 : ", a-b)
elif 50000<=a<300000 :
    print("할인율 : 7.5%")
    print("할인 금액 : ", int(a/1000*75), "원")
    b=int(a/1000*75)
    print("지불 금액 : ", a-b)
else :
    print("할인율 : 0%")
    print("할인 금액 : 0원")
    print("지불 금액 : ", a)'''
'''print("원하는 메뉴를 선택하세요.")
print("1. 떡볶이 3000원")
print("2. 김밥 2500원")
print("3. 튀김 3500원")
a=int(input("번호 선택 : "))
if a==1 :
    print("당신은 떡볶이를 선택하셨군요!")
    b=int(input("떡볶이를 몇 인분 주문하시겠습니까? "))
    print("총가격은",3000*b,"원 입니다.")
elif a==2 :
    print("당신은 김밥을 선택하셨군요!")
    b=int(input("김밥을 몇 인분 주문하시겠습니까? "))
    print("총가격은",2500*b,"원 입니다.")
elif a==3 :
    print("당신은 튀김을 선택하셨군요!")
    b=int(input("튀김을 몇 인분 주문하시겠습니까? "))
    print("총가격은",3500*b,"원 입니다.")
else :
    print("1,2,3 중 하나를 선택해주세요")'''
'''a=int(input("체중을 입력하세요: "))
b=float(input("키를 입력하세요(m): "))
c=a/(b*b)
if 0<=c<=15 :
    print("당신의 bmi지수는", format(c,'.8f'), "이며 정상입니다.")
elif 15<c<=25 :
    print("당신의 bmi지수는", format(c,'.8f'), "이며 과체중입니다.")
else :
    print("당신의 bmi지수는", format(c,'.8f'), "이며 비만입니다.")'''
'''a=int(input("체중을 입력하세요: "))
b=int(input("키를 입력하세요(cm): "))
c=int(input("나이를 입력하세요: "))
d=input("성별을 입력하세요: 남자/여자 ")
if d=="남자" :
    e=66.47+(13.75*a)+(5*b)-(6.76*c)
    print("당신의 기초대사량은", e, "입니다.")
if d=="여자" :
    e=655.1+(9.56*a)+(1.85*b)-(4.68*c)
    print("당신의 기초대사량은", e, "입니다.")'''
'''a=int(input("현재년을 입력해 주세요 : "))
b=int(input("현재월을 입력해 주세요 : "))
c=int(input("현재일을 입력해 주세요 : "))
d=int(input("출생년을 입력해 주세요 : "))
e=int(input("출생월을 입력해 주세요 : "))
f=int(input("출생일을 입력해 주세요 : "))
print("오늘 날짜 : ", a,"년",b,"월",c,"일")
print("생년 월일 : ", d,"년",e,"월",f,"일")
if e<b :
    g=a-d
elif e==b :
    if f<c :
        g=a-d
    else :
        g=a-d-1
else :
    g=a-d-1
print("만 나이 : ", g, "세")'''
import datetime
from pytz import timezone
now = datetime.datetime.now(timezone('Asia/Seoul'))
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)