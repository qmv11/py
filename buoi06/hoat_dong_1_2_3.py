#1.1
print("Bai 1.1:\n")
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bscnn(a, b):
    return a * b // uscln(a, b)
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
print(uscln(24, 36))
print(bscnn(4, 6))
print(kiem_tra_nguyen_to(29))
print(kiem_tra_so_hoan_thien(28)) # 28 = 1 + 2 + 4 + 7 + 14

#1.2
print("\nBai 1.2:\n")
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return # ham khong tra ve gia tri (tra ve None)
def chia_lay_thuong_du(a, b):
    return a // b, a % b # tra ve nhieu gia tri qua tuple
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, du: {du}")

#2
print("\nBai 2:\n")
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")
gioi_thieu("An") # dung het gia tri mac dinh
gioi_thieu("Binh", 20) # ghi de tuoi
gioi_thieu("Chi", lop="CNTT01") # dung tham so tu khoa, bo qua tuoi
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19) # thu tu tham so tu khoa co the dao lon

#3.1
print("\nBai 3.1:\n")
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong()) # khong truyen so nao -> tra ve 0

#3.2
print("\nBai 3.2:\n")
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f" {khoa}: {gia_tri}")
in_thong_tin("Nguyen Van A", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")