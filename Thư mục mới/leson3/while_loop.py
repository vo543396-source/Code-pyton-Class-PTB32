'''
    - vòng lặp while: là một cấu trúc các ngôn ngữ lập trình, cho phép lặp lại một khối mã lệnh cho đến 
khi điều kiện trở thành false
    - vòng lặp vô hạn: là vong lặp không bao giờ kết thúc , gây ra hiện tượng treo ứng dụng. thường sảy ra
trong vòng lặp while
    - break : giúp thoát khỏi vòng lặp , tránh lặp vô hạn, dừng lại
điều kiện break bằng true
'''
# vòng lặp thường
count = 0
while count < 1000:
        print("giá trị của count là :", count)
        count += 1 #count = count + 1
        #vòng lặp vô hạn 
        count = 0
        while True:
                print("giá trị của count là: ", count)
#vòng lặp khi sử dụng break
count = 0
while True:
                print("giá trị của count là: ", count)
                count += 1 #count = count + 1

                if count == 1000:
                        print ("giới hạn")
                        break 
