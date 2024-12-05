# print("雲霄飛車!")
# height = int(input("請輸入您的身高(cm)"))
# if(height > 120):
#     print(f"身高為{height}公分，可以進入")
# else:
#     print(f"身高為{height}公分，身高太矮，禁止進入")


# number = int(input("請輸入數字"))
# if(number % 2 == 0):
#     print("是偶數")
# else:
#     print("是奇數")

print("雲霄飛車")
height = int(input("請輸入身高(cm)"))
price = 0
if(height >= 120):
    print("可以進入，請問幾歲?")
    age = int(input("請輸入年齡"))
    if(age > 18):
        price = 12
        print("支付12美元")
    elif(age > 12 and age < 18):
        price = 7
        print("支付7美元")
    else:
        price = 5
        print("支付5美元")
    
    want_photo = input(("需要照片嗎?是/否"))
    if(want_photo == "是"):
        price += 3
    print(f"總共{price}元")
else:
    print("小於120公分不得進入")

# weight = 85
# height = 1.85
# bmi = weight / (height ** 2)
# print(bmi)
# if(bmi < 18.5):
#     print("underweight")
# elif(bmi < 25 and bmi >= 18.5):
#     print("normal weight")
# else:
#     print("overweight")