import tkinter as tk
from tkinter import messagebox

danh_sach_sp = []

def them_sp():
    ma = entry_ma.get().strip()
    ten = entry_ten.get().strip()
    gia_str = entry_gia.get().strip()
    sl_str = entry_sl.get().strip()

    if not ma or not ten:
        messagebox.showerror("Lỗi", "Mã SP và Tên SP không được để trống!")
        return
    try:
        gia = int(gia_str)
        soluong = int(sl_str)
        if gia < 0 or soluong < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Lỗi", "Giá và Số lượng phải là số nguyên dương hợp lệ!")
        return

    sp = {"ma": ma, "ten": ten, "gia": gia, "sl": soluong}
    danh_sach_sp.append(sp)
    
    hien_thi_danh_sach(danh_sach_sp)
    messagebox.showinfo("Thành công", "Đã thêm sản phẩm!")
    
    entry_ma.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_gia.delete(0, tk.END)
    entry_sl.delete(0, tk.END)

def hien_thi_danh_sach(ds):
    listbox.delete(0, tk.END)
    for sp in ds:
        chuoi = f"{sp['ma']} - {sp['ten']} - {sp['gia']}đ - SL: {sp['sl']}"
        listbox.insert(tk.END, chuoi)

def tim_kiem():
    tu_khoa = entry_tim.get().strip().lower()
    ket_qua = [sp for sp in danh_sach_sp if tu_khoa in sp['ten'].lower()]
    hien_thi_danh_sach(ket_qua)

root = tk.Tk()
root.title("Quản lý sản phẩm")
root.geometry("500x500")

nhap = tk.Frame(root, pady=10)
nhap.pack()

tk.Label(nhap, text="Mã SP:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_ma = tk.Entry(nhap, width=30)
entry_ma.grid(row=0, column=1)

tk.Label(nhap, text="Tên SP:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_ten = tk.Entry(nhap, width=30)
entry_ten.grid(row=1, column=1)

tk.Label(nhap, text="Giá:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_gia = tk.Entry(nhap, width=30)
entry_gia.grid(row=2, column=1)

tk.Label(nhap, text="Số lượng:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_sl = tk.Entry(nhap, width=30)
entry_sl.grid(row=3, column=1)

btn_them = tk.Button(root, text="Thêm sản phẩm", command=them_sp, bg="lightblue")
btn_them.pack(pady=5)

frame_search = tk.Frame(root, pady=10)
frame_search.pack()
tk.Label(frame_search, text="Tìm theo tên:").pack(side=tk.LEFT, padx=5)
entry_tim = tk.Entry(frame_search, width=20)
entry_tim.pack(side=tk.LEFT)
btn_tim = tk.Button(frame_search, text="Tìm", command=tim_kiem)
btn_tim.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, width=70, height=10)
listbox.pack(pady=10)

root.mainloop()