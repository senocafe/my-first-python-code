daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
print('Tampilkan vaiable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku dengan indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print('\nTampilkan buku dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan dengan for in range, dimana tipe data tiap elemn berbeda2')
daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika Kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
#add comment

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen kedua')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nKembalikan semua daftar buku kemudian pop')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


