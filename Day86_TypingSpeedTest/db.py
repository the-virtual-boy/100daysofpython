import sqlite3

## database stuff

#create db connection
conn = sqlite3.connect('dictionary')

#create cursor
c = conn.cursor()

# #create table
# c.execute("""CREATE TABLE words (
#           word text,
#           letters integer
#           )""")

#create add function
def submit():
    #create db

    #creat cursor

    #insert
    c.execute(f'INSERT INTO words VALUES (:var1, :var2)')

#commit changes
conn.commit()
#close connection
conn.close()