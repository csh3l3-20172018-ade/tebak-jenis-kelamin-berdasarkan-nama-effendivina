class Nama:
    nama = ""
    total = ""
    Pr = ""
    Lk = ""

    def __init__(self, nama):                   # contructor
        self.nama = nama                        # inisialisasi nama dan atribut lainnya
        self.total = 0
        self.Lk = 0
        self.Pr = 0

    def hitungJumlah(self):
        if self.nama == 'muhammad':             # kondisi bagi orang dengan nama muhammad
            print('100% Laki laki')
        else:
            # menghitung jumlah huruf yang frekuensinya lebih banyak di nama perempuan (a,i,u,e,t,l)
            self.Pr = self.nama.count('i') + self.nama.count('a') + self.nama.count('u') \
                      + self.nama.count('e') + self.nama.count('t') + self.nama.count('l')
            # menghitung jumlah huruf yang frekuensinya lebih banyak di nama laki-laki (b,d,o)
            self.Lk = self.nama.count('b')+self.nama.count('d')+self.nama.count('o')
            self.total = self.Lk + self.Pr
            # menampilkan perbedaan persen kemungkinan
            print ("{:.1f}".format((self.Lk/self.total)*100),'% Laki laki')
            print("{:.1f}".format((self.Pr / self.total) * 100), '% Perempuan')

if __name__ == "__main__":
    # meminta inputan nama dari user tanpa singkatan lalu membuat inputan menjadi lowercase
    namaLeng = input("Silahkan ketik nama lengkap Anda: ").lower()
    # membagi nama lengkap sesuai dengan jumlah kata yang ada
    namaDep = namaLeng.split()
    # menginisiasi sebuah class Nama bernama test dengan menginputkan kata pertama dari nama sebagai parameter constructor
    test = Nama(namaDep[0])
    # memanggil methode hitungJumlah di class Nama
    test.hitungJumlah()
