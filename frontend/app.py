# frontend/app.py
import tkinter as tk
import time
import sys
import os

# Menghubungkan folder frontend dengan backend
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from m2_antrean import QueueNaif, QueueCircular
from baca_data import muat_csv
from m3_sort import linear_search, binary_search, merge_sort

# Variabel Global
q_naif = QueueNaif()
q_circular = QueueCircular()
data_mentah = []
data_terurut_oid = [] 

def aksi_load_data():
    global data_mentah, data_terurut_oid
    hasil_text.insert(tk.END, "Memuat data CSV... Mohon tunggu.\n")
    app.update()
    
    # 1. Membaca data CSV
    mulai = time.time()
    data_mentah = muat_csv()
    
    # Memasukkan ke antrean M2
    for pesanan in data_mentah:
        if pesanan['status'] == 'ANTRE':
            q_naif.enqueue(pesanan)
            q_circular.enqueue(pesanan)
            
    waktu_load = (time.time() - mulai) * 1000
    hasil_text.insert(tk.END, f"Sukses! {len(data_mentah)} data dibaca ({waktu_load:.2f} ms).\n")
    
    # 2. M3: Menyusun data dengan Merge Sort sebagai syarat Binary Search
    hasil_text.insert(tk.END, "Menyusun data dengan Merge Sort untuk persediaan Search...\n")
    app.update()
    data_terurut_oid, banding, pindah = merge_sort(data_mentah, 'oid')
    hasil_text.insert(tk.END, f"Siap! ({banding} perbandingan dilakukan).\n")
    hasil_text.insert(tk.END, "-"*40 + "\n")

def aksi_uji_queue():
    if not q_naif.data:
        hasil_text.insert(tk.END, "Antrean kosong! Klik LOAD DATA dulu.\n")
        return
        
    # Uji Queue Naif
    mulai_naif = time.time()
    pesanan_keluar_naif = q_naif.dequeue()
    waktu_naif = (time.time() - mulai_naif) * 1000
    
    # Uji Queue Circular
    mulai_circular = time.time()
    pesanan_keluar_circular = q_circular.dequeue()
    waktu_circular = (time.time() - mulai_circular) * 1000
    
    hasil_text.insert(tk.END, f"Melayani Pesanan: {pesanan_keluar_naif['oid']} - {pesanan_keluar_naif['pelanggan']}\n")
    hasil_text.insert(tk.END, f"Queue Naif     : {waktu_naif:.2f} ms | Elemen bergeser: {q_naif.geseran}\n")
    hasil_text.insert(tk.END, f"Queue Circular : {waktu_circular:.2f} ms | Elemen bergeser: {q_circular.geseran}\n")
    hasil_text.insert(tk.END, "-"*40 + "\n")

def aksi_uji_search():
    if not data_mentah:
        hasil_text.insert(tk.END, "Data kosong! Klik LOAD DATA dulu.\n")
        return
        
    target = "O-000004" # Target pesanan yang dicari
    hasil_text.insert(tk.END, f"Mencari pesanan {target}...\n")
    
    # Uji Linear Search
    mulai_linear = time.time()
    idx_linear, banding_linear = linear_search(data_mentah, target)
    waktu_linear = (time.time() - mulai_linear) * 1000
    
    # Uji Binary Search
    mulai_binary = time.time()
    idx_binary, banding_binary = binary_search(data_terurut_oid, target)
    waktu_binary = (time.time() - mulai_binary) * 1000
    
    hasil_text.insert(tk.END, f"Linear Search : Baris {idx_linear} | {banding_linear} perbandingan | {waktu_linear:.3f} ms\n")
    hasil_text.insert(tk.END, f"Binary Search : Baris {idx_binary} | {banding_binary} perbandingan | {waktu_binary:.3f} ms\n")
    hasil_text.insert(tk.END, "-"*40 + "\n")


# === PENGATURAN UI JENDELA APLIKASI ===
app = tk.Tk()
app.title("Demo 2EZ4U Food Delivery")
app.geometry("600x550")

tombol_load = tk.Button(app, text="1. LOAD DATA (pesanan.csv)", command=aksi_load_data, bg="lightblue")
tombol_load.pack(pady=5)

tombol_uji_queue = tk.Button(app, text="2. Uji Queue (Keluarkan 1 Pesanan)", command=aksi_uji_queue, bg="lightgreen")
tombol_uji_queue.pack(pady=5)

tombol_uji_search = tk.Button(app, text="3. Uji Search (Cari Pesanan O-000004)", command=aksi_uji_search, bg="lightyellow")
tombol_uji_search.pack(pady=5)

hasil_text = tk.Text(app, height=20, width=70)
hasil_text.pack(padx=20, pady=10)

app.mainloop()