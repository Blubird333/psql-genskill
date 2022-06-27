#cursor is an api kind of thing. It is used to access the database.



import csv        #To pass the csv file(heroes.csv)
import sys        #To read the argv passed after 'python3 ingest.py' in the terminal.
import psycopg2   #To connect the database.

# method to insert things into the database.
def insert(fname):
    dbconn = psycopg2.connect("dbname=superhero user=dheeraj")
    curs = dbconn.cursor()

    f = open(fname)
    reader = csv.reader(f)
    for name,gender in reader:
        print(name,gender,"    ....inserted")
        curs.execute("INSERT INTO heroes(name,gender) VALUES(%s,%s);",(name,gender))

    dbconn.commit()

    curs.close()
    dbconn.close()



#Main method.
def main():
    insert_file = sys.argv[1]
    insert(insert_file)


main()


conn = psycopg2.connect("dbname=superhero user=dheeraj")
cur = conn.cursor()

cur.execute("INSERT INTO heroes(name,gender) VALUES(%s,%s);",("Spiderman","m"))
print("-------new hero:\n","Spiderman","m","    ....inserted")

conn.commit()

cur.close()
conn.close()
