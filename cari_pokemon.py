from threading import local
from pandas import isnull
import mariadb
import sys
from tabulate import tabulate

conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="abuser"
)

cur = conn.cursor()

print("PILIH KRITERIA YANG AKAN DI CARI, JIKA LEBIH DARI SATU DI PISAH MENGGUNAKAN SPASI")
while True:
    #print("PILIH KRITERIA YANG AKAN DI CARI, JIKA LEBIH DARI SATU DI PISAH MENGGUNAKAN SPASI")
    print("1. Nama Abiliti\n2. Jumlah abiliti\n3. Spesies\n4. Weight\n5. Height")
    kriteria = list(input("Pilih Kriteria: ").split())
    if not kriteria:
        print("KRITERIA GAK BOLEH KOSONG")
    else:
        break


for i in kriteria:
    
    if i == "1":
        print("Masukkan nama abiliti. Jika lebih dari satu, di pisah menggunakan spasi")
        while True:
            nama_abl = list(input("Abiliti: ").split())
            
            if not nama_abl:
                print("Nama gak boleh kosong") 
            else:
                rmv_char = "[]"
                nama_abl = f"({nama_abl})"
                for i in rmv_char:
                    nama_abl = nama_abl.replace(i,"")
                break
    
    elif i == "2":
        print("JUMLAH ABILITI\n1. kurang dari\n2. Lebih dari\n3. Sama dengan")
        while True:
            key = input("Pilih opsi: ")
        
            if not key:
                print("opsi gak boleh kosong")
            else:
                abiliti = input("Masukkan jumlah abiliti: ")

            if not abiliti:
                print("abiliti gak boleh kosong")
            else:
                if key == "1":
                    abiliti = f"< {abiliti}"
                elif key == "2":
                    abiliti = f"> {abiliti}"
                elif key == "3":
                    abiliti = f"= {abiliti}"
                break
    
    elif i == "3":
        print("Masukkan nama Spesies. Jika lebih dari satu, di pisah menggunakan spasi")

        while True:
            spesies = list(input("Spesies: ").split())

            if not spesies:
                print("Spesies gak boleh kosong")
            else:
                rmv_char = "[]"
                spesies = f"({spesies})"
                for i in rmv_char:
                    spesies = spesies.replace(i,"")
                break
    
    elif i == "4":
        print("PILIH WEIGHT\n1. kurang dari\n2. Lebih dari\n3. Sama dengan")

        while True:
            key = input("Pilih opsi: ")
            
            if not key:
                print("opsi gak boleh kosong")
            else:
                weight = input("Masukkan ukuran WEIGHT: ")

                if not weight:
                    print("weight gak boleh kosong")
                else:
                    if key == "1":
                        weight = f"< {weight}"
                    elif key == "2":
                        weight = f"> {weight}"
                    elif key == "3":
                        weight = f"= {weight}"
                    break
    elif i == "5":
        print("PILIH HEIGHT\n1. kurang dari\n2. Lebih dari\n3. Sama dengan")

        while True:
            key = input("Pilih opsi: ")
            
            if not key:
                print("opsi gak boleh kosong")
            else:
                height = input("Masukkan ukuran HEIGHT: ")

                if not height:
                    print("height gak boleh kosong")
                else:
                    if key == "1":
                        height = f"< {height}"
                    elif key == "2":
                        height = f"> {height}"
                    elif key == "3":
                        height = f"= {height}"
                    break


