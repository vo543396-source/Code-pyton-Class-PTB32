'''
xâu chuỗi trong python co thể hiểu là chuỗi ky tự strings
1.tạo chuôi
2.nôt chuỗi
3.truy cập vị tri của chuỗi
4.căt chuỗi
5.định dạng của chuỗi
6.cac phương thưc của chuỗi
'''
#1.tạo chuỗi:đượ khai bao trong dâu nhay đơn(' ') hoặc dâu nhay kep(" ")
name ="Hung"
age = "99"
print("đây là kiểu dữ liệu của age", type(age))

#nôi chuỗi: sử dụng toan tử (+) - chỉ được nôi chuỗi bởi kiểu dữ liệu sring
address = " Hà Nội"
info = name + "sông ở" + address +"tuổi" + str(age)
print(info)

#truy cập vị tri của chuỗi : sủ dụng index để truyc cập vị tri
name = "vu lam"
index_name = name[5]
print("vị tri cua 5 la: ", index_name)
#căt chuỗi: sử dụng index để căt theo vị 
strings = "123456789"
print(strings[ :4])
print(strings[3:7])
print(strings[5: ])

#định dạng của chuỗi:gồm 3 định dạng
name = "Thanh Hung"
address = "Nghệ An"
age = 18
print("ten toi la ", name, "dia chi", address, " tuoi la", str(age))
print("ten toi la: {} dia chi{} tuoi la{}".format(name,address, str(age)))
print("ten toi la: {name} dia chi la: {address} tuoi la: {str(age)}")
#cac phuong thuc cua chuỗi
#phuong thuc upper(): chuyen doi chuoi thanh chu hoa
print(f"su dung upper(): {name.upper()}")
name = "lam"
print(f"su dung lower (): {name.lower}")

strings_list = strings.split()
print("strings sau khi bi tach boi split():{string_list}")


new_strings = "nguyen "
print(new_strings.find("n"))
print(new_strings.index("n"))


string2 = "lam xau"
new_strings =  string2.replace("xau","khong dep")
print(new_strings)










