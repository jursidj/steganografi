from PIL import Image

def baca_pesan_dari_gambar(gambar):
    img = Image.open(gambar) #Buka Gambar
    
    data = list(img.getdata()) # Ambil data piksel gambar
    
    pesan_biner = ""
    for item in data:
        pesan_biner += str(item[0] & 1) # Ambil bit terakhir dari setiap piksel
        
    pesan = ""
    for i in range(0, len(pesan_biner), 8):
        byte = pesan_biner[i:i + 8]
        pesan += chr(int(byte,2)) #ubah setiap byte biner menjadi karakter
    
    return pesan

# contoh penggnaan
gambar = "gambar_sisipan.png"

pesan_terbaca = baca_pesan_dari_gambar(gambar)
print("Pesan yang terbaca:", pesan_terbaca)
