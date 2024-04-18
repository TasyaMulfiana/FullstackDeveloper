class Matematika:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def tambah(self):
        return self.angka1 + self.angka2

    def kurang(self):
        return self.angka1 - self.angka2

    def kali(self):
        return self.angka1 * self.angka2

    def bagi(self):
        return self.angka1 / self.angka2

# Main Program
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

matematika = Matematika(angka1, angka2)

print("Hasil penjumlahan:", matematika.tambah())
print("Hasil pengurangan:", matematika.kurang())
print("Hasil perkalian:", matematika.kali())
print("Hasil pembagian:", matematika.bagi())