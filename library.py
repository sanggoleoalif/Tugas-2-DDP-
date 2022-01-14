import random
import string
import sys
import fileinput


def anggota(fname, badge):  # Fungsi untuk menambah Anggota Baru dengan 2 parameter yang diambil yaitu Nama Anggota, dan Status Anggota
    # Membuat Kode Anggota dengan kata kunci LNF dan diakhiri oleh 3 digit bilangan random
    kode = "LNF" + "".join(random.choice(string.digits) for _ in range(3))
    # Membuat list yg mencangkup 3 hal yaitu Kode Anggota, Nama Anggota, dan Status Anggota
    line = [kode, fname, badge]
    # Membuka File anggota.txt dengan "a" sebagai append yang berarti menambahkan tulisan baru ke dalam file text
    with open("anggota.txt", "a") as f:
        # Menulis baris list line yang sudah dibuat sebelumnya, dan memisahkan setiap Kode Anggota, Nama Anggota, dan Status Anggota menggunakan ","
        f.writelines(",".join(line))
        f.write("\n")  # Membuat enter baru
    print("Pendaftaran anggota dengan kode",
          kode, "atas nama", fname, "berhasil.", "\n")  # Memverifikasi kepada pelanggan bahwa pendaftaran telah berhasil


def buku(title, fname, stock):  # Fungsi untuk menambah Buku Baru dengan 3 parameter yang diambil yaitu Judul Buku, Nama Penulis, dan Stok Buku
    # Apabila nama berupa 2 kata dan 1 kata berisi 2 huruf setelah itu spasi, maka spasi tersebut harus dihapus
    nama = fname.replace(" ", "").upper()
    isi = str(stock)  # Jumlah Stok dari buku
    kode = "".join(nama[0:3]) + \
        "".join(random.choice(string.digits) for _ in range(
            3))  # Membuat Kode Buku dengan kata kunci 3 huruf pertama Nama Penulis dan diakhiri oleh 3 digit bilangan random
    # Membuat list yg mencangkup 4 hal yaitu Kode Buku, Judul Buku, Nama Penulis, dan Stok Buku
    line = [kode, title, fname, isi]
    # Membuka File buku.txt dengan "a" sebagai append yang berarti menambahkan tulisan baru ke dalam file text
    with open("buku.txt", "a") as f:
        # Menulis baris list line yang sudah dibuat sebelumnya, dan memisahkan setiap Kode Buku, Judul Buku, Nama Penulis, dan Stok Buku menggunakan ","
        f.writelines(",".join(line))
        f.write("\n")  # Membuat enter baru
    print("Penambahan buku baru dengan kode",
          kode, "dan judul", title, "berhasil.", "\n")  # Memverifikasi kepada pelanggan bahwa pendaftaran telah berhasil


# Fungsi untuk mengecheck Kode Buku dengan 1 parameter yang diambil yaitu Kode Buku
def cekKodeBuku(check):
    # Membuka File buku.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("buku.txt", "r") as f:
        lines = f.readlines()  # Membaca semua baris yang berada di dalam file buku.txt
    for line in lines:  # Membuat perulangan untuk setiap baris yang berada di dalam file buku.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        # Mengecheck apabila Kode Buku berada di dalam list dengan index 0, yang mana jika di check di dalam buku.txt merupakan Kode Buku
        if check == currentLine[0]:
            return True  # Mengembalikan nilai True


# Fungsi untuk mengecheck Kode Anggota dengan 1 parameter yang diambil yaitu Kode Anggota
def cekKodeAnggota(check):
    # Membuka File anggota.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("anggota.txt", "r") as f:
        lines = f.readlines()  # Membaca semua baris yang berada di dalam file anggota.txt
    for line in lines:  # Membuat perulangan untuk setiap baris yang berada di dalam file anggota.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        # Mengecheck apabila Kode Anggota berada di dalam list dengan index 0, yang mana jika di check di dalam anggota.txt merupakan Kode Anggota
        if check == currentLine[0]:
            return True  # Mengembalikan nilai True


