import tkinter as tk

def bai_1_1():
    cua_so = tk.Tk()
    cua_so.title("Cua so dau tien")
    cua_so.geometry("400x300") #WxH

    cua_so.mainloop()

def bai_1_2():
    cua_so = tk.Tk()
    cua_so.title("Ung dung demo")
    cua_so.geometry("400x300") #WxH
    cua_so.resizable(False, False) #Khong cho thay doi kich thuoc cua so

    nhan = tk.Label(cua_so, text="Xin chao, Tkinter!", font=("Arial", 20))
    nhan.pack(pady=20)

    cua_so.mainloop()

def bai_2():
    cua_so = tk.Tk()
    cua_so.title("Vi du ve Frame")
    cua_so.geometry("400x300") #WxH

    khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
    khung_tren.pack(fill="x")

    khung_duoi = tk.Frame(cua_so, bg="lightyellow")
    khung_duoi.pack(fill="both", expand=True)

    tk.Label(khung_tren, text="Khung tren", bg="lightblue").pack(pady=10)
    tk.Label(khung_duoi, text="Khung duoi", bg="lightyellow").pack(pady=10)

    cua_so.mainloop()

if __name__ == "__main__":
    bai_1_1()
    bai_1_2()
    bai_2()