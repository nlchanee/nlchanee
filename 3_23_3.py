from winreg import KEY_READ


letters = 'python'
print(letters[0],letters[2])

string = "PYTHON"
i=0
while i < 6 :
    i = i+1
    print(string[6-i],end='')
print (" ")

url = "http://sharebook.kr"
index = "kr"
result1 = url.rfind(index)
print(len(url))
print(result1)

file_name = "보고서.xlsx"
result2 = file_name.endswith('xlsx')
print(result2)

file_name2 = "2020보고서.xlsx"
result3 = file_name2.startswith("2020")
print(result3)

score = int(input("점수를 입력하세요 :"))
if 0 < score <= 20:
    print("E")
if 20 < score <= 40:
    print("D")
if 40 < score <= 60:
    print("C")
if 60 < score <= 80:
    print("B")
if 80 < score <= 100:
    print("A")

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
result4 = len(cook)
print(result4)

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "Samsung", "LG"]
list = input("종목을 입력하세요 :")
if list in warn_investment_list:
    print("투자경고 종목입니다.")
else :
    print("투자경고 종목이 아닙니다.")

Sell_list = [100, 200, 300]
Added_Sell_list = [Sell_list[i]+10 for i in range(3)]
print(Added_Sell_list)

list2 = ["SK하이닉스", "삼성전자", "LG전자"]
j = 0
while j<3 :
    print(len(list2[j]))
    j = j+1
