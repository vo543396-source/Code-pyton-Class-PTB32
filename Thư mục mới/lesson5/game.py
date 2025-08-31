from random import randint
#tạo ra cơ chê chọn ngẫu nhiên cho may tinh
computer = randint(0, 2)
if computer == 0:
    computer = "keo"
elif computer == 1:
    computer = "bua"
elif computer == 2:
    computer = "bao"
print(computer)
#tao người chơi
player = input("nhập sự lựu chọn của bạn:  ")


if computer == player:
     print("hòa")
if player == "keo":
    if computer == "bua":
        print("thua")
    if computer == "bao":
        print("thang")

      
if player == "bua":
    if computer == "keo":
        print("thang")
    if computer == "bao":
        print("thua")

       
if player == "bao":
    if computer == "bua":
        print("thang")
    if computer == "keo":
        print("thua")
print(computer)

    