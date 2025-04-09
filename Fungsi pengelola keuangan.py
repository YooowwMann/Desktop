pengeluaran = {}

def tambah_pengeluaran(tanggal, deskripsi, jumlah):
    pengeluaran[tanggal] = {'deskripsi': deskripsi, 'jumlah': jumlah}

def tampilkan_pengeluaran():
    for tanggal, info in pengeluaran.items():
        print(f"Tanggal: {tanggal}, Deskripsi: {info['deskripsi']}, Jumlah: {info['jumlah']}")

def hapus_pengeluaran(tanggal):
    if tanggal in pengeluaran:
        del pengeluaran[tanggal]
        print(f"Pengeluaran pada tanggal {tanggal} telah dihapus.")
    else:
        print("Data pengeluaran tidak ditemukan.")

def edit_pengeluaran(tanggal, deskripsi, jumlah):
    if tanggal in pengeluaran:
        pengeluaran[tanggal] = {'deskripsi': deskripsi, 'jumlah': jumlah}
        print(f"Pengeluaran pada tanggal {tanggal} telah diedit.")
    else:
        print("Data pengeluaran tidak ditemukan.")

def cari_pengeluaran(tanggal):
    if tanggal in pengeluaran:
        info = pengeluaran[tanggal]
        print(f"Tanggal: {tanggal}, Deskripsi: {info['deskripsi']}, Jumlah: {info['jumlah']}")
    else:
        print("Data pengeluaran tidak ditemukan.")

def urutkan_pengeluaran():
    for tanggal in sorted(pengeluaran):
        info = pengeluaran[tanggal]
        print(f"Tanggal: {tanggal}, Deskripsi: {info['deskripsi']}, Jumlah: {info['jumlah']}")