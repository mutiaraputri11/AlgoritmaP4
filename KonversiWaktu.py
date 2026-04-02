jumlah_hari = int(input("Masukkan jumlah hari: "))

tahun = jumlah_hari // 365
sisa_hari = jumlah_hari % 365

bulan = sisa_hari // 30
hari = sisa_hari % 30

print("\n=== Hasil Konversi ===")
print("Tahun : ", tahun)
print("Bulan : ", bulan)
print("Hari : ", hari)