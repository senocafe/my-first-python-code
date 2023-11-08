"""
Semua sitaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial   : langkah berurutan
2. Percabangan  : langkah melompat jika kondisi terpenuhi
3. Perulangan   : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Anak Menjawab, "Baik, apa yang harus saya lakukan ditoko?"')
print('Ibu Menjawab, "Beli satu botol susu, jika ada telur beli 6"')
print('Maka Anak pergi ke toko')
print('Anak bertanya ke toko, "Apakah susu ada?"')

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f'jumlah botol susu {jumlah_botol_susu} botol')
print(f'jumlah telur {jumlah_telur} butir')

if jumlah_botol_susu > 0:
    print('Anak mengecek harganya, dan ternyata cukup uangnya')
    if jumlah_telur >= 6:
        print('Anak membeli 6 butir telur')
    else:
        print('Anak tidak membeli telur')
    print('Anak membeli 1 botol susu')
else:
    print('Anak tidak jadi membeli susu')

print('Anak pulang kerumah')
print('Anak menyampaikan hasilnya kepada ibu')
