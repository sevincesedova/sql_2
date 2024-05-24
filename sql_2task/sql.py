import sqlite3
connection=sqlite3.connect("films")
cursor=connection.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS FILMS (ad TEXT, il INT, yonetmen TEXT, janr TEXT)")
    connection.commit()

def add_table():
    cursor.execute("INSERT INTO films VALUES('Pianist',2002,'Roman Polanski','Drama'),")
    connection.commit()

# ad=input("filmin adini qeyd edin: ")
# il=int(input("filmin cixis ilini qeyd edin: "))
# yonetmen=input("filmin yonetmenini qeyd edin: ")
# janr=input("filmin janrini qeyd edin: ")

def dynamic_add_table(ad,il,yonetmen,janr):
    cursor.execute("INSERT INTO films VALUES(?,?,?,?)",(ad,il,yonetmen,janr))
    connection.commit()

def delete_film(ad):
    cursor.execute("DELETE FROM films WHERE ad=?", (ad,))
    connection.commit()


def show_films_2010():
    cursor.execute("SELECT * FROM films WHERE il >= 2010")
    data = cursor.fetchall()
    for row in data:
        print(row)
        
show_films_2010()
# filmdelete = input("Silmek istediyiniz filmin adını qeyd edin: ")
# delete_film(filmdelete)
# dynamic_add_table(ad,il,yonetmen,janr)
# create_table()
# add_table()
connection.close()