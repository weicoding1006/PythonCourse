print("Hello"[0])
print(type("String"))
print(type(123))
print(type(True))
print(type(3.14))
print(type([1,2,3,4,5]))
print(type({"name":"Jeff","age":25}))

# print("字串" + str(len(input("輸入你的姓名"))))
print(2**3)
print(3 * (3 + 3) / 3 - 3)
print(round(3.1415926,2))
#Bmi
# try:
#     height = float(input("請輸入身高(m)"))
#     weight = float(input("請輸入體重(kg)"))
#     if height <= 0 or weight <= 0:
#         print("體重和身高都必須為正數")
#     else:
#         bmi = weight / (height * height)
#         print(f"bmi:{round(bmi,2)}")
# except ValueError:
#     print("請輸入有效數字")

#小費計算
totalBill = int(input("總共多少錢(台幣)"))
tip = float(totalBill * (int(input("要給幾%小費,10,12或15"))/100))
number_of_people = int(input("幾人平分？"))
total_price = (totalBill + tip) / number_of_people
print(f"一人要付:{round(total_price,2)}元")





