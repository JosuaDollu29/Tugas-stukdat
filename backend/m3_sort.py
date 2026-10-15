# backend/m3_sort.py

def linear_search(data, target_oid):
    perbandingan = 0
    for i in range(len(data)):
        perbandingan += 1
        if data[i]['oid'] == target_oid:
            return i, perbandingan # Kembalikan indeks dan jumlah perbandingan
    return -1, perbandingan

def binary_search(data_terurut, target_oid):
    perbandingan = 0
    lo = 0
    hi = len(data_terurut) - 1
    
    while lo <= hi:
        perbandingan += 1
        mid = (lo + hi) // 2
        
        if data_terurut[mid]['oid'] == target_oid:
            return mid, perbandingan
        elif data_terurut[mid]['oid'] < target_oid:
            lo = mid + 1
        else:
            hi = mid - 1
            
    return -1, perbandingan

def merge_sort(data, kunci):
    perbandingan = [0] 
    pemindahan = [0]
    
    def rekursif(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        kiri = rekursif(arr[:mid])
        kanan = rekursif(arr[mid:])
        
        hasil = []
        i = j = 0
        
        while i < len(kiri) and j < len(kanan):
            perbandingan[0] += 1
            if kiri[i][kunci] <= kanan[j][kunci]:
                hasil.append(kiri[i])
                pemindahan[0] += 1
                i += 1
            else:
                hasil.append(kanan[j])
                pemindahan[0] += 1
                j += 1
                
        while i < len(kiri):
            hasil.append(kiri[i])
            pemindahan[0] += 1
            i += 1
        while j < len(kanan):
            hasil.append(kanan[j])
            pemindahan[0] += 1
            j += 1
            
        return hasil
        
    data_terurut = rekursif(data)
    return data_terurut, perbandingan[0], pemindahan[0]