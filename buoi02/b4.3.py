cau = " Toi dang HOC Python rat vui "
print(cau.strip()) # bo khoang trang 2 dau
print(cau.strip().upper()) # in hoa toan bo
print(cau.strip().lower()) # in thuong toan bo
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split()) # tach thanh danh sach cac tu
print(len(cau.strip().split())) # dem so tu trong cau
print(cau.count("o")) # dem so lan xuat hien ky tu 'o'
print(cau.find("Python")) # vi tri bat dau cua "Python"
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))