print("Bai 3.2")
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000
print("Ten: ", ten)
print("Diem toan: ", diem_toan)
print("Diem van: ", diem_van)
print("So luong mon hoc: ", so_luong_mon_hoc)

print("\nBai 5.1")
a = 17
b = 5
print("Tong: ", a + b)
print("Hieu: ", a - b)
print("Tich: ", a * b)
print("Thuong: ", a / b)
print("Chia lay nguyen: ", a // b)
print("Phan du: ", a % b)
print("Luy thua: ", a ** b)

print("\nBai 5.2")
diem = 6.5
tuoi = 20
check_diem = (diem >= 6.5 and diem < 8.0)
check_tuoi = (tuoi < 18 or tuoi > 60)
phu_dinh_diem = not check_diem
phu_dinh_tuoi = not check_tuoi
print("Diem: ", diem)
print("Tuoi: ", tuoi)
print("Check diem: ", check_diem)
print("Check tuoi: ", check_tuoi)
print("Phu dinh diem: ", phu_dinh_diem)
print("Phu dinh tuoi: ", phu_dinh_tuoi)

print("\nBai 5.3")
x = 10
x += 5
print(x)
x-= 3
print(x)
x*= 2
print(x)
x/= 4
print(x)
x//= 2
print(x)
x**= 3
print(x)

danh_sach = [1, 2, 3, "python"]
print(3 in danh_sach)
test = danh_sach
print(test is danh_sach)

print("\nBai 5.4")
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

print("\nBai 6.1")
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))

print("\nBai 6.2")
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0
dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)

print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))