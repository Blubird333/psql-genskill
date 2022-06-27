import sys
import csv
import psycopg2

# Method to extract things from the database.
def dump(fname):
    dbconn = psycopg2.connect("dbname=superhero")
    curs = dbconn.cursor()

    f = open(fname,"w")
    writer = csv.writer(f)

    curs.execute("SELECT name,gender FROM heroes;")                             # to get things from the database.

    for name,gender in curs.fetchall():
        print(name,gender)                                                      # to print the things extracted from database in the terminal.
        writer.writerow([name,gender])                                          # to insert the things extracted from database in the file.


    f.close()

    curs.close()
    dbconn.close()


#Main method.
def main():
    extract_file = sys.argv[1]
    dump(extract_file)


main()
