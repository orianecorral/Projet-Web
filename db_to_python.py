import mysql.connector
from mysql.connector import errorcode

from config import config


try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err : 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorect user or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Incorect database")
    else:
        print(err)


    exit()

# Création du curseur pour selectionner les éléments dans la base de donné
#Grace au dictionary=True je met tous les éléments de chaque ligne dans un dictionnaire

the_cursor = cnx.cursor(dictionary=True)

# Selectionner la table 
the_cursor.execute('SELECT * FROM Annonces')
result = the_cursor.fetchall()

print(result[0]["titre"])

the_cursor.close()

cnx.close()

# conn = pymysql.connect(host="localhost",user='root',database="Database")
# arp = conn.cursor()
# arp.execute('SELECT * FROM Annonce')
# result = arp.fetchall()
# for row in result: 
#     print(row) 
#     print("\n") 