percentage = float(input("masukkan persentase nilai siswa: "))

if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Needs Improvement")