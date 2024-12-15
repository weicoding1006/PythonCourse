import random
# list = ["測試一","測試二"]
# list.append("測試三") #插入一筆資料
# print(list)

# list.extend(["插入資料一","插入資料二"]) #插入多筆資料
# print(list)

# friends = ["Jeff","Demy","Hani","Tim","Louis"]
# friends_index = random.randint(0,len(friends) - 1)
# print(f"{friends[friends_index]}付錢")

# # 巢狀清單（Nested List）
# fruits = ["草莓","橘子"]
# vegetables = ["高麗菜","青江菜"]
# data = [fruits,vegetables]
# print(data)
def check(my_chose,computer_chose):
    if(my_chose == computer_chose):
        print("平手")
    elif(my_chose == "剪刀" and computer_chose == "布"):
        print("玩家勝利")
    elif(my_chose == "石頭" and computer_chose == "剪刀"):
        print("玩家勝利")
    elif(my_chose == "布" and computer_chose == "石頭"):
        print("玩家勝利")
    else:
        print("電腦勝利")

data = ["剪刀","石頭","布"]
while True:
    try:
        my_chose_index = int(input("請輸入剪刀(0),石頭(1),布(2)"))
        if my_chose_index < 0 or my_chose_index > 2:
            print("僅能輸入0,1,2")
        else:
            print(f"您輸入的是:{data[my_chose_index]}")
            my_chose_string = data[my_chose_index]
            computer_chose_index = random.randint(0,len(data) - 1)
            print(f"電腦輸入的是{data[computer_chose_index]}")
            computer_chose_string = data[computer_chose_index]
            check(my_chose_string,computer_chose_string)
            break
    except ValueError:
        print("僅能輸入0,1,2")


    


