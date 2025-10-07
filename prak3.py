n = int (input("Masukkan nilai n untuk batas deret Fibonanci: "))

a, b = 0, 1

print("Deret Fibonanci hingga", n, ":")
while a <= n:
    print(a, end=" ")
    a, b, = a + b