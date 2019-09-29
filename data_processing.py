'''kode ini akan menerima N entri sesuai yang diinput, lalu selama data yang diinput bukan -999
, maka akan menyimpan terus data-datanya sampai N entri.
Setelah N entri data disimpan, program akan memproses dan menghitung rata-rata data
, lalu data terbesar yang ada di N buah data dan juga data terkecilnya.
Syarat pengolahan data terjadi apabila data yang diinput antara 100 dan 200 (100 dan 200 tidak diinclude).
Jika data tidak antara 100 dan 200, program tetap berlanjut, tetapi tidak akan diolah.
Contoh : 5 buah entri data dengan masing-masing = 1 , 150 , 300 , 15 , -5
----maka program hanya akan mengolah data 150 dan 300 saja untuk selanjutnya dihitung rata-rata dan nilai max dan min nya. '''




N = int(input ("jumlah entry :"))
k = []
for i in range(1, N+1):
    a = int (input ("masukkan data :"))
    if a != -999 :
        if 100 < a < 200 :
            k.append(a)
        else :
            print ("sesuaikan syarat!")
            continue
    else :
        print ("data tidak valid!")
        break

print (k)
print ("rata2 nya :" , sum(k)/float(len(k)))
print ("Data terbesar :" , max(k))
print ("Data terkecil :" , min(k))
