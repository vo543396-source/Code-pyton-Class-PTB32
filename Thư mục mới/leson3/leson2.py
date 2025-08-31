'''
các loại toán tử trong python
1. toán tử số học (+, -, *, /)
  3. toán tử đặc biệt 
   - chia lấy dư : %
   - lũy thừa : * *
   - chia lấy phần nguyên : //
'''
# ví dụ về toán tử số học
a = 10
b = 3
c = a * b 
print("sau khi a * b là: ", c)
#chia lấy dư
d = a % b # 10 % 3 => (9 + 1)/3
print("sau khi chia lấy dư: ", d)
#phép toán lũy thừa 
e = a**b # 10**3 = > 10 * 10 *10
print("sau khi lấy lũy thừa: ", e)
#phép chia lấy phần nguyên 
r = a // b # 10 // 3 = 3
print("sau khi chia lấy phần nguyên: ", r)

'''
2. toán tử gán
- giá trị gán: =
- cộng và gán: +=
- trừ và gán: -=
- nhân và gán: *=
- chia và gán: /=
- chia lấy phần nguyên và gán: //=
'''

#ví dụ toán tự gán
gan = 10 
gan += 10 #gan = gan +10
print("sau khi gán: ", gan)
gan %= 3
print("sau khi chia lấy phần dư và gán: ", gan)

'''
3. toán tử so sánh
- toán tử so sánh cơ bản: >, <, >=, <=
- toán tử bằng: ==
- toan tu khác: !=
'''
#ví dụ về toán tử so sánh 
num1 = 10
num2 = 30 
if num1 != num2:
    print("đúng")
else:
    print("sai")

'''
4. toán tử logic
and : và logic/ tất cả các điều kiện đều phải đúng mới thỏa mãn
our: hoặc logic/ chỉ cần một điều kiện đúng sẽ thõa mãn 
not: phủ định/ đảo ngược logic
'''

t = 20
f = 30 
if not(t == f) and t <= f:
    print(True)
else:
    print(False)