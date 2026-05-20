count = 0
for i in range(1, 8):
    revenue = int(input(f"Nhập doanh thu Ngày {i}: "))

    if revenue >= 5000000:
        count+=1
    
print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print(f"Tổng doanh thu cả tuần: {revenue}")
print(f"Doanh thu trung bình mỗi ngày: {revenue/7}")
print(f"Số ngày đạt doanh thu mục tiêu (>= 5000000): {count} ngày")