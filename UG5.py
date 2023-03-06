class Karyawan:
    _nama = None
    _umur = None
    _jenisKelamin = None
    _upahPerHari = None



    def __init__(self, nama, umur):
        self._nama = nama
        self._umur = umur

    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin
    
    def setUpahPerHari(self, upahPerHari):
        self._upahPerHari = upahPerHari
    
    
    def getJenisKelamin(self):
        return self._jenisKelamin
        
    def getUpahPerHari(self):
        return self._upahPerHari
    
    def hitungGajiBulanan(self, hari):
        self._hari = hari
        if self.getUpahPerHari() == None:
             print("ERROR! Upah per Hari belum di inputkan")
        else:
             print("Gaji Bulan ini : Rp ", self._hari * self._upahPerHari)
       
            
        
    def printInfo(self):
            print("========== INFO ==========")
            print("Nama : ", self._nama)
            print("Umur : ", self._umur)
            print("Jenis Kelamin : ", self._jenisKelamin)
            print("Upah Per Hari : ", self._upahPerHari)

        

orang1 = Karyawan("Haniif", 90)
orang1.printInfo()
orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo()
orang1.hitungGajiBulanan(28)
orang2.hitungGajiBulanan(30)