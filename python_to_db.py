import mysql.connector
from mysql.connector import errorcode
import hashlib
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

MDP = hashlib.md5(b'Julien')
MDO = MDP.hexdigest()
the_cursor = cnx.cursor(dictionary=True)
#push ce qui se trouve dans le .execute dans la base de donnée
the_cursor.execute('INSERT INTO Utilisateurs( prenom,nom,email,telephone,mdp) VALUES("Jean","Castex","Jean.Castex@gmail.com","08 36 65 65 65",%s)',(MDO,))  
#le %S indique qu'on remplace ça par une variable qui sera mis juste après ,ici MDO est la variable encodé , il faut bien mettre une virgule juste après MDO car sinon ils demanderons de mettre une liste ou un tuple à la place
cnx.commit()

the_cursor.close()

cnx.close()