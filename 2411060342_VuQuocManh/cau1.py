danh_sach = [
    {"MaSP": "SP001", "TenSP": "Bút bi thiên long", "Gia": 3000, "SoLuong": 150},
    {"MaSP": "SP002", "TenSP": "Vở học sinh 96 trang", "Gia": 8000, "SoLuong": 8},
    {"MaSP": "SP003", "TenSP": "Bút chì 2B", "Gia": 2500, "SoLuong": 200}
]

def tim_sp(MaSP):
    for sp in danh_sach:
        if sp["MaSP"] == MaSP:
            return sp
    return None

def them_sp(MaSP, TenSP, Gia, SoLuong):
    
    danh_sach.append({"MaSP": MaSP, "TenSP": TenSP, "Gia": Gia, "SoLuong": SoLuong})
    print(f"-> Đã thêm thành công {TenSP}, mã {MaSP}")

def tim_kiem_theo_ten(danh_sach, tu_khoa):
    tu_khoa_lower = tu_khoa.lower()
    ket_qua = []
    for sp in danh_sach:
        if tu_khoa_lower in sp["TenSP"].lower():
            ket_qua.append(sp)
    return ket_qua

def tong_Gia_tri_ton_kho(danh_sach):
    tong = 0
    for sp in danh_sach:
        tong += sp["Gia"] * sp["SoLuong"]
    return tong

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac)) 
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

def hien_thi_menu():
    print("\n===== QUAN LY DANH SACH SAN PHAM =====")
    print("1. Thêm sản phẩm")
    print("2. Tìm kiếm theo tên")
    print("3. Tổng giá trị tồn kho")
    print("0. Thoát chương trình")

def in_danh_sach(danh_sach):
    print(f"{'MaSP':<10}{'TenSP':<30}{'Gia':<12}{'SoLuong':<10}")
    print("-" * 62)
    for sp in danh_sach:
        print(f"{sp['MaSP']:<10}{sp['TenSP']:<30}{sp['Gia']:<12}{sp['SoLuong']:<10}")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        in_danh_sach(danh_sach)
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        if lua_chon == "1":
            while True:
                ma = input("Nhập mã SP: ").strip()
                if tim_sp(ma) is not None:
                    print("Mã sản phẩm đã tồn tại! Không thể thêm")
                break
            ten = input("Nhập tên SP: ").strip()
            gia = nhap_so_nguyen("Nhập giá sản phẩm: ")
            sl = nhap_so_nguyen("Nhập số lượng sản phẩm: ")
            them_sp(ma, ten, gia, sl)
            print(f" Đã thêm sản phẩm '{ten}'.")
        elif lua_chon == "2":
            tu_khoa = input("Nhập từ khoá tên cần tìm: ").strip()
            ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)
            if ket_qua:
                print(f" Tìm thấy {len(ket_qua)} sản phẩm:")
                in_danh_sach(ket_qua)
            else:
                print(" Không tìm thấy sản phẩm nào.")
                
        elif lua_chon == "3":
            tong = tong_Gia_tri_ton_kho(danh_sach)
            print(f" Tổng giá trị tồn kho: {tong:,.0f} VNĐ")
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()