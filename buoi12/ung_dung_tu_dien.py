import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_tu_dien as db

DANH_SACH_LOAI_TU = ["Danh từ", "Động từ", "Tính từ", "Trạng từ", "Khác"]


class UngDungTuDien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Từ điển cá nhân")
        self.geometry("620x540")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_tu()

    def khoi_tao_giao_dien(self):
        # ---- Khung them tu ----
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Từ khóa:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_tu_khoa = tk.Entry(khung_nhap, width=30)
        self.o_nhap_tu_khoa.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Loại từ:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_loai_tu = ttk.Combobox(khung_nhap, values=DANH_SACH_LOAI_TU,
                                         width=27, state="readonly")
        self.chon_loai_tu.current(0)
        self.chon_loai_tu.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Nghĩa:").grid(row=2, column=0, sticky="w", pady=5)
        self.o_nhap_nghia = tk.Entry(khung_nhap, width=30)
        self.o_nhap_nghia.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Thêm từ", command=self.xu_ly_them_tu).grid(
            row=3, column=0, columnspan=2, pady=10)

        # ---- Khung tim kiem ----
        khung_tim_kiem = tk.Frame(self)
        khung_tim_kiem.pack(pady=5, padx=10, fill="x")

        tk.Label(khung_tim_kiem, text="Tìm kiếm:").pack(side="left")
        self.o_nhap_tim_kiem = tk.Entry(khung_tim_kiem, width=22)
        self.o_nhap_tim_kiem.pack(side="left", padx=5)
        tk.Button(khung_tim_kiem, text="Tìm",
                  command=self.xu_ly_tim_kiem).pack(side="left", padx=3)
        tk.Button(khung_tim_kiem, text="Hiển thị tất cả",
                  command=self.tai_lai_danh_sach_tu).pack(side="left", padx=3)
        tk.Button(khung_tim_kiem, text="Lịch sử tra cứu",
                  command=self.xu_ly_lich_su).pack(side="left", padx=3)

        # ---- Khung danh sach ----
        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_tu = tk.Listbox(khung_danh_sach, width=85, height=12)
        self.listbox_tu.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical",
                                   command=self.listbox_tu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_tu.config(yscrollcommand=thanh_cuon.set)

        # ---- Khung nut thao tac ----
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(khung_nut_thao_tac, text="Đánh dấu đã học",
                  command=self.xu_ly_danh_dau_da_hoc).grid(row=0, column=0, pady=5, padx=5)
        tk.Button(khung_nut_thao_tac, text="Xóa từ",
                  command=self.xu_ly_xoa_tu).grid(row=0, column=1, pady=5, padx=5)
        tk.Button(khung_nut_thao_tac, text="Thống kê theo loại từ",
                  command=self.xu_ly_thong_ke).grid(row=0, column=2, pady=5, padx=5)

    def tai_lai_danh_sach_tu(self):
        self.listbox_tu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_tu()
        for tu in self.danh_sach_hien_tai:
            id_tu, tu_khoa, loai_tu, nghia, da_hoc = tu
            trang_thai = "[Đã học]" if da_hoc == 1 else "[Chưa học]"
            self.listbox_tu.insert(tk.END, f"{trang_thai} {tu_khoa} - ({loai_tu}) - {nghia}")

    def xu_ly_them_tu(self):
        tu_khoa = self.o_nhap_tu_khoa.get().strip()
        loai_tu = self.chon_loai_tu.get()
        nghia = self.o_nhap_nghia.get().strip()

        if tu_khoa == "" or nghia == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ từ khóa và nghĩa.")
            return

        thanh_cong = db.them_tu(tu_khoa, loai_tu, nghia)
        if thanh_cong == False:
            messagebox.showerror("Lỗi", f"Tu '{tu_khoa}' đã tồn tại trong từ điển.")
            return

        self.o_nhap_tu_khoa.delete(0, tk.END)
        self.o_nhap_nghia.delete(0, tk.END)
        self.tai_lai_danh_sach_tu()
        messagebox.showinfo("Thành công", f"Đã thêm từ: {tu_khoa}")

    def xu_ly_tim_kiem(self):
        tu_khoa = self.o_nhap_tim_kiem.get().strip()
        if tu_khoa == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập từ khóa cần tìm.")
            return

        self.listbox_tu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.tim_kiem_tu(tu_khoa)
        for tu in self.danh_sach_hien_tai:
            id_tu, tu_khoa_db, loai_tu, nghia, da_hoc = tu
            trang_thai = "[Đã học]" if da_hoc == 1 else "[Chưa học]"
            self.listbox_tu.insert(tk.END, f"{trang_thai} {tu_khoa_db} - ({loai_tu}) - {nghia}")

        if len(self.danh_sach_hien_tai) == 0:
            messagebox.showinfo("Thông báo", f"Không tìm thấy từ nào chứa '{tu_khoa}'.")

    def xu_ly_danh_dau_da_hoc(self):
        lua_chon = self.listbox_tu.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một từ để đánh dấu đã học.")
            return
        id_tu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.danh_dau_da_hoc(id_tu)
        self.tai_lai_danh_sach_tu()

    def xu_ly_xoa_tu(self):
        lua_chon = self.listbox_tu.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một từ trong danh sách để xóa.")
            return
        id_tu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_tu(id_tu)
        self.tai_lai_danh_sach_tu()

    def xu_ly_lich_su(self):
        du_lieu_lich_su = db.lay_lich_su()
        if not du_lieu_lich_su:
            messagebox.showinfo("Thông báo", "Chưa có lịch sử tra cứu.")
            return

        cua_so_lich_su = tk.Toplevel(self)
        cua_so_lich_su.title("Lịch sử tra cứu (20 lần gần nhất)")
        cua_so_lich_su.geometry("420x400")

        listbox_lich_su = tk.Listbox(cua_so_lich_su, width=55, height=20)
        listbox_lich_su.pack(pady=10, padx=10, fill="both", expand=True)

        for dong in du_lieu_lich_su:
            tu_khoa_da_tim, thoi_gian = dong
            listbox_lich_su.insert(tk.END, f"{thoi_gian} - {tu_khoa_da_tim}")

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_loai_tu()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu từ vựng để thống kê.")
            return

        cac_loai_tu = [dong[0] for dong in du_lieu_thong_ke]
        so_luong = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(6, 4))
        plt.bar(cac_loai_tu, so_luong, color="cornflowerblue")
        plt.title("Số lượng từ theo loại từ")
        plt.xlabel("Loại từ")
        plt.ylabel("Số lượng từ")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ung_dung = UngDungTuDien()
    ung_dung.mainloop()