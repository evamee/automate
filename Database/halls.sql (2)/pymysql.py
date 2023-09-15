import pymysql

connection = pymysql.connect(host='localhost',port=3306, user='root', password='', database='boss')
mcursor = connection.cursor()

mcursor.execute("SELECT first_choice,gender,name,id FROM tbl_biodata_attach")

 
mcursor.execute("CREATE TABLE Assigned halls ( id INT AUTO_INCREMENT PRIMARY KEY name VARCHAR(255), gender VARCHAR(255) SRC int(200), Liberty Hall int(100) Ashanti Hall int(100))")


LibertyCounter= 0
AshantiCounter = 0


for x in mcursor:
    if x == 'ATE' and x == 'FEMALE':
        sql = "INSERT INTO Assigned halls(id,name,gender,SRC) VALUES(%s,%s,%s,%s)"
        mcursor.execute(sql)
        connection.commit()

    elif x == "MALE" and x != 'ATE' and LibertyCounter <= 100 :
        sql_2 = "INSERT INTO Assigned halls(id,name,gender,Liberty Hall) VALUES(%s,%s,%s%s)"
        mcursor.execute(sql_2)
        connection.commit
        LibertyCounter+=1

    
    elif x == "MALE" and x != 'ATE' and AshantiCounter <= 100 :
        sql_3 = "INSERT INTO Assigned halls(id,name,gender,Ashanti Hall) VALUES(%s,%s,%s%s)"
        mcursor.execute(sql_2)
        connection.commit
        AshantiCounter +=1

    else:
