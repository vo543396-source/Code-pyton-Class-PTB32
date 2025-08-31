tong = 0
print("Các số nguyên tố bé hơn 100 là:")

for n in range(2, 100): 
    is_prime = True
    for i in range(2, n):
        if n % i == 0: 
            is_prime = False
            break
   

print("\nTổng các số nguyên tố là:", tong)

'''
Dùng vòng lặp for để kiểm tra từng số từ 2 đến 99.
Với mỗi số n, thử chia n cho các số nhỏ hơn nó.
Nếu không chia hết cho số nào => là số nguyên tố.
In ra số đó và cộng vào tổng.
'''
