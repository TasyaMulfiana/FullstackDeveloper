class ContohKelas:
    def __init__(self):
        self.__atribut_private = 42

    def __metode_private(self):
        print("Ini adalah metode private.")

    def metode_publik(self):
        print("Ini adalah metode publik.")
        print("Nilai atribut private:", self.__atribut_private)
        self.__metode_private()


objek = ContohKelas()

# Mengakses atribut private dari luar kelas akan menghasilkan AttributeError
# print(objek.__atribut_private)

# Memanggil metode private dari luar kelas akan menghasilkan AttributeError
# objek.__metode_private()

# Mengakses atribut private melalui metode publik
objek.metode_publik()