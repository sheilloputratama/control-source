a = float(input("masukkan angka pertama: "))
b = float(input("masukkan angka kedua: "))
c = float(input("masukkan angka ketiga: "))

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c
else:
    print("Tidak ada nilai terbesar")

print("Angka terbesar adalah:", largest)