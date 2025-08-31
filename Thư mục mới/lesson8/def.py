'''
hàm là một khôi mã đuoc đặt tên sử dụng để thực hiện 1 loạt động cụ thể 
Hàm cho phep chia nhỏ chương trình thành cac phần nhỏ, giup quản li cac đoạn mã
dễ hơn, hàm co thể tai sử dụng lại nêu chương trình cần
'''
#tổng 2 sô
def tong_hai_so(a, b):
    tong = a+ b
    return tong 

#cach gan gia trị gan giam tiêp
c = 10
d = 20
ket_qua = tong_hai_so(c, d)
#cach gan gia tri truc tiep
ket_qua2 =tong_hai_so(40, 50)


print(f"tong cua {c} va {d} la: {ket_qua}")
print(f"tong cua a va b la: {ket_qua2}")

#ham khong tam so
def in_ket_qua():
    print("ket qua la: ")

in_ket_qua()