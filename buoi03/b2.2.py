ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#In ra theo tung hang
for hang in ma_tran:
    print(hang)
tong = 0
#In ra tung phan tu, duyet theo hang roi theo cot
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
        tong += phan_tu
    print()
print("Tong:", tong)