# Tugas Pertemuan 1
# Menghitung Volume Tabung

print("=== PROGRAM MENGHITUNG VOLUME TABUNG ===")

# Input jari-jari dan tinggi
r = float(input("Masukkan jari-jari tabung: "))
t = float(input("Masukkan tinggi tabung: "))

# Memilih nilai phi
print("\nPilih nilai phi:")
print("1. 22/7")
print("2. 3.14")

pilihan = input("Masukkan pilihan (1/2): ")

# Menentukan nilai phi
if pilihan == "1":
    pi = 22 / 7
elif pilihan == "2":
    pi = 3.14
else:
    print("Pilihan tidak valid.")
    exit()

# Menghitung volume
volume = pi * r * r * t

# Menampilkan hasil
print("Volume tabung =", int(volume))