# Fungsi untuk mengecheck Stok Buku dengan 1 parameter yang diambil yaitu Kode Buku
def cekStokBuku(check):
    # Membuka File buku.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("buku.txt", "r") as f:
        lines = f.readlines()  # Membaca semua baris yang berada di dalam file buku.txt
    for line in lines:  # Membuat perulangan untuk setiap baris yang berada di dalam file buku.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        # Mengecheck apabila Kode Buku berada di dalam list dengan index 0, yang mana jika di check di dalam buku.txt merupakan Kode Buku
        if check == currentLine[0]:
            # Mengecheck apabila Stok Buku yang berada di list dengan index 3 lebih dari 0
            if int(currentLine[3]) > 0:
                return True  # Mengembalikan nilai True


def peminjamanCek(name):  # Fungsi untuk mengecheck Kode Anggota yang berada di Peminjaman.txt dengan 1 parameter yang diambil yaitu Kode Anggota
    # Membuat variabel f untuk Membuka File peminjaman.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    f = open("peminjaman.txt", "r")
    text = f.read()  # Membaca semua baris yang berada di dalam file peminjaman.txt
    if name in text:  # Mengecheck apabila Kode Anggota berada di dalam text
        return True  # Mengembalikan nilai True


# Fungsi untuk menambah Peminjaman ke dalam peminjaman.txt dengan 2 parameter yang diambil yaitu Kode Anggota, dan Kode Buku
def peminjamanTambah(name, book):
    # Membuat variabel filename untuk Membuka File peminjaman.txt
    filename = "peminjaman.txt"
    # Membuka File peminjaman.txt
    with fileinput.FileInput(filename, inplace=True) as f:
        for line in f:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
            if name in line:  # Mengecheck apabila Kode Anggota berada di dalam baris
                # Menghitung panjang baris dikurang dengan 1
                length = len(line) - 1
                increase = "," + book  # Membuat buku baru dengan "," didepannya
                # Mengganti baris akhir dengan buku baru yang diakhiri dengan enter
                print(line.replace(line[length], increase), end="\n")
            else:  # Apabila Kode Anggota tidak berada di dalam baris
                print(line, end='')  # Menulis baris seperti biasa


def stokKurang(book):  # Fungsi untuk mengurangi stok buku di dalam buku.txt dengan 1 parameter yang diambil yaitu Kode Buku
    filename = "buku.txt"  # Membuat variabel filename untuk Membuka File buku.txt
    with fileinput.FileInput(filename, inplace=True) as f:  # Membuka File buku.txt
        for line in f:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
            # Membuat list yang dipisahkan dengan "," di dalam 1 baris
            currentLine = line.split(",")
            if book in line:  # Mengecheck apabila Kode Buku berada di dalam baris
                # Mengurangi stok buku yang berada di list dengan index 3 dikurang dengan 1
                decrease = str(int(currentLine[3]) - 1)
                # Mengganti list dengan index ke-3 yang berada di line dengan hasil pengurangan stok, yang diakhiri dengan enter
                print(line.replace(currentLine[3], decrease), end="\n")
            else:  # Apabila Kode Buku tidak berada di dalam baris
                print(line, end='')  # Menulis baris seperti biasa


def peminjaman(name, book):  # Fungsi untuk menambah Peminjaman ke dalam peminjaman.txt dengan 2 parameter yang diambil yaitu Kode Anggota, dan Kode Buku
    # Membuat list yg mencangkup 2 hal yaitu Kode Anggota, dan Kode Buku
    lineFull = [name, book]
    # Membuka File peminjaman.txt dengan "a" sebagai append yang berarti menambahkan tulisan baru ke dalam file text
    with open("peminjaman.txt", "a") as f:
        # Menulis baris list line yang sudah dibuat sebelumnya, dan memisahkan setiap Kode Anggota, dan Kode Buku menggunakan ","
        f.writelines(",".join(lineFull))
        f.write("\n")  # Membuat enter baru
        return True  # Mengembalikan nilai True


