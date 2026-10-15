# backend/m2_antrean.py

# --- BAGIAN 1: STACK (Tumpukan) ---
# Wajib ada untuk fitur Undo/Redo dan Kasir (Postfix)
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return None
        
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return None

    def is_empty(self):
        return len(self.data) == 0


# --- BAGIAN 2: QUEUE (Antrean) ---
# Untuk antrean layanan pesanan kurir
class QueueNaif:
    def __init__(self):
        self.data = []
        self.geseran = 0 # Menghitung berapa elemen yang tergeser

    def enqueue(self, pesanan):
        self.data.append(pesanan)

    def dequeue(self):
        if len(self.data) > 0:
            # Mengambil indeks 0 memaksa seluruh elemen di belakangnya bergeser (O(n))
            pesanan_keluar = self.data.pop(0) 
            self.geseran += len(self.data)
            return pesanan_keluar
        return None

class QueueCircular:
    def __init__(self, kapasitas=300000):
        self.data = [None] * kapasitas
        self.kapasitas = kapasitas
        self.front = 0
        self.rear = 0
        self.count = 0
        self.geseran = 0 # Penanda bahwa versi circular tidak pernah menggeser data

    def enqueue(self, pesanan):
        if self.count < self.kapasitas:
            self.data[self.rear] = pesanan
            # Penunjuk berputar kembali ke 0 jika mencapai batas kapasitas
            self.rear = (self.rear + 1) % self.kapasitas
            self.count += 1

    def dequeue(self):
        if self.count > 0:
            pesanan_keluar = self.data[self.front]
            # Hanya memajukan penunjuk front, TIDAK ADA elemen yang digeser (O(1))
            self.front = (self.front + 1) % self.kapasitas 
            self.count -= 1
            return pesanan_keluar
        return None