if ('nama_abl' in locals()) and ('abiliti' not in locals()) and ('spesies' not in locals()) and ('weight' not in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} group by 1;"
elif ('nama_abl' not in locals()) and ('abiliti' in locals()) and ('spesies' not in locals()) and ('weight' not in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon group by 1 having count(nama) {abiliti};"
elif ('nama_abl' not in locals()) and ('abiliti' not in locals()) and ('spesies' in locals()) and ('weight' not in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where species IN {spesies} group by 1;"
elif ('nama_abl' not in locals()) and ('abiliti' not in locals()) and ('spesies' not in locals()) and ('weight' in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where weight {weight} group by 1;"
elif ('nama_abl' not in locals()) and ('abiliti' not in locals()) and ('spesies' not in locals()) and ('weight' not in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where height {height} group by 1;"

elif ('nama_abl' in locals()) and ('abiliti' in locals()) and ('spesies' not in locals()) and ('weight' not in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' in locals()) and ('abiliti' not in locals()) and ('spesies' in locals()) and ('weight' not in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and species IN {spesies} group by 1;"
elif ('nama_abl' in locals()) and ('abiliti' not in locals()) and ('spesies' not in locals()) and ('weight' in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and weight {weight} group by 1;"
elif ('nama_abl' in locals()) and ('abiliti' not in locals()) and ('spesies' not in locals()) and ('weight' not in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and height {height} group by 1;"
elif ('nama_abl' not in locals()) and ('abiliti' in locals()) and ('spesies' in locals()) and ('weight' not in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where species IN {spesies} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' not in locals()) and ('abiliti' in locals()) and ('spesies' not in locals()) and ('weight' in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where weight {weight} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' not in locals()) and ('abiliti' in locals()) and ('spesies' not in locals()) and ('weight' not in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where height {height} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' not in locals()) and ('abiliti' not in locals()) and ('spesies' in locals()) and ('weight' in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where species IN {spesies} and weight {weight} group by 1;"
elif ('nama_abl' not in locals()) and ('abiliti' not in locals()) and ('spesies' in locals()) and ('weight' not in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where species IN {spesies} and height {height} group by 1;"
elif ('nama_abl' not in locals()) and ('abiliti' not in locals()) and ('spesies' not in locals()) and ('weight' in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where weight {weight} and height {height} group by 1;"

elif ('nama_abl' in locals()) and ('abiliti' in locals()) and ('spesies' in locals()) and ('weight' not in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and species IN {spesies} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' in locals()) and ('abiliti' in locals()) and ('spesies' not in locals()) and ('weight' in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and weight {weight} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' in locals()) and ('abiliti' in locals()) and ('spesies' not in locals()) and ('weight' not in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and height {height} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' in locals()) and ('abiliti' not in locals()) and ('spesies' in locals()) and ('weight' in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and species IN {spesies} and weight {weight} group by 1;"
elif ('nama_abl' in locals()) and ('abiliti' not in locals()) and ('spesies' in locals()) and ('weight' not in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and species IN {spesies} and height {height} group by 1;"
elif ('nama_abl' in locals()) and ('abiliti' not in locals()) and ('spesies' not in locals()) and ('weight' in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and weight {weight} and height {height} group by 1;"
elif ('nama_abl' not in locals()) and ('abiliti' in locals()) and ('spesies' in locals()) and ('weight' in locals()) and ('height' not in locals()):
    query = f"select nama from pokemon where species IN {spesies} and weight {weight} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' not in locals()) and ('abiliti' in locals()) and ('spesies' in locals()) and ('weight' not in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where species IN {spesies} and height {height} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' not in locals()) and ('abiliti' in locals()) and ('spesies' not in locals()) and ('weight' in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where weight {weight} and height {height} group by 1 having count(nama) {abiliti};"
elif ('nama_abl' not in locals()) and ('abiliti' not in locals()) and ('spesies' in locals()) and ('weight' in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where species IN {spesies} and weight {weight} and height {height} group by 1;"

elif ('nama_abl' in locals()) and ('abiliti' in locals()) and ('spesies' in locals()) and ('weight' in locals()) and ('height' in locals()):
    query = f"select nama from pokemon where abilities IN {nama_abl} and species IN {spesies} and weight {weight} and height {height} group by 1 having count(nama) {abiliti};"


cur.execute(query)
hasil = cur.fetchall()
print(tabulate(hasil, headers=['nama'], tablefmt='psql'))


