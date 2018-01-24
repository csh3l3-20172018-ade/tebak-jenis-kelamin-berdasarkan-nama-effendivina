class Nama:
    nama = ""
    total = ""
    Pr = ""
    Lk = ""

    def __init__(self, nama):
        self.nama = nama
        self.total = 0
        self.Lk = 0
        self.Pr = 0

    def hitungJumlah(self):
        if self.nama == 'muhammad':
            print('100% Laki laki')
        else:
            self.Pr = self.nama.count('i') + self.nama.count('a') + self.nama.count('u') \
                      + self.nama.count('e') + self.nama.count('t') + self.nama.count('l')
            self.Lk = self.nama.count('b')+self.nama.count('d')+self.nama.count('o')
            print(self.Pr, self.Lk)
            self.total = self.Lk + self.Pr
            print ((self.Lk/self.total)*100,'% Laki laki')
            print ((self.Pr/self.total)*100,'% Perempuan')

if __name__ == "__main__":
    namaLeng = input("Silahkan ketik nama lengkap Anda: ").lower()
    namaDep = namaLeng.split()
    test = Nama(namaDep[0])
    test.hitungJumlah()
