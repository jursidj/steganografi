from PIL import Image

#Fungsi untuk menyisipkan pesan ke dalam gambar

def sisipkan_pesan(gambar, pesan):
    img = Image.open(gambar)
    #buka gambar
    
    pesan_biner = ''.join(format(ord(c), '08b') for c in pesan)
    #ubah pesan menjadi format biner
    
    data = list(img.getdata()) 
    #ambil data piksel gambar
    
    if len(pesan_biner) > len(data):
        raise ValueError("Ukuran pesan terlalu besar untuk gambar ini.")
    
    pesan_biner += '0' * (len(data) - len(pesan_biner)) #Padding pesan dengan nol jika pesan lebih pendek dari gambar
    
    data_baru = []
    index = 0
    for item in data:
        if index < len(pesan_biner):
            # Mengubah bit terakhir piksel menjadi bit pesan
            data_baru.append((item[0] & 0xFE) | int(pesan_biner[index]))
            index += 1
        else:
            data_baru.append(item)
            
    img.putdata(data_baru) #Masukan data piksel yang telah diubah ke dalam gambar
    
    img.save("gambar_sisipan.png")
    #simpan gambar baru dengan pesan sisipan
    
    print("Pesan berhasil dalam gambar")
    
#contoh penggunaan
pesan = "IIB Darmajaya bebas P3 2.5 Juta dan Cashback 1 juta sebelum bulan Juni 2023"
gambar = "gambar.png"

sisipkan_pesan(gambar,pesan)
