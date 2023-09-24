# =================================================================================== #
def login_sukses():
  print('=============================================================') #Menu yang tersedia setelah melakukan Login
  print(f'Halo {nama}, Selamat Datang Di Kalkulator Segitiga Pythagoras')
  print('[1] Mencari Sisi Alas')
  print('[2] Mencari Sisi Tegak')
  print('[3] Mencari Sisi Miring')
  print('=============================================================')

  #While untuk Looping apabila input yang dimasukkan User tidak sesuai, akan diminta kembali memasukkan input yang benar
  while True:
    operasi = input('Silahkan Pilih Operasi yang anda inginkan : ')

    if operasi == '1': #Untuk Menentukan sisi alas
      print('=============================================================')
      sisi_miring = float(input('Masukkan Sisi Miring : '))
      sisi_tegak = float(input('Masukkan Sisi Tegak : '))
      sisi_alas = (sisi_miring**2 - sisi_tegak**2)**0.5
      print(f'Panjang Sisi Alas adalah {sisi_alas}')
      print('===========================Selesai===========================')

      break
    elif operasi == '2': #Untuk Menentukan sisi tegak
      print('=============================================================')

      sisi_miring = float(input('Masukkan Sisi Miring : '))
      sisi_alas = float(input('Masukkan Sisi Alas : '))
      sisi_tegak = (sisi_miring**2 - sisi_alas**2)**0.5
      print(f'Panjang Sisi Tegak adalah {sisi_tegak}')
      print('===========================Selesai===========================')

      break
    elif operasi == '3': #Untuk Menentukan sisi miring
      print('=============================================================')

      sisi_alas = float(input('Masukkan Sisi Alas : '))
      sisi_tegak = float(input('Masukkan Sisi Tegak : '))
      sisi_miring = (sisi_alas**2 + sisi_tegak**2)**0.5
      print(f'Panjang Sisi Miring adalah {sisi_miring}')
      print('===========================Selesai===========================')

      break
    else:
      print('Maaf pilihan tidak valid, Silahkan coba lagi')
      print('=============================================================')
# =================================================================================== #

# =================================================================================== #
print('=======================Login Mahasiswa=======================') #Login Untuk Masuk ke Kalkulator
nama = input('Masukkan Nama : ')
nim = int(input('Masukkan NIM : '))

while True: #untuk Looping apabila Paswword salah, akan diminta memasukkan ulang Password
  password = int(input('Masukkan Password :')) 
  if password == nim: #Password yang dimasukkan sama dengan NIM
    login_sukses()
    break #bagian dari while, untuk keluar dari Looping apabila password benar, dan masuk ke Kalkulator
  else:
    print('===========Password anda salah, silahkan coba lagi===========')
# =================================================================================== #
