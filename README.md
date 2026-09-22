# Studi_Kasus_5_Graceilla_079

Nama : Graceilla Tifunny Glory Hutagalung

NIM : 079

Kelas : B

SCREENSHOT HASIL/OUTPUT::

<img width="960" height="600" alt="Screenshot 2026-09-22 215440" src="https://github.com/user-attachments/assets/41e11b7b-1e22-4e31-801c-177663124335" />

PENJELASAN KODE PROGRAM :

1. Membuat Fungsi

   def hitung_biaya(jenis_kamar, lama_menginap):
  
-  def  = perintah untuk bikin fungsi
​
-  hitung_biaya  = nama fungsinya
​
-  (jenis_kamar, lama_menginap)  = parameter, tempat menampung nilai yang akan dipakai di dalam fungsi
 
 if jenis_kamar == "Standard":
    tarif = 200000
  elif jenis_kamar == "Deluxe":
    tarif = 350000
  else:
    return"Jenis kamar tidak tersedia"
 
-  if  = cek kondisi pertama, kalau kamarnya Standard, harganya 200.000
​
-  elif  = kalau bukan yang di atas, cek yang kedua, kalau Deluxe harganya 350.000
​
-  else  = kalau bukan dua-duanya, kasih pesan kamar tidak ada
​
-  return  = mengembalikan hasil keluaran dari fungsi
 
 total = tarif * lama_menginap
 return total
 
-  *  = perkalian, harga dikali jumlah malam
​
-  return total  = hasil akhirnya dikembalikan ke pemanggil fungsi
 
2. Mengisi Data
 
 jenis = "Deluxe"
 masuk_hari = 22
 masuk_bulan = 9
 masuk_tahun = 2026
 keluar_hari = 25
 keluar_bulan = 9
 keluar_tahun = 2026
 
-  =  = menyimpan nilai ke variabel
​
- Di sini kita isi sendiri datanya: pilih kamar Deluxe, tanggal masuk dan keluar
 
3. Menghitung Lama Menginap
 
 lama = keluar_hari - masuk_hari
 
-  -  = pengurangan, tanggal keluar dikurangi tanggal masuk → hasilnya 3 malam
 
4. Memanggil Fungsi
 
 bayar = hitung_biaya(jenis, lama)
 
-  hitung_biaya(jenis, lama)  = memanggil fungsi yang sudah dibuat, mengirimkan nilai  jenis  dan  lama  sebagai argumen
​
- Hasil yang dikembalikan fungsi disimpan ke variabel  bayar 
 
5. Menampilkan Hasil
 
 print("Jenis Kamar       :",jenis)
 print("Tanggal Check-In  :",masuk_hari, "September", masuk_tahun)
 print("Tanggal Check-Out :",keluar_hari, "September",keluar_tahun)
 print("Total Biaya       : Rp",bayar)
 
-  print()  = menampilkan tulisan/angka ke layar
​
- tanda  ,  = menyambungkan tulisan tetap dengan isi variabel
​
- Garis  ====== untuk dipakai biar tampilan rapi seperti struk
