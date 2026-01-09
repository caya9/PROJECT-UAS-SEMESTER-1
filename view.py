class ViewMahasiswa:
    def tampilkan_tabel(self, data):
        print("\n===== DATA MAHASISWA =====")
        print("{:<10} {:<20} {:<10}".format("NIM", "Nama", "Nilai"))
        print("-" * 45)

        for mhs in data:
            print("{:<10} {:<20} {:<10}".format(mhs.nim, mhs.nama, mhs.nilai))

