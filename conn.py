import pymysql #Librairie auxliaire
conn = pymysql.connect(host="localhost",user='root',database="Database")
arp = conn.cursor()
arp.execute('SELECT * FROM Annonce')
result = arp.fetchall()
for row in result: 
    print(type(row)) 
    print("\n") 