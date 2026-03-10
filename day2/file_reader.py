import os

def analisis_file(nama_file):
    try:
        # Memastikan file ada sebelum dibuka
        if not os.path.exists(nama_file):
            print(f"Kesalahan: File '{nama_file}' tidak ditemukan.")
            return

        with open(nama_file, 'r', encoding='utf-8') as file:
            konten = file.read()
            
            # Menghitung metrik
            # .splitlines() menangani berbagai jenis newline (\n, \r\n)
            baris = konten.splitlines()
            jumlah_baris = len(baris)
            
            # .split() tanpa argumen membagi berdasarkan whitespace (spasi, tab, newline)
            jumlah_kata = len(konten.split())
            
            # Menghitung total karakter termasuk spasi
            jumlah_karakter = len(konten)
            preview = konten[:100]
            # Menampilkan hasil
            print("-" * 30)
            print(f"Statistik untuk File: {nama_file}")
            print("-" * 30)
            print(f"Jumlah Baris               : {jumlah_baris}")
            print(f"Jumlah Kata                : {jumlah_kata}")
            print(f"Jumlah 100 Karakter Pertama: {preview}")
            print(f"Jumlah Karakter            : {jumlah_karakter}")
            print("-" * 30)

    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

if __name__ == "__main__":
    file_target = input("Masukkan nama file (contoh: data.txt): ")
    analisis_file(file_target)