# Fungsi untuk mengecheck Kode Buku Peminjaman di dalam peminjaman.txt dengan 1 parameter yang diambil yaitu Kode Buku
def cekKodeBukuPeminjaman(check):
    # Membuka File peminjaman.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("peminjaman.txt", "r") as f:
        lines = f.readlines()  # Membaca semua baris yang berada di dalam file peminjaman.txt
    for line in lines:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        # Menghitung panjang "," dari list currentLine
        length = len(currentLine)
        # Membuat variabel yang berisi Kode Buku dengan enter dibelakangnya
        checkEnd = check + "\n"
        # Membuat perulangan untuk l dalam jangka 1 sampai panjang "," dari list currentLine
        for l in range(1, length):
            # Mengecheck apabila Kode Buku sama dengan currentLine[l] (index sesuai dengan perulangan yang diperiksa)
            if check == currentLine[l]:
                return True  # Mengembalikan nilai True
            # Mengecheck apabila Kode Buku Akhir sama dengan currentLine[l] (index sesuai dengan perulangan yang diperiksa)
            elif checkEnd == currentLine[l]:
                return True  # Mengembalikan nilai True


# Fungsi untuk mengecheck Kode Anggota Peminjaman di dalam peminjaman.txt dengan 2 parameter yang diambil yaitu Kode Anggota, dan Kode Buku
def cekKodeAnggotaPeminjaman(check, book):
    # Membuka File peminjaman.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("peminjaman.txt", "r") as f:
        lines = f.readlines()  # Membaca semua baris yang berada di dalam file peminjaman.txt
    for line in lines:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        # Mengecheck apabila Kode Anggota berada di dalam list dengan index 0, yang mana jika di check di dalam peminjaman.txt merupakan Kode Anggota
        if check == currentLine[0]:
            if book in line:  # Mengecheck apabila Kode Buku berada di dalam baris
                return True  # Mengembalikan nilai True


# Fungsi untuk mengecheck Status Anggota Peminjaman di dalam anggota.txt dengan 1 parameter yang diambil yaitu Kode Anggota
def cekStatusAnggota(name):
    # Membuka File anggota.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("anggota.txt", "r") as f:
        lines = f.readlines()  # Membaca semua baris yang berada di dalam file anggota.txt
    for line in lines:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        length = len(line)  # Menghitung panjang baris
        # Mengecheck apabila Kode Anggota berada di dalam list dengan index 0, yang mana jika di check di dalam anggota.txt merupakan Kode Anggota
        if name == currentLine[0]:
            # Mengembalikan nilai berupa baris yang berisi Status Anggota
            return line[length - 2]


# Fungsi untuk mengecheck Pengembalian Buku Peminjaman dari setiap Anggota yang merupakan karyawan NF atau tidak dengan 4 parameter yang diambil yaitu Kode Buku, Kode Anggota, Hari Pengembalian, Status Anggota
def cekPengembalianBuku(book, name, day, status):
    if status == "1":  # Mengecheck apabila Status Anggota bernilai 1 maka Anggota tersebut termasuk Karyawan NF
        if day == 0:  # Mengecheck apabila Hari Pengembalian bernilai 0 maka Anggota tersebut mengembalikan tepat waktu
            print("Pengembalian buku", book, "oleh", name, "berhasil.\n")
        elif day > 0:  # Mengecheck apabila Hari Pengembalian bernilai lebih dari 0 maka Anggota tersebut dikenakan denda senilai 1000/hari untuk Anggota yang merupakan Karyawan NF
            print("Total denda =", day * 1000)
            print("Pengembalian buku", book, "oleh", name, "berhasil.\n")
            return True
        else:  # Mengecheck apabila Hari Pengembalian bernilai negatif maka akan tampil error code
            print("Keterlambatan pengembalian tidak boleh bernilai negatif!\n")
            return False
    else:  # Mengecheck apabila Status Anggota tidak bernilai 1 maka Anggota tersebut tidak termasuk Karyawan NF
        if day == 0:  # Mengecheck apabila Hari Pengembalian bernilai 0 maka Anggota tersebut mengembalikan tepat waktu
            print("Pengembalian buku", book, "oleh", name, "berhasil.\n")
        elif day > 0:  # Mengecheck apabila Hari Pengembalian bernilai lebih dari 0 maka Anggota tersebut dikenakan denda senilai 2500/hari untuk Anggota yang bukan merupakan Karyawan NF
            print("Total denda =", day * 2500)
            print("Pengembalian buku", book, "oleh", name, "berhasil.\n")
            return True
        else:  # Mengecheck apabila Hari Pengembalian bernilai negatif maka akan tampil error code
            print("Keterlambatan pengembalian tidak boleh bernilai negatif!\n")
            return False


