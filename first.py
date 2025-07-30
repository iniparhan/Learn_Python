'''
Case :
- 

'''

import pandas as pd

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {'username' : 'cakboyo', 'password' : 'pangerantampan'}
        self.is_login = False

    def login(self):
        if self.data['username'] == self.username and self.data['password'] == self.password:
            self.is_login = True
        else:
            self.is_login = False

        return self.is_login

class ParkingLot:
    def __init__(self, jenis_kendaraan, plat_nomor):
        self.jenis_kendaraan = jenis_kendaraan
        self.plat_nomor = plat_nomor
        
        self.vehicle_priority = {'car': [3, 2, 1], 'motor': [1, 2, 3], 'bus': 3}
        
        self.koordinat_row = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.koordinat_column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        
        self.isi_parkiran_lantai_1 = {}
        self.slot_parkiran_lantai_1 = {'motor': 30, 'mobil': 60}
        self.isi_parkiran_lantai_2 = {}
        self.slot_parkiran_lantai_2 = {'motor': 27, 'mobil': 63}
        self.isi_parkiran_lantai_3 = {}
        self.slot_parkiran_lantai_3 = {'motor': 27, 'mobil': 63}

    def koordinat_parkiran(self):
        self.koordinat = []

        for row in self.koordinat_row:
            for column in self.koordinat_column:
                self.koordinat.append(f'{column}{row}')
        
        return self.koordinat

    def parkir_lantai_1(self):
        self.koordinat = self.koordinat_parkiran()
        self.list_slot_parkir_motor = []

        for row in range(3):
            for column in self.koordinat_column:
                self.list_slot_parkir_motor.append(f'{column}{row}')

        
    
    def parkir_lantai_2(self):
        pass
    
    def parkir_lantai_3(self):
        pass

    def check_capacity(self):
        pass

class Laporan:
    def __init__(self):
        pass

    def total_kendaraan(self):
        pass

    def total_pendapatan(self):
        pass

    def posisi_kendaraan(self):
        pass

    def cek_ketersediaan_parkiran(self):
        pass


if __name__ == "__main__":
    
    # =================
    # Buat cek login
    # =================

    # username = 'cakboyo'
    # password = 'pangerantampan'

    # login = Login(username, password)
    
    # if login.login():
    #     print('Login Berhasil')
    # else:
        # print('Login Gagal, periksa kembali username dan password')
    pass
