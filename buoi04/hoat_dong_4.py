print("Bai 4.1")
chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))

so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

danh_sach = list((1, 2, 3)) #tuple -> list
bo_ba = tuple([4, 5, 6])    #list -> tuple
tap_hop = set([1, 2, 2, 3, 3, 3])   #list ->set (tu loai bo trung lap)
tu_dien = dict([("a", 1), ("b", 2)])

print(danh_sach, bo_ba, tap_hop, tu_dien)

print("\nBai 4.2\n")

so_hop_le = int(float("3.14"))
print(so_hop_le)

print("\nBai 4.3\n")
ket_qua = 5 + 2.5   # int + float -> Python tu dong chuyen thanh float
print(ket_qua, type(ket_qua))

ket_qua_2 = "Diem: " + str(8.5)     # phai ep str() tuong minh, Python KHONG tu dong noi str voi so
print(ket_qua_2)