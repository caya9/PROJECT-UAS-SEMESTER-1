from process import ProsesMahasiswa
from view import ViewMahasiswa

def main():
    proses = ProsesMahasiswa()
    view = ViewMahasiswa()

    while True:
        try:
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")
            nilai = int(input("Masukkan Nilai: "))

            proses.tambah_mahasiswa(nim, nama, nilai)

            lanjut = input("Tambah data lagi? (y/n): ")
            if lanjut.lower() != 'y':
                break

        except ValueError as e:
            print("Error:", e)

    view.tampilkan_tabel(proses.get_semua_data())

if __name__ == "__main__":
    main()
