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

# print("雲霄飛車")
# height = int(input("請輸入身高(cm)"))
# price = 0
# if(height >= 120):
#     print("可以進入，請問幾歲?")
#     age = int(input("請輸入年齡"))
#     if(age > 18):
#         if(age > 45 and age < 55):
#             price = 0
#             print("支付0美元")
#         else:
#             price = 12
#             print("支付12美元")
#     elif(age > 12 and age < 18):
#         price = 7
#         print("支付7美元")
#     else:
#         price = 5
#         print("支付5美元")
    
#     want_photo = input(("需要照片嗎?是/否"))
#     if(want_photo == "是"):
#         price += 3
#     print(f"總共{price}元")
# else:
#     print("小於120公分不得進入")

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

# print("歡迎來到披薩店")
# size = input("要多大的尺寸? S,M 或L")
# pepperoni = input("需要加辣香腸嗎? Y or N")
# extra_cheese = input("起司要增量嗎? Y or N")
# price = 0
# if(size == "S"):
#     price += 15
# elif(size == "M"):
#     price += 20
# elif(size == "L"):
#     price += 25
# else:
#     print("輸入錯誤")

# if(pepperoni == "Y"):
#     if(size == "S"):
#         price +=2
#     else:
#         price += 3
        
# if(extra_cheese == "Y"):
#     price +=1


# print(f"價格是{price}元")


print("遊戲開始")
direction = input("你看到一條岔路，你選? 左/右")
if(direction == "左"):
    action = input("你看到一條水路，你選擇? 等待/游泳")
    if(action == "等待"):
            color = input("選哪個顏色的門? 紅/黃/藍")
        if(color == "黃"):
            print("勝利")
        else:
            print("失敗")
    else:
        print("失敗")
else:
    print("失敗")