def stokTambah(book):  # Fungsi untuk menambah stok buku di dalam buku.txt dengan 1 parameter yang diambil yaitu Kode Buku
    filename = "buku.txt"  # Membuat variabel filename untuk Membuka File buku.txt
    with fileinput.FileInput(filename, inplace=True) as f:  # Membuka File buku.txt
        for line in f:  # Membuat perulangan untuk setiap baris yang berada di dalam file buku.txt
            # Membuat list yang dipisahkan dengan "," di dalam 1 baris
            currentLine = line.split(",")
            if book in line:  # Mengecheck apabila Kode Buku berada di dalam baris
                # Menambah stok buku yang berada di list dengan index 3 ditambah dengan 1
                increase = str(int(currentLine[3]) + 1)
                # Mengganti list dengan index ke-3 yang berada di line dengan hasil penambahan stok, yang diakhiri dengan enter
                print(line.replace(currentLine[3], increase), end="\n")
            else:  # Apabila Kode Buku tidak berada di dalam baris
                print(line, end='')  # Menulis baris seperti biasa


# Fungsi untuk mengurangi peminjaman buku di dalam peminjaman.txt dengan 2 parameter yang diambil yaitu Kode Anggota, dan Kode Buku
def bukuPeminjamanKurang(name, book):
    # Membuat variabel filename untuk Membuka File peminjaman.txt
    filename = "peminjaman.txt"
    # Membuka File peminjaman.txt
    with fileinput.FileInput(filename, inplace=True) as f:
        for line in f:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
            # Membuat list yang dipisahkan dengan "," di dalam 1 baris
            currentLine = line.split(",")
            # Menghitung panjang "," dari list currentLine
            lengthCurrentLine = len(currentLine)
            bookEnd = book + "\n"  # Membuat variabel yang berisi Kode Buku dengan enter dibelakangnya
            # Membuat perulangan untuk l dalam jangka 1 sampai panjang "," dari list currentLine
            for l in range(1, lengthCurrentLine):
                # Membuat variabel yang berisi Kode Buku yang dipilih dengan "," didepannya
                r = "," + currentLine[l]
                # Mengecheck apabila Kode Anggota berada di dalam list dengan index 0, yang mana jika di check di dalam peminjaman.txt merupakan Kode Anggota
                if name in currentLine[0]:
                    # Mengecheck apabila Kode Buku berada di dalam list dengan index l, yang mana jika di check di dalam peminjaman.txt merupakan Kode Buku yang berjumlah lebih dari 1 dan berada di tengah baris
                    if book == currentLine[l]:
                        # Mengganti variabel yang berisi Kode Buku yang dipilih dengan string kosong dan diakhiri dengan string kosong juga
                        print(line.replace(r, ""), end="")
                    # Mengecheck apabila Kode Buku berada di dalam list dengan index 1, yang mana jika di check di dalam peminjaman.txt merupakan Kode Buku yang berjumlah 1
                    elif bookEnd == currentLine[1]:
                        # Mencetak String kosong kedalam Line yang ditentukan
                        print("", end="")
                    # Mengecheck apabila Kode Buku berada di dalam list dengan index l, yang mana jika di check di dalam peminjaman.txt merupakan Kode Buku yang berjumlah lebih dari 1 dan berada di akhir baris
                    elif bookEnd == currentLine[l]:
                        # Mengganti variabel yang berisi Kode Buku yang dipilih dengan string kosong dan diakhiri dengan string kosong juga
                        print(line.replace(r, ""), end="\n")
            # Apabila Kode Anggota tidak berada di dalam baris
            if name not in currentLine[0]:
                print(line, end="")  # Menulis baris seperti biasa


