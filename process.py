from data import Mahasiswa

class ProsesMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_mahasiswa(self, nim, nama, nilai):
        if not nim.isdigit():
            raise ValueError("NIM harus berupa angka")

        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 - 100")

        mahasiswa = Mahasiswa(nim, nama, nilai)
        self.data_mahasiswa.append(mahasiswa)

    def get_semua_data(self):
        return self.data_mahasiswa
