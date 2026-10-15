# backend/baca_data.py
import csv
import os

def muat_csv():
    # Menentukan lokasi file pesanan.csv (berada di folder 'data' di luar 'backend')
    lokasi_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'pesanan.csv')
    
    semua_pesanan = []
    
    try:
        # Buka file CSV
        with open(lokasi_file, mode='r', encoding='utf-8') as file:
            pembaca_csv = csv.reader(file)
            
            # Lewati baris pertama karena itu adalah baris judul (header: oid, pelanggan, dll)
            next(pembaca_csv) 
            
            # Membaca setiap baris pesanan
            for baris in pembaca_csv:
                # Struktur: [oid, pelanggan, resto, menu, harga, prioritas, t_masuk, t_selesai, status]
                # Pastikan mengubah tipe data angka (seperti harga dan prioritas) agar bisa diolah nanti
                pesanan = {
                    'oid': baris[0],
                    'pelanggan': baris[1],
                    'resto': baris[2],
                    'menu': baris[3],
                    'harga': int(baris[4]) if baris[4].isdigit() else 0,
                    'prioritas': int(baris[5]) if baris[5].isdigit() else 3,
                    't_masuk': baris[6],
                    't_selesai': baris[7],
                    'status': baris[8]
                }
                semua_pesanan.append(pesanan)
                
        print(f"Berhasil memuat {len(semua_pesanan)} data pesanan.")
        return semua_pesanan
        
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di lokasi {lokasi_file}")
        return []