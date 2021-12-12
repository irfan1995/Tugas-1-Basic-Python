#Program yang dapat menghitung luas lingkaran

print("Soal-3 Program untuk menentukan apakah seorang siswa lulus ujian atau tidak")

nilai_teori = float(input("Input nilai ujian teori: "))
nilai_praktek = float(input("Input nilai ujian praktek: "))

if nilai_teori >= 70 and nilai_praktek >= 70 :
    print("Selamat, Anda lulus!")
elif nilai_teori >= 70 and nilai_praktek < 70 :
    print("Anda harus mengulang ujian praktek.")
elif nilai_teori < 70 and nilai_praktek >= 70 :
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")