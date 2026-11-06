import sqlite3
import os
from datetime import datetime


THU_MUC_HIEN_TAI = os.path.dirname(os.path.abspath(__file__))
TEN_FILE_CSDL = os.path.join(THU_MUC_HIEN_TAI, "tu_dien.db")


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS tu_dien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tu_khoa TEXT NOT NULL UNIQUE,
            loai_tu TEXT NOT NULL,
            nghia TEXT NOT NULL,
            da_hoc INTEGER NOT NULL DEFAULT 0
        )
    """)
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS lich_su (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tu_khoa_tim TEXT NOT NULL,
            thoi_gian TEXT NOT NULL
        )
    """)
    ket_noi.commit()
    ket_noi.close()


def them_tu(tu_khoa, loai_tu, nghia):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    try:
        con_tro.execute(
            "INSERT INTO tu_dien (tu_khoa, loai_tu, nghia) VALUES (?, ?, ?)",
            (tu_khoa, loai_tu, nghia)
        )
        ket_noi.commit()
        ket_qua = True
    except sqlite3.IntegrityError:
        ket_qua = False
    ket_noi.close()
    return ket_qua


def lay_toan_bo_tu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, tu_khoa, loai_tu, nghia, da_hoc FROM tu_dien ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


def tim_kiem_tu(tu_khoa):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    con_tro.execute(
        "INSERT INTO lich_su (tu_khoa_tim, thoi_gian) VALUES (?, ?)",
        (tu_khoa, thoi_gian)
    )
    con_tro.execute(
        "SELECT id, tu_khoa, loai_tu, nghia, da_hoc FROM tu_dien WHERE tu_khoa LIKE ?",
        ("%" + tu_khoa + "%",)
    )
    ket_qua = con_tro.fetchall()
    ket_noi.commit()
    ket_noi.close()
    return ket_qua


def danh_dau_da_hoc(id_tu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("UPDATE tu_dien SET da_hoc = 1 WHERE id = ?", (id_tu,))
    ket_noi.commit()
    ket_noi.close()


def xoa_tu(id_tu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM tu_dien WHERE id = ?", (id_tu,))
    ket_noi.commit()
    ket_noi.close()


def lay_lich_su():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT tu_khoa_tim, thoi_gian FROM lich_su ORDER BY id DESC LIMIT 20")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua


def thong_ke_theo_loai_tu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT loai_tu, COUNT(*) FROM tu_dien GROUP BY loai_tu")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua