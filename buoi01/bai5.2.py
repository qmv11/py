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