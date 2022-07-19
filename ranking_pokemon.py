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

query = "SELECT nama, COUNT(*) AS rnk FROM abuser.pokemon GROUP BY 1 order BY 2 DESC"

cur = conn.cursor()
cur.execute(query)
hasil = cur.fetchall()

print(tabulate(hasil, headers=['nama','jumlah abiliti'], tablefmt='psql'))