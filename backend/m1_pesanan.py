# backend/m1_pesanan.py

class ArrayPesanan:
    def __init__(self):
        self.data = [] 

    # Menambah pesanan REGULER: Masuk paling belakang. O(1) - Sangat cepat.
    def tambah_reguler(self, pesanan):
        self.data.append(pesanan)

    # Menambah pesanan VIP: Masuk paling depan. O(n) - Sangat lambat jika datanya banyak.
    # Karena semua data di belakangnya harus digeser satu per satu.
    def tambah_vip(self, pesanan):
        self.data.insert(0, pesanan)


# Struktur Node (Simpul) wajib ada untuk membuat Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListPesanan:
    def __init__(self):
        self.head = None
        self.tail = None

    # Menambah pesanan REGULER: Masuk paling belakang. O(1) - Sangat cepat.
    # Karena kita sudah menyimpan posisi 'tail' (ekor), jadi tinggal disambung.
    def tambah_reguler(self, pesanan):
        node_baru = Node(pesanan)
        if not self.head:
            self.head = self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru

    # Menambah pesanan VIP: Masuk paling depan. O(1) - Sangat cepat.
    # Tidak perlu menggeser data lain, cukup ubah arah panah (next) ke head yang lama.
    def tambah_vip(self, pesanan):
        node_baru = Node(pesanan)
        node_baru.next = self.head
        self.head = node_baru
        if not self.tail:
            self.tail = node_baru