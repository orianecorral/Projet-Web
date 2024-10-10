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


the_cursor = cnx.cursor(dictionary=True)

the_cursor.execute('INSERT INTO Utilisateurs( prenom,nom,email,telephone,mdp) VALUES("Jean","Castex","Jean.Castex@gmail.com","08 36 65 65 65","Jupiter")')
cnx.commit()

the_cursor.close()

cnx.close()