def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000
    else:
        return "Jenis kamar tidak tersedia"

    total = tarif * lama_menginap
    return total
jenis = "Deluxe"
masuk_hari = 22
masuk_bulan = 9
masuk_tahun = 2026
keluar_hari = 25
keluar_bulan = 9
keluar_tahun = 2026
lama = keluar_hari - masuk_hari
bayar = hitung_biaya(jenis, lama)
print("====== DETAIL PEMESANAN HOTEL ======")
print("Jenis Kamar          :", jenis)
print("Tanggal Check-In     :", masuk_hari, "September", masuk_tahun)
print("Tanggal Check-Out    :",keluar_hari, "September", keluar_tahun)
print("Lama Menginap        :", lama, "malam")
print("Total BIaya          : Rp", bayar)