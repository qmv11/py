import csv
import matplotlib.pyplot as plt

danh_sach = []
with open("sanpham.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        danh_sach.append({
            "ma": row["MaSP"],
            "ten": row["TenSP"],
            "gia": int(row["Gia"]),
            "sl": int(row["SoLuong"])
        })

tong_sp = len(danh_sach)
tong_gia = sum(sp["gia"] for sp in danh_sach)
gia_tb = tong_gia / tong_sp if tong_sp > 0 else 0

sp_max = max(danh_sach, key=lambda x: x["gia"])

print(f"Tổng số sản phẩm: {tong_sp}")
print(f"Giá trung bình: {gia_tb:,.2f} VNĐ")
print(f"Sản phẩm giá cao nhất: {sp_max['ten']} ({sp_max['gia']} VNĐ)")

ten_sp = [sp["ten"] for sp in danh_sach]
so_luong = [sp["sl"] for sp in danh_sach]

plt.figure(figsize=(10, 6))
plt.bar(ten_sp, so_luong, color='skyblue')
plt.xlabel("Tên sản phẩm")
plt.ylabel("Số lượng tồn kho")
plt.title("Biểu đồ số lượng tồn kho")
plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig("bieudo.png")
plt.close()

sp_sap_het = [sp for sp in danh_sach if sp["sl"] < 10]

with open("canh_bao_hang.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["MaSP", "TenSP", "Gia", "SoLuong"])
    for sp in sp_sap_het:
        writer.writerow([sp["ma"], sp["ten"], sp["gia"], sp["sl"]])

print("Đã lưu biểu đồ vào 'bieudo.png' và danh sách cảnh báo vào 'canh_bao_hang.csv'")