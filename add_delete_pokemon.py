import mariadb
import sys

conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="abuser"
)

print("***PILIH SALAH SATU***")
print("1. Nambah Abiliti\n2. Hapus Abiliti")
while True:
    pilihan = input("Pilih Opsi: ")
    if not pilihan:
        print("OPSI GAK BOLEH KOSONG")
    else:
        break

if pilihan == "1":
    print("Masukkan nama Pokemon yang akan di tambahkan abilitinya")
    while True:
            pokemon = input("Nama Pokemon: ")

            if not pokemon:
                print("Nama pokemon gak boleh kosong") 
            else:
                abiliti_baru = input("Masukkan abiliti baru: ")
                
                if not abiliti_baru:
                    print("HARUS DI ISI")
                else:
                    query = f"INSERT INTO pokemon_mini SELECT nama, '{abiliti_baru}' AS abilities, species, weight, height FROM pokemon_mini WHERE nama = '{pokemon}' GROUP BY 1,2,3,4;"
                    break

elif pilihan == "2":
    print("Masukkan nama Pokemon yang akan di hapus abilitinya")
    while True:
            pokemon = input("Nama Pokemon: ")

            if not pokemon:
                print("Nama pokemon gak boleh kosong") 
            else:
                abiliti_del = input("Masukkan abiliti: ")
                
                if not abiliti_del:
                    print("HARUS DI ISI")
                else:
                    query = f"DELETE from pokemon_mini WHERE nama = '{pokemon}' AND abilities = '{abiliti_del}';"
                    break

cur = conn.cursor()
cur.execute(query)
conn.commit()
#print(query)