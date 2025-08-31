'''
vòng lặp: có hai kiểu vòng lặp
1.vòng lặp for
 cú pháp :
    for (index: số làn lặp) in "tập hợp"
        các cú pháp và câu lệnh 
        - Index : sẽ lấy giá trị và thay đổi qua mỗi vòng lặp
        - Tập hợp : là tập hợp các phần tự muốn lặp qua
'''
#sự dụng hàm range() để vẽ hình tam giác
n = 10 
for index in range(1, n + 1) : #range(1, b -1)
    print("*" * index)
    #ví dụ vòng lặp qua list 
    nums = [1, 2, 3, 4, 5, 6, 7]
# Index số thứ tự - bắt đầu từ 0

    for num in nums :
        print(num)

#đếm số chẵn lẻ trong 1 danh sách 
numbers = [1, 2, 3, 4, 5,6, 7]
even_count = 0 # Biển lưu trữ số chẵn
odd_count = 0 # Biển lưu trữ số lẻ

for num in numbers :
    print(num)
    if num % 2 == 0 :
        even_count += 1
    else :
        odd_count += 1 
print("số chẵn là: " + str(even_count))
print("số lẻ là: ", odd_count)

