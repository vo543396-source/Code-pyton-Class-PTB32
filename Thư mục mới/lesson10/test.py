diem_so = []
n = int(input("nhap so luong bai kiem tra: "))
for index in range(n):
    diem = float(input(f"nhap so diem cho bai kiem tra thu {index + 1}: "))
    diem_so.append(diem)
def sap_xep_va_xoa_diem(diem_so):
    diem_so.sort()
    while diem_so[0] == diem_so [1]:
        diem_so.remove(diem_so[0])
        diem_so.remove(diem_so[0])

    return diem_so
def diem_lon_hon_8(diem_so):
    count = 0
    for diem in diem_so:
        if diem >= 8:
            count += 1 
    return count

sap_xep = sap_xep_va_xoa_diem(diem_so)
print("danh sach sau khi xu ly 1 va 2la: ")
for diem in diem_so:
    print(diem)


count = diem_lon_hon_8(diem_so)
print(f"so luong hon hon va bang 8 la: {count}  ")

while True:
    n = int(input("nhap vao gia tri: "))
    if n < 0: 
        print("nhap lai so nguen duong: ") 
    elif n == 0:
        print("dung chuong trinh: ")
        break
    else:
        tong = 0
        for index in range (1, n +1):
            tong += index
            print(f"tong cac so {n} la: {tong}")