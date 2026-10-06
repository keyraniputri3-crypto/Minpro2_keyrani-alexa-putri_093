from datetime import datetime

akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

tanaman = []


#ini buat login bang
def login():
    while True:
        print("--- LOGIN ---")
        username = input("Username: ").strip()
        password = input("Password: ")

        if username in akun:
            if password == akun[username]["password"]:
                print("Login berhasil")
                return akun[username]["role"]

        print("Username atau password salah")


def input_teks(pesan):
    while True:
        teks = input(pesan).strip()

        if teks != "":
            return teks

        print("Input tidak boleh kosong")


def input_angka(pesan):
    while True:
        teks = input(pesan).strip()

        if teks == "":
            print("Input tidak boleh kosong")
            continue

        valid = True

        for karakter in teks:
            if karakter not in "0123456789":
                valid = False
                break

        if valid:
            return int(teks)

        print("Input harus berupa bilangan bulat 0 atau lebih.")


def input_data():
    nama = input_teks("Nama tanaman: ")
    jenis = input_teks("Jenis tanaman: ")
    jumlah = input_angka("Jumlah tanaman: ")

    return {
        "nama": nama,
        "jenis": jenis,
        "jumlah": jumlah
    }


def tampilkan_data():
    print("--- DATA TANAMAN ---")

    if not tanaman:
        print("Belum ada data tanaman.")
    else:
        for i, data in enumerate(tanaman, 1):
            print("Data ke-", i)
            print("Nama   :", data["nama"])
            print("Jenis  :", data["jenis"])
            print("Jumlah :", data["jumlah"])


def pilih_data():
    for i, data in enumerate(tanaman, 1):
        print(i, ".", data["nama"])

    while True:
        nomor = input_angka("Pilih nomor data: ")

        if 1 <= nomor <= len(tanaman):
            return nomor - 1

        print("Masukkan nomor data yang tersedia.")


def tambah_data():
    print("--- TAMBAH DATA TANAMAN ---")
    tanaman.append(input_data())
    print("Data berhasil ditambahkan")


def ubah_data():
    print("--- UBAH DATA TANAMAN ---")

    if not tanaman:
        print("Belum ada data tanaman.")
    else:
        nomor = pilih_data()
        print("Masukkan data pengganti:")
        tanaman[nomor] = input_data()
        print("Data berhasil diubah")


def hapus_data():
    print("--- HAPUS DATA TANAMAN ---")

    if not tanaman:
        print("Belum ada data tanaman.")
    else:
        nomor = pilih_data()
        tanaman.pop(nomor)
        print("Data berhasil dihapus")


def menu_utama(role):
    while True:
        print("\n==============================")
        print(" PENDATAAN TANAMAN HIDROPONIK")
        print("==============================")
        print("User    :", role)
        print("Role    :", role)

        if role == "admin":
            print("1. Tambah Data Tanaman")
            print("2. Tampilkan Semua Data")
            print("3. Ubah Data Tanaman")
            print("4. Hapus Data Tanaman")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ").strip()

            if pilihan == "1":
                tambah_data()
            elif pilihan == "2":
                tampilkan_data()
            elif pilihan == "3":
                ubah_data()
            elif pilihan == "4":
                hapus_data()
            elif pilihan == "5":
                print("Berhasil keluar dari akun.")
                return
            else:
                print("Pilihan tidak valid")

        elif role == "user":
            print("1. Tampilkan Semua Data")
            print("2. Keluar")

            pilihan = input("Pilih menu (1-2): ").strip()

            if pilihan == "1":
                tampilkan_data()
            elif pilihan == "2":
                print("Berhasil keluar dari akun.")
                return
            else:
                print("Pilihan tidak valid")


while True:
    role = login()
    menu_utama(role)