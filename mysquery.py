import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="darshanbhai",
    database="myproject")


mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Images (id SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,Photo LONGBLOB NOT NULL)")

def insertblob(filepath):
    with open(filepath,"rb") as file:
        binarydata=file.read()
    SQlstatement="INSERT INTO Images (photo) VALUES (%s)"
    mycursor.execute(SQlstatement,(binarydata,))
    mydb.commit()



def retrieveimg():
    SQLstatement2="SELECT * FROM IMAGES ORDER BY id"
    mycursor.execute(SQLstatement2)
    myresult=mycursor.fetchall()
    for x in myresult:
        storagefile="C:/Users/Harsh/Desktop/sem 6 project/application/prev_images/{}.jpg".format(str(x[0]))
        with open(storagefile,"wb")as file:
            file.write(x[1])
            file.close()        