def cetakDaftar():  # Fungsi untuk mencetak daftar buku dengan peminjam-nya
    # Membuka File buku.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("buku.txt", "r") as f:
        lines = f.readlines()  # Membaca semua baris yang berada di dalam file buku.txt
    # Membuka File peminjaman.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("peminjaman.txt", "r") as f1:
        lines1 = f1.readlines()  # Membaca semua baris yang berada di dalam file peminjaman.txt
    # Membuka File anggota.txt dengan "r" sebagai read yang berarti membaca tulisan yang berada di dalam file text
    with open("anggota.txt", "r") as f2:
        lines2 = f2.readlines()  # Membaca semua baris yang berada di dalam file anggota.txt
    buku = []  # Membuat list yg mencangkup Kode Buku
    judul = []  # Membuat list yg mencangkup Judul Buku
    penulis = []  # Membuat list yg mencangkup Penulis Buku
    peminjaman = []  # Membuat list yg mencangkup Kode Anggota Peminjam Buku
    for line in lines:  # Membuat perulangan untuk setiap baris yang berada di dalam file buku.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        buku.append(currentLine[0])  # Menambahkan Kode Buku kedalam list buku
        # Menambahkan Judul Buku kedalam list judul
        judul.append(currentLine[1])
        # Menambahkan Penulis Buku kedalam list penulis
        penulis.append(currentLine[2])
    for line in lines1:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
        # Membuat list yang dipisahkan dengan "," di dalam 1 baris
        currentLine = line.split(",")
        # Menambahkan Kode Anggota Peminjam Buku kedalam list peminjam
        peminjaman.append(currentLine[0])
    # Membuat perulangan untuk i dalam jangka 0 sampai panjang index dari list buku
    for i in range(0, len(buku)):
        n = 1  # Membuat variabel berisi nilai 1 untuk mereset nilai variabel dalam setiap perulangan
        print("\nJudul:", judul[i])  # Mencetak Judul Buku
        print("Penulis:", penulis[i])  # Mencetak Penulis Buku
        print("Daftar Peminjam:")  # Mencetak Daftar Peminjam
        for line in lines1:  # Membuat perulangan untuk setiap baris yang berada di dalam file peminjaman.txt
            # Membuat list yang dipisahkan dengan "," di dalam 1 baris
            currentLine = line.split(",")
            if buku[i] in line:  # Mengecheck apabila Kode Buku berada di salah satu baris file peminjaman.txt
                for line1 in lines2:  # Membuat perulangan untuk setiap baris yang berada di dalam file anggota.txt
                    # Membuat list yang dipisahkan dengan "," di dalam 1 baris
                    currentLine1 = line1.split(",")
                    # Mengecheck apabila Status Anggota bernilai 1
                    if currentLine1[2] == "1\n":
                        k = "(x)"  # Membuat variabel k yang berisi string "(x)"
                    else:  # Mengecheck apabila Status Anggota tidak bernilai 1
                        k = ""  # Membuat variabel k yang berisi string kosong
                    # Mengecheck Kode Anggota yang berada di file peminjaman.txt berada di dalam baris Kode Anggota di file anggota.txt
                    if currentLine[0] in currentLine1[0]:
                        # Mencetak sesuai format yaitu nomor, nama, dan status anggota contoh (1. Budi(x))
                        print("{}. {}{}".format(n, currentLine1[1], k))
                        n += 1  # Nilai n ditambah 1 setiap perulangan
                        break  # Memberhentikan perulangan
    print(end="\n")  # Memberikan enter di akhir baris


# Pembukaan dan Pilihan Menu
while True:
    print("*" * 5, "SELAMAT DATANG DI NF LIBRARY", 5 * "*",
          """\nMENU:
[1] Tambah Anggota Baru
[2] Tambah Buku Baru
[3] Pinjam Buku
[4] Kembalikan Buku
[5] Lihat Data Peminjaman
[6] Keluar""")

    # Variable Masukkan Input Pilihan
    pilihan = input("Masukkan menu pilihan Anda: ")

    # Hasil dari Pilihan
    if pilihan == "1":

        print("\n" + "*" * 3, "PENDAFTARAN ANGGOTA BARU", 3 * "*")
        namaAnggota = str(input("Masukkan nama: "))
        tipeAnggota = str(
            input("Apakah merupakan karyawan NF Group? (Y/T): "))

        if tipeAnggota == "Y":
            anggota(namaAnggota, "1")
            continue
        elif tipeAnggota == "T":
            anggota(namaAnggota, "2")
            continue

        else:
            print("Masukkan sesuai format (Y/T)\n")
            continue

    elif pilihan == "2":

        print("\n" + "*" * 3, "PENAMBAHAN BUKU BARU", 3 * "*")
        judulBuku = str(input("Judul: "))
        penulisBuku = str(input("Penulis: "))

        if len(penulisBuku) < 3:
            print("Masukkan minimal 3 karakter")
            continue

        stokBuku = input("Stok: ")

        try:
            val = int(stokBuku)
            pass

        except ValueError:
            print("Masukkan nilai berupa angka!\n")
            continue

        buku(judulBuku, penulisBuku, stokBuku)

    elif pilihan == "3":

        print("\n" + "*" * 3, "PEMINJAMAN BUKU", 3 * "*")
        kodeBuku = str(input("Kode buku: "))

        if cekKodeBuku(kodeBuku) == True:
            pass
        else:
            print("Kode buku tidak ditemukan. Peminjaman gagal.\n")
            continue

        kodeAnggota = str(input("Kode anggota: "))

        if cekKodeAnggota(kodeAnggota) == True:
            pass
        else:
            print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
            continue

        if cekStokBuku(kodeBuku) == True:
            pass
        else:
            print("Stok buku kosong. Peminjaman gagal.\n")
            continue

        if peminjamanCek(kodeAnggota) == True:
            peminjamanTambah(kodeAnggota, kodeBuku)
            stokKurang(kodeBuku)
            print("Peminjaman buku", kodeAnggota,
                  "oleh", kodeBuku, "berhasil.")
            continue
        else:
            pass

        if peminjaman(kodeAnggota, kodeBuku) == True:
            stokKurang(kodeBuku)
            print("Peminjaman buku", kodeAnggota,
                  "oleh", kodeBuku, "berhasil.")
            continue

    elif pilihan == "4":

        print("\n" + "*" * 3, "PENGEMBALIAN BUKU", 3 * "*")
        kodeBuku = str(input("Kode buku: "))

        if cekKodeBukuPeminjaman(kodeBuku) == True:
            pass
        else:
            print("Kode buku tidak ditemukan. Peminjaman gagal.\n")
            continue

        kodeAnggota = str(input("Kode anggota: "))

        if cekKodeAnggotaPeminjaman(kodeAnggota, kodeBuku) == True:
            pass
        else:
            print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
            continue

        status = cekStatusAnggota(kodeAnggota)
        pengembalianBuku = int(
            input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat): "))

        if cekPengembalianBuku(kodeBuku, kodeAnggota, pengembalianBuku, status) == False:
            continue
        stokTambah(kodeBuku)
        bukuPeminjamanKurang(kodeAnggota, kodeBuku)

    elif pilihan == "5":

        print("\n" + "*" * 3, "DAFTAR PEMINJAMAN BUKU", 3 * "*")
        cetakDaftar()

    elif pilihan == "6":

        print("Terima kasih atas kunjungan Anda...")
        sys.exit()

    else:

        print("Masukkan pilihan dengan benar!")
        continue
