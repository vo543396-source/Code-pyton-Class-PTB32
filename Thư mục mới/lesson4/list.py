'''
    list (danh sách)
    -Tạo ra danh sách 
    -Truy cập phần tử trong danh sách 
    -Thêm phần tử vào danh sách
    -xóa phần tử khỏi danh sách 
    -độ dài danh sách
    -lặp qua danh sách
'''
#1. tạo ra danh sách
# danh sách (list): kí hiệu[] - có thể chữa các kiểu dữ liệu khác nhau
empty_list = [] # danh sách rỗng
my_list = [1, 2, 3, -1, 1.4, "Hung dz", True]
#index 0, 1, 2, 3, 4, 5, 6
'''
Index: dùng để đáng dấu các phần tử (item) theo số thứ tự từ 0
item: (phần tử - giá trị) là kiểu dữ liệu tồn tại trong 
'''
# truy cập phần tử trong danh sách
# chú ý : có thể truy cập các phần tử bằng (index)
num = my_list[2]
print("giá trị ở vị trí số 2 là:", num)
name = my_list[5]
print("giá trị ở vị trí số 5 là:", name)
# thêm phần tử vào danh sách "append()" - "insert()""
my_list.append("Nguyên xz") # thêm phần tử "Nguyên xz" vào cuối list
print("danh sách sau khi được thêm: " , my_list)
my_list.insert(2, "Nguyên") #thêm phần tử "Nguyên" vào vị trí số 2
print("danh sách sau khi được thêm bởi insert: " , my_list)
# xóa phần tử ra khỏi danh sách "rembve()" - "del" - "pop()" - "clear()"
my_list.remove("Hung dz") 
print("danh sách sau khi xóa khi dùng remove: " , my_list) 
del my_list[2] # xóa phần tử ở vị trí số 2 ra khỏi list
print("dánh sách sau khi bị xóa khi dùng del: " , my_list)
my_list.pop()
print("dánh sách sau khi bị xóa khi dùng pop: " , my_list)
my_list.clear()
print("dánh sách sau khi bị xóa khi dùng clear: " , my_list )
# độ dài danh sách 
length = len(my_list)
print("độ dài danh sách: " , length)
# lặp qua danh sách
for index in my_list:
    print(index)

    new_list = [5, 3, 1, 2